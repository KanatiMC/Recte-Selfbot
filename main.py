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
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")
from os import system

try:
    import json
except ModuleNotFoundError:
    os.system("pip install json")

system("title " + "Recte Selfbot By Kanati")

token = ""
prefix = ""


def logInfo(log: str):
    return f"{Fore.LIGHTBLUE_EX}{Style.DIM}{log}{Fore.RESET}{Style.RESET_ALL}"


def logError(log: str):
    return f"{Fore.LIGHTRED_EX}{Style.DIM}{log}{Fore.RESET}{Style.RESET_ALL}"


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


input_string = text2art("Recte", font="tarty123")
try:
    rgb_wave_text(input_string, speed=0.2)
except KeyboardInterrupt:
    pass


def headers(header_token: str):
    # Your header generation logic here
    return {"Authorization": header_token, "accept": "*/*", "accept-language": "en-US", "connection": "keep-alive",
            "cookie": f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US", "DNT": "1",
            "origin": "https://discord.com", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin", "referer": "https://discord.com/channels/@me", "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9007 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
            "X-Context-Properties": "e30=",
            "X-Debug-Options": "bugReporterEnabled",
            "X-Discord-Locale": "en-GB",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wKChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwNy4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwNy4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTYzMDM1LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}


def check(tokenToCheck):
    resp = requests.get('https://discord.com/api/v9/users/@me', headers=headers(tokenToCheck))
    if resp.status_code == 200:
        return True
    else:
        return False


async def main():
    global prefix
    global token

    with open("config.json") as f:
        data = json.load(f)
        if len(data['token']) != 0 and check(data['token']):
            print("Config Token Is Valid.")
            token = data['token']
        else:
            token = ""
            while True:
                token = input("Token: ")
                if check(token):
                    print("Token is valid.")
                    break
                else:
                    print("Invalid token. Please try again.")
        if len(data['prefix']) == 0:
            prefix = input("Prefix: ")
        elif len(data['prefix']) != 0:
            print("Prefix Loaded")
            prefix = data['prefix']

    # Move the bot creation and other setup here, inside the main function
    bot = commands.Bot(command_prefix=prefix, self_bot=True, case_insensitive=True)
    bot.remove_command("help")
    cogCount = await load(bot)
    if cogCount == 0:
        print(f"{logInfo('[Cogs]:')} Zero Cogs Loaded")
    elif cogCount == 1:
        print(f"{logInfo('[Cogs]:')} One Cog Loaded")
    elif cogCount >= 2:
        print(f"{logInfo('[Cogs]:')} {str(cogCount)} Cogs Loaded")
    else:
        print(f"{logError('[Cogs]:')} An Error Has Occurred.")
    await bot.start(token)


async def load(bot: discord.Client):
    i: int = 0
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            i += 1
    return i


asyncio.run(main())
