import os

try:
    import discord
except ModuleNotFoundError:
    os.system("pip install discord.py-self")
try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
from discord.ext import commands

try:
    from art import *
except ModuleNotFoundError:
    os.system("pip install art")
try:
    import time
except ModuleNotFoundError:
    os.system("pip install time")
try:
    import base64
except ModuleNotFoundError:
    os.system("pip install base64")
try:
    import random
except ModuleNotFoundError:
    os.system("pip install random")
try:
    import asyncio
except ModuleNotFoundError:
    os.system("pip install asyncio")
try:
    import string
except ModuleNotFoundError:
    os.system("pip install string")
try:
    import math
except ModuleNotFoundError:
    os.system("pip install math")
try:
    import shutil
except ModuleNotFoundError:
    os.system("pip install shutil")
try:
    from colorama import Fore
except ModuleNotFoundError:
    os.system("pip install colorama")
from os import system

system("title " + "Recte Selfbot By Kanati")


def rgb_wave_text(text, speed=1):
    # Get the dimensions of the console
    columns, rows = shutil.get_terminal_size()

    # Split the input text into lines
    lines = text.strip().split("\n")
    longest_line = max(len(line) for line in lines)

    colored_characters = []

    # Generate the color for each character
    for y in range(len(lines)):
        line = lines[y]

        # Calculate padding for this line
        padding_left = (columns - len(line)) // 2
        padding_right = columns - len(line) - padding_left

        # Color the padding spaces on the left
        padding_left = ' ' * padding_left

        # Color the padding spaces on the right
        padding_right = ' ' * padding_right

        color_line = padding_left

        for x in range(len(line)):
            # Calculate the RGB values
            r = (math.sin(speed * (x + y) + 0) * 127 + 128)
            g = (math.sin(speed * (x + y) + 2) * 127 + 128)
            b = (math.sin(speed * (x + y) + 4) * 127 + 128)

            # Convert the RGB values to an escape code
            rgb_escape = f"\033[38;2;{int(r)};{int(g)};{int(b)}m"

            # Add the escape code and the character to the current line
            color_line += rgb_escape + line[x]

        # Add padding at the end of line
        color_line += padding_right

        # Add the current line to our list of colored lines
        colored_characters.append(color_line)

    # Pad empty lines above and below the text
    padding_top = [' ' * columns] * ((rows - len(lines)) // 2)
    padding_bottom = [' ' * columns] * (rows - len(lines) - len(padding_top))
    colored_characters = padding_top + colored_characters + padding_bottom

    # Join the colored lines together with newline characters
    colored_text = '\n'.join(colored_characters)

    # Print the colored text, and reset colors afterwards
    print(colored_text + "\033[0m")


if __name__ == "__main__":
    input_string = text2art("Recte", font="tarty123")
    try:
        rgb_wave_text(input_string, speed=0.2)
    except KeyboardInterrupt:
        pass


def headers(header_token: str):
    return {"Authorization": header_token, "accept": "*/*", "accept-language": "en-US", "connection": "keep-alive",
            "cookie": f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US", "DNT": "1",
            "origin": "https://discord.com", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin", "referer": "https://discord.com/channels/@me", "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9007 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
            "X-Context-Properties": "e30=",
            "X-Debug-Options": "bugReporterEnabled",
            "X-Discord-Locale": "en-GB",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwNy4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwNy4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTYzMDM1LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}


def check(tokenToCheck):
    resp = requests.get('https://discord.com/api/v9/users/@me', headers=headers(token))
    if resp.status_code == 200:
        return True
    else:
        return False


while True:
    token = input("Token: ")
    if check(token):
        print("Token is valid.")
        break
    else:
        token = ""
        print("Invalid token. Please try again.")

prefix = input("Prefix: ")

bot = commands.Bot(command_prefix=prefix, self_bot=True, case_insensitive=True)
bot.remove_command("help")



@bot.event
async def on_ready():
    print(f"Welcome, {Fore.LIGHTRED_EX}{bot.user.name}{Fore.RESET}"
          "\nInfo:"
          f"\n  Username: {bot.user.name}"
          f"\n  Display Name: {bot.user.display_name}"
          f"\n  ID: {bot.user.id}"
          f"\n  Discriminator: {bot.user.discriminator}")

@bot.command(name="prefix")
async def prefixChange(ctx, prefix2Set:str):
    if prefix2Set is not None:
        global prefix
        prefix = prefix2Set
        await ctx.reply(f"Prefix Has Been Changed To: `{prefix2Set}`")

@bot.command()
async def help(ctx):
    await ctx.reply(
        f"```{prefix}clone <guild1 ID> <guild2 ID>\n"
        "Clones The Guild1 Server To Guild2 \n\n"
        f"{prefix}status <mode> <name>\n"
        "Sets A Custom Status To The Bot\n\n"
        f"{prefix}base64encode <string>\n"
        "Sends The String, But Encoded By Base64\n\n"
        f"{prefix}base64decode <strings>\n"
        "Decodes The String If It Was Decrypted With Base64\n\n"
        f"{prefix}chanelinfo <channel>(optional)\n"
        "Sends Info On The Channel, If There Is None Then It Sends Info On The Channel From This Message\n\n"
        f"{prefix}roleinfo <role>\n"
        "Sends Info On A Picked Role\n\n"
        f"{prefix}ascii <font>(optional) <text>\n"
        "Sends ASCII Art Of The Chosen Text With The Chosen Font\n\n"
        f"{prefix}nitro\n"
        "Generates A Fake Nitro, With The Possibility Of Being Real\n\n"
        f"{prefix}hide <displayText> <hiddenText>\n"
        "Sends A Message With <hiddenText> Being Hidden, But <displayText> Being Visible\n\n"
        f"{prefix}minesweeper <size>\n"
        "Creates A Minesweeper Game With The Chosen Size\n\n"
        f"{prefix}1337 <text>\n"
        "Sends A Message With Super Hacker Text```"
    )


mappings = {"roles": {}, "categories": {}, "webhooks": {}, "channels": {}, "messages": {}}


@bot.command()
async def base64encode(ctx, *, str):
    encoded = base64.b64encode(str.encode()).decode()
    await ctx.reply(f"Here Is Your Encoded String: ```{encoded}```")


@bot.command()
async def base64decode(ctx, *, str):
    decoded = base64.b64decode(str.encode()).decode()
    await ctx.reply(f"Here Is Your Decoded String: ```{decoded}```")


@bot.command()
async def channelinfo(ctx, channel: discord.Optional[discord.TextChannel]):
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
    await ctx.send(info)


@bot.command()
async def roleinfo(ctx, role: discord.Role):
    info = f"Role Information\n\n" \
           f"**Name:** {role.name}\n" \
           f"**ID:** {role.id}\n" \
           f"**Color:** {role.color}\n" \
           f"**Mentionable:** {role.mentionable}\n" \
           f"**Permissions:** {role.permissions.value}\n" \
           f"**Created At:** {role.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    await ctx.send(info)


@bot.command()
async def ascii(ctx, font: discord.Optional[str], *, text=None):
    if text is None:
        await ctx.send(f'Error, Must Have A Text Argument.')
        return
    msg = ""
    if font is None:
        msg = text2art(text)
    if font is not None:
        msg = text2art(text, font)
    await ctx.send(f"```{msg}```"
                   "Check Out More Fonts At http://kanati.bio/fonttypes.txt")

#Taken From https://github.com/KxleLmao/DiscordSelfbot
@bot.command()
async def nitro(ctx):
    await ctx.reply(
        f'Here Is You Generated Nitro Code: \nhttps://discord.gift/{"".join(random.choices(string.ascii_letters + string.digits, k=16))}')

#Taken From https://github.com/KxleLmao/DiscordSelfbot
@bot.command()
async def hide(ctx, displayText=None, hiddenText=None):
    await ctx.message.delete()
    if displayText is None and hiddenText is None:
        await ctx.send(f'[Error]: Invalid input!')
        return
    await ctx.send(displayText + ('||\u200b||' * 200) + hiddenText)


m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

#Taken From https://github.com/KxleLmao/DiscordSelfbot
@bot.command()
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

#Taken From https://github.com/KxleLmao/DiscordSelfbot
@bot.command(name="1337")
async def _1337(ctx, *, text=None):
    await ctx.message.delete()
    if text is None:
        await ctx.send(f'[Error]: Invalid input!')
        return
    text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
        .replace('E', '3').replace('i', '!').replace('I', '!') \
        .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'{text}')


