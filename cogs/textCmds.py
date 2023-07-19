import discord
from discord.ext import commands
from colorama import Fore
import base64
from art import *
import random
import string
import os
try:
    from owoify.owoify import owoify, Owoness
except ModuleNotFoundError:
    os.system("pip install owoify.py")
import requests


class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['owoify'])
    async def owo(self, ctx, *, text2owo):
        await ctx.message.delete()
        await ctx.send(owoify(text2owo, Owoness.Uvu))

    @commands.command(aliases=["ip"])
    async def iplookup(self, ctx, *, ipaddr: str = '9.9.9.9'):
        r = requests.get(
            f"http://extreme-ip-lookup.com/json/{ipaddr}?key=DxDovPAsEimfELYYWnS0")
        geo = r.json()
        return await ctx.reply(f"```IP Lookup"
                               f"\nIP: {geo['query']}"
                               f"\nIP Type: {geo['iptype']}"
                               f"\nCountry: {geo['Country']}"
                               f"\nCity: {geo['city']}"
                               f"\nContinent: {geo['continent']}"
                               f"\nIP Name: {geo['ipName']}"
                               f"\nISP: {geo['isp']}"
                               f"\nLatitude: {geo['lat']}"
                               f"\nLongitude: {geo['lon']}"
                               f"\nOrg: {geo['org']}"
                               f"\nRegion: {geo['region']}"
                               f"\nStatus: {geo['status']}```")

    @commands.command()
    async def translate(self, ctx, toLang, fromLang, *, text):
        print(text, toLang, fromLang)
        resp = requests.get(f"https://api.popcat.xyz/translate?to={toLang}&from={fromLang}&text={text}")
        res = resp.json()
        try:
            await ctx.reply("```Translator"
                            f"\n{res['translated']}```")
        except:
            await ctx.reply(f"```Error!\n{res['message']}```")

    @commands.command()
    async def base64encode(self, ctx, *, str):
        encoded = base64.b64encode(str.encode()).decode()
        await ctx.reply(f"Here Is Your Encoded String: ```{encoded}```")

    @commands.command()
    async def base64decode(self, ctx, *, str):
        decoded = base64.b64decode(str.encode()).decode()
        await ctx.reply(f"Here Is Your Decoded String: ```{decoded}```")

    @commands.command()
    async def ascii(self, ctx, font: discord.Optional[str], *, text=None):
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

    # Taken From https://github.com/KxleLmao/DiscordSelfbot
    @commands.command()
    async def hidetext(self, ctx, displayText=None, hiddenText=None):
        await ctx.message.delete()
        if displayText is None and hiddenText is None:
            await ctx.send(f'[Error]: Invalid input!')
            return
        await ctx.send(displayText + ('||\u200b||' * 200) + hiddenText)

    # Taken From https://github.com/KxleLmao/DiscordSelfbot
    @commands.command(name="1337")
    async def _1337(self, ctx, *, text=None):
        await ctx.message.delete()
        if text is None:
            await ctx.send(f'[Error]: Invalid input!')
            return
        text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
            .replace('E', '3').replace('i', '!').replace('I', '!') \
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
        await ctx.send(f'{text}')

    # Taken From https://github.com/KxleLmao/DiscordSelfbot
    @commands.command()
    async def nitro(self, ctx):
        await ctx.reply(
            f'Here Is You Generated Nitro Code: \nhttps://discord.gift/{"".join(random.choices(string.ascii_letters + string.digits, k=16))}')


async def setup(bot):
    await bot.add_cog(Text(bot))
