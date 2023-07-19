import discord
from discord.ext import commands
from colorama import Fore, Style
import asyncio
import time


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def logInfo(self, log: str):
        return f"{Fore.LIGHTBLUE_EX}{Style.DIM}{log}{Fore.RESET}{Style.RESET_ALL}"

    def logError(self, log: str):
        return f"{Fore.LIGHTRED_EX}{Style.DIM}{log}{Fore.RESET}{Style.RESET_ALL}"

    mappings = {"roles": {}, "categories": {}, "webhooks": {}, "channels": {}, "messages": {}}

    async def prepareServer(self, guild: discord.Guild):
        try:
            if guild is None:
                return

            for channel in guild.channels:
                await channel.delete()
                print(f"{Fore.LIGHTBLUE_EX}[Prepering Server]{Fore.RESET} Deleted Channel: {channel.name}")
                await asyncio.sleep(.75)
            for role in guild.roles:
                try:
                    if role.name != "@everyone":
                        await role.delete()
                        print(f"{Fore.LIGHTBLUE_EX}[Prepering Server]{Fore.RESET} Deleted Role: {role.name}")
                        await asyncio.sleep(.8)
                except discord.Forbidden:
                    print(f"{Fore.RED}[Error]{Fore.RESET} Insufficient permissions to delete the role: {role.name}")
                except discord.HTTPException:
                    print(f"{Fore.RED}[Error]{Fore.RESET} Invalid Role: {role.name}")
            for emoji in guild.emojis:
                await emoji.delete()
                print(f"{Fore.LIGHTBLUE_EX}[Prepering Server]{Fore.RESET} Deleted Emoji: {emoji.name}")
                await asyncio.sleep(.8)
            for sticker in guild.stickers:
                await sticker.delete()
                print(f"{Fore.LIGHTBLUE_EX}[Prepering Server]{Fore.RESET} Deleted Sticker: {sticker.name}")
                await asyncio.sleep(.8)
        except discord.RateLimited as e:
            print(f"{Fore.RED}[Error]{Fore.RESET} {e}")
            return

    async def cloneInfo(self, oldGuild: discord.Guild, newGuild: discord.Guild):
        try:
            if oldGuild.icon is not None:
                print(f"{Fore.LIGHTBLUE_EX}[Info Cloning]{Fore.RESET} Cloning Icon")
                icon_data = await oldGuild.icon.read()
                await newGuild.edit(icon=icon_data)
                print(f"{Fore.LIGHTBLUE_EX}[Info Cloning]{Fore.RESET} Icon Cloned")
            if oldGuild.icon is None:
                print(f"{Fore.LIGHTBLUE_EX}[Info Cloning]{Fore.RESET} No Icon Detected, Removing Icon...")
                await newGuild.edit(icon=None)
                print(f"{Fore.LIGHTBLUE_EX}[Info Cloning]{Fore.RESET} Icon Removed")
            if newGuild.premium_tier >= 2:
                if oldGuild.banner is not None:
                    print(f"{Fore.LIGHTBLUE_EX}[Info Cloning]{Fore.RESET} Cloning Banner")
                    banner_data = await oldGuild.banner.read()
                    await newGuild.edit(banner=banner_data)
                    print(f"{Fore.LIGHTBLUE_EX}[Info Cloning]{Fore.RESET} Banner Cloned")
                if oldGuild.banner is None:
                    print(f"{Fore.LIGHTBLUE_EX}[Info Cloning]{Fore.RESET} No Banner Detected, Removing Banner...")
                    await newGuild.edit(banner=None)
                    print(f"{Fore.LIGHTBLUE_EX}[Info Cloning]{Fore.RESET} Banner Removed")
            if oldGuild.name is not None:
                await newGuild.edit(name=oldGuild.name)
                print(f"{Fore.LIGHTBLUE_EX}[Info Cloning]{Fore.RESET} Guild Name Changed")

        except discord.RateLimited as e:
            print(f"{Fore.RED}[Error]{Fore.RESET} {e}")
            await asyncio.sleep(e.retry_after)
            await self.cloneInfo(oldGuild, newGuild)
            return

    async def cloneRoles(self, oldGuild: discord.Guild, newGuild: discord.Guild):
        global mappings
        try:
            roles_create = []
            role: discord.Role
            print(f"{Fore.LIGHTBLUE_EX}[Role Cloning]{Fore.RESET} Saving Role Permissions")
            for role in oldGuild.roles:
                if role.name != "@everyone":
                    roles_create.append(role)
                else:
                    mappings["roles"][role] = discord.utils.get(newGuild.roles, name="@everyone")
            for role in reversed(roles_create):
                new_role = await newGuild.create_role(name=role.name, colour=role.colour, hoist=role.hoist,
                                                      mentionable=role.mentionable, permissions=role.permissions)
                mappings["roles"][role] = new_role
                print(f"{Fore.LIGHTBLUE_EX}[Role Cloning]{Fore.RESET} Role Created: " + str(
                    new_role.id) + " | " + new_role.name)
                await asyncio.sleep(.8)
        except discord.RateLimited as e:
            print(f"{Fore.RED}[Error]{Fore.RESET} {e}")
            await asyncio.sleep(e.retry_after)
            await self.cloneRoles(oldGuild, newGuild)
            return

    async def cloneCategories(self, oldGuild: discord.Guild, newGuild: discord.Guild, perms: bool = True):
        try:
            for category in oldGuild.categories:
                overwrites: dict = {}
                if perms:
                    for role, permissions in category.overwrites.items():
                        if isinstance(role, discord.Role):
                            overwrites[mappings["roles"][role]] = permissions
                new_category = await newGuild.create_category(name=category.name, position=category.position,
                                                              overwrites=overwrites)
                mappings["categories"][category] = new_category
                print(
                    f"{Fore.LIGHTBLUE_EX}[Category Cloning]{Fore.RESET} Category Created: {str(new_category.id)} | {new_category.name}")
                await asyncio.sleep(.7)
        except discord.RateLimited as e:
            print(f"{Fore.RED}[Error]{Fore.RESET} {e}")
            await asyncio.sleep(e.retry_after)
            await self.cloneCategories(oldGuild, newGuild)
            return

    async def cloneChannels(self, oldGuild: discord.Guild, newGuild: discord.Guild, perms: bool = True):
        try:
            for channel in oldGuild.channels:
                category = mappings.get("categories", {}).get(channel.category, None)
                overwrites: dict = {}
                if perms:
                    for role, permissions in channel.overwrites.items():
                        if isinstance(role, discord.Role):
                            overwrites[mappings["roles"][role]] = permissions
                if isinstance(channel, discord.TextChannel):
                    new_channel = await newGuild.create_text_channel(name=channel.name,
                                                                     position=channel.position,
                                                                     topic=channel.topic,
                                                                     slowmode_delay=channel.slowmode_delay,
                                                                     nsfw=channel.nsfw,
                                                                     category=category,
                                                                     overwrites=overwrites)
                    mappings["channels"][channel] = new_channel
                    print(
                        f"{Fore.LIGHTBLUE_EX}[Channel Cloning]{Fore.RESET} Channel Created: {str(new_channel.id)} | {new_channel.name}")

                elif isinstance(channel, discord.VoiceChannel):
                    bitrate = channel.bitrate if channel.bitrate <= 96000 else None
                    new_channel = await newGuild.create_voice_channel(name=channel.name,
                                                                      position=channel.position,
                                                                      bitrate=bitrate,
                                                                      user_limit=channel.user_limit,
                                                                      category=category,
                                                                      overwrites=overwrites)
                    print(
                        f"{Fore.LIGHTBLUE_EX}[Channel Cloning]{Fore.RESET} Voice Channel Created: {str(new_channel.id)} | {new_channel.name}")
                await asyncio.sleep(.7)
        except discord.RateLimited as e:
            print(f"{Fore.RED}[Error]{Fore.RESET} {e}")
            await asyncio.sleep(e.retry_after)
            await self.cloneChannels(oldGuild, newGuild)
            return

    async def cloneEmojis(self, oldGuild: discord.Guild, newGuild: discord.Guild):
        try:
            max_emojis = newGuild.emoji_limit
            available_slots = max_emojis - len(newGuild.emojis)
            if available_slots <= 0:
                print(f"{Fore.LIGHTRED_EX}[Emoji Cloning]{Fore.RESET} Cannot Create More Emojis")
                return

            emojis_to_clone = min(available_slots, len(oldGuild.emojis))
            for emoji in oldGuild.emojis[:emojis_to_clone]:
                try:
                    print(
                        f"{Fore.LIGHTBLUE_EX}[Emoji Cloning]{Fore.RESET} Creating Emoji: {str(emoji.id)} | {emoji.name}")
                    await newGuild.create_custom_emoji(name=emoji.name, image=await emoji.read())
                    print(f"{Fore.LIGHTBLUE_EX}[Emoji Cloning]{Fore.RESET} Created Emoji")
                    await asyncio.sleep(.7)
                except discord.HTTPException:
                    print(print(f"{Fore.RED}[Error]{Fore.RESET} Unable To Resize Emoji"))

        except discord.RateLimited as e:
            print(f"{Fore.RED}[Error]{Fore.RESET} {e}")
            await asyncio.sleep(e.retry_after)
            await self.cloneEmojis(oldGuild, newGuild)
            return

    @commands.command()
    async def clone(self, ctx: commands.Context, OldID: int, newGuildID: int):
        start_time = time.time()
        oldGuild: discord.Guild = self.bot.get_guild(OldID)
        newGuild: discord.Guild = self.bot.get_guild(newGuildID)
        msg = await ctx.send("Cloning Started!")
        await msg.edit(content="Preparing Server...")
        await self.prepareServer(newGuild)
        await msg.edit(content="Info Cloning...")
        await self.cloneInfo(oldGuild, newGuild)
        await msg.edit(content="Cloning Roles...")
        await self.cloneRoles(oldGuild, newGuild)
        await msg.edit(content="Cloning Categories...")
        await self.cloneCategories(oldGuild, newGuild, True)
        await msg.edit(content="Cloning Channels...")
        await self.cloneChannels(oldGuild, newGuild, True)
        await msg.edit(content="Cloning Emojis...")
        await self.cloneEmojis(oldGuild, newGuild)
        await msg.edit(content=f"Server Cloned! It Took {round((time.time() - start_time), 2)} Seconds.")
        print(f"{Fore.LIGHTBLUE_EX}[Log]{Fore.RESET} Server Cloning Complete")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def hide(self, ctx, channel: discord.Optional[discord.TextChannel]):
        if channel is None:
            channel = ctx.message.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.view_channel = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.reply(f"Channel: {channel.name} Is Now Visible")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unhide(self, ctx, channel: discord.Optional[discord.TextChannel]):
        if channel is None:
            channel = ctx.message.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.view_channel = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.reply(f"Channel: {channel.name} Is Now Visible")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.Optional[discord.TextChannel]):
        if channel is None:
            channel = ctx.message.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send('Channel locked.')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: discord.Optional[discord.TextChannel]):
        if channel is None:
            channel = ctx.message.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send('Channel Unlocked.')

    @commands.command(aliases=["clear", "prg", "clr"])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=30):
        if ctx.message.author.guild_permissions.manage_messages:
            channel = ctx.message.channel
            messages = []
            async for message in channel.history(limit=amount + 1):
                messages.append(message)
            await channel.delete_messages(messages)
            await ctx.send(
                f'{ctx.message.author.mention} Has Purged {amount} Messages')
            print(f"{self.logInfo('[Logging]:')} {ctx.author} Has Just Purged {amount} Message(s)")
        else:
            await ctx.send(
                "You're Missing The Correct Permissions For This Command.")


async def setup(bot):
    await bot.add_cog(Admin(bot))
