import discord
from discord.ext import commands
from colorama import Fore
import base64
from art import *
import random
import string

class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



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
    async def hide(self, ctx, displayText=None, hiddenText=None):
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
        await ctx.reply(f'Here Is You Generated Nitro Code: \nhttps://discord.gift/{"".join(random.choices(string.ascii_letters + string.digits, k=16))}')

async def setup(bot):
    await bot.add_cog(Text(bot))
