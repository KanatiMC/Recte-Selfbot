import discord
from discord.ext import commands
from colorama import Fore


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command(name="channelinfo")
    async def cinfo(self, ctx, channel: discord.Optional[discord.TextChannel]):
        if channel is None:
            channel = ctx.message.channel
        info = f"Channel Information\n\n" \
               f"**Name:** {channel.name}\n" \
               f"**ID:** {channel.id}\n" \
               f"**Type:** {channel.type}\n" \
               f"**Position:** {channel.position}\n" \
               f"**Category:** {channel.category.name if channel.category else 'None'}\n" \
               f"**Topic:** {channel.topic if channel.topic else 'None'}\n" \
               f"**NSFW:** {channel.is_nsfw()}\n" \
               f"**Slowmode Delay:** {channel.slowmode_delay}\n" \
               f"**Creation Time:** {channel.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        await ctx.reply(info)

    @commands.command(aliases=['il'])
    async def invitelist(self, ctx):
        inviteCodes = []
        for invite in await ctx.guild.invites():
            inviteCodes.append(f"{invite.code} | {invite.inviter}\n")
        inviteCodes.reverse()  # to make it higher first
        a = str(inviteCodes)
        embed = discord.Embed(title="Invite Codes", description=a.strip('"[]'))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def roles(self, ctx):
        all_roles = []
        for role in ctx.guild.roles:
            all_roles.append(role.name)
        all_roles.reverse()  # to make it higher first
        all_roles.remove("@everyone")
        embed = discord.Embed(title="Server Roles", description=all_roles)
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(name="roleinfo")
    async def rinfo(self, ctx, role: discord.Role):
        info = f"Role Information\n\n" \
               f"**Name:** {role.name}\n" \
               f"**ID:** {role.id}\n" \
               f"**Color:** {role.color}\n" \
               f"**Mentionable:** {role.mentionable}\n" \
               f"**Permissions:** {role.permissions.value}\n" \
               f"**Created At:** {role.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        await ctx.reply(info)

    @commands.command(name="guildinfo")
    async def ginfo(self, ctx, guild: discord.Optional[discord.Guild]):
        if guild is None:
            guild = ctx.message.guild
        await ctx.reply(f"Guild Information\n\n"
                        f"**Name:** {guild.name}\n"
                        f"**ID:** {guild.id}\n"
                        f"**Description:** {guild.description}\n"
                        f"**Boost Level:**{guild.premium_tier}\n"
                        f"**System Channel:** {guild.system_channel}\n"
                        f"**AFK Channel:** {guild.afk_channel}\n"
                        f"**Created At:** {guild.created_at}\n"
                        f"**Default Role:** {guild.default_role}\n"
                        f"**Member Count:** {guild.member_count}\n"
                        f"**Online Count:** {guild.online_count}\n"
                        f"**Owner:** {guild.owner}\n"
                        )


async def setup(bot):
    await bot.add_cog(Info(bot))