@bot.command()
async def status(ctx, mode, *, name):
    mode = mode.lower()
    if "watching" in mode:
        watching = discord.Streaming(name=name, url="https://kanati.gay")
        await bot.change_presence(activity=watching)
    elif "playing" in mode:
        game = discord.Game(name=name)
        await bot.change_presence(activity=game)
    elif "custom" in mode:
        competing = discord.CustomActivity(name=name)
        await bot.change_presence(activity=competing)
    else:
        await ctx.send("Invalid mode. Please choose one of 'watching', 'playing', or 'custom'.")
        return
    await ctx.reply("Status Has Been Changed")


async def prepareServer(guild: discord.Guild):
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


async def cloneInfo(oldGuild: discord.Guild, newGuild: discord.Guild):
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
        await cloneInfo(oldGuild, newGuild)
        return


async def cloneRoles(oldGuild: discord.Guild, newGuild: discord.Guild):
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
        await cloneRoles(oldGuild, newGuild)
        return


async def cloneCategories(oldGuild: discord.Guild, newGuild: discord.Guild, perms: bool = True):
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
        await cloneCategories(oldGuild, newGuild)
        return


async def cloneChannels(oldGuild: discord.Guild, newGuild: discord.Guild, perms: bool = True):
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
        await cloneChannels(oldGuild, newGuild)
        return


