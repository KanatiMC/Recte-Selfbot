import discord
from discord.ext import commands
from colorama import Fore


class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def status(self, ctx, mode, *, name):
        mode = mode.lower()
        if "watching" in mode:
            watching = discord.Streaming(name=name, url="https://kanati.gay")
            await self.bot.change_presence(activity=watching)
        elif "playing" in mode:
            game = discord.Game(name=name)
            await self.bot.change_presence(activity=game)
        elif "custom" in mode:
            competing = discord.CustomActivity(name=name)
            await self.bot.change_presence(activity=competing)
        else:
            await ctx.send("Invalid mode. Please choose one of 'watching', 'playing', or 'custom'.")
            return
        await ctx.reply("Status Has Been Changed")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Current Ping: {round(self.bot.latency, 1)}')


async def setup(bot):
    await bot.add_cog(User(bot))