async def cloneEmojis(oldGuild: discord.Guild, newGuild: discord.Guild):
    try:
        max_emojis = newGuild.emoji_limit
        available_slots = max_emojis - len(newGuild.emojis)
        if available_slots <= 0:
            print(f"{Fore.LIGHTRED_EX}[Emoji Cloning]{Fore.RESET} Cannot Create More Emojis")
            return

        emojis_to_clone = min(available_slots, len(oldGuild.emojis))
        for emoji in oldGuild.emojis[:emojis_to_clone]:
            try:
                print(f"{Fore.LIGHTBLUE_EX}[Emoji Cloning]{Fore.RESET} Creating Emoji: {str(emoji.id)} | {emoji.name}")
                await newGuild.create_custom_emoji(name=emoji.name, image=await emoji.read())
                print(f"{Fore.LIGHTBLUE_EX}[Emoji Cloning]{Fore.RESET} Created Emoji")
                await asyncio.sleep(.7)
            except discord.HTTPException:
                print(print(f"{Fore.RED}[Error]{Fore.RESET} Unable To Resize Emoji"))

    except discord.RateLimited as e:
        print(f"{Fore.RED}[Error]{Fore.RESET} {e}")
        await asyncio.sleep(e.retry_after)
        await cloneEmojis(oldGuild, newGuild)
        return






@bot.command()
async def clone(ctx: commands.Context, OldID: int, newGuildID: int):
    start_time = time.time()
    oldGuild: discord.Guild = bot.get_guild(OldID)
    newGuild: discord.Guild = bot.get_guild(newGuildID)
    msg = await ctx.send("Cloning Started!")
    await msg.edit(content="Preparing Server...")
    await prepareServer(newGuild)
    await msg.edit(content="Info Cloning...")
    await cloneInfo(oldGuild, newGuild)
    await msg.edit(content="Cloning Roles...")
    await cloneRoles(oldGuild, newGuild)
    await msg.edit(content="Cloning Categories...")
    await cloneCategories(oldGuild, newGuild, True)
    await msg.edit(content="Cloning Channels...")
    await cloneChannels(oldGuild, newGuild, True)
    await msg.edit(content="Cloning Emojis...")
    await cloneEmojis(oldGuild, newGuild)
    await msg.edit(content=f"Server Cloned! It Took {round((time.time() - start_time), 2)} Seconds.")
    print(f"{Fore.LIGHTBLUE_EX}[Log]{Fore.RESET} Server Cloning Complete")


bot.run(token)
