import discord
from discord.ext import commands
from colorama import Fore


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener(name="on_ready")
    async def on_ready(self):
        print(
            f"""Welcome, {Fore.LIGHTRED_EX}{self.bot.user.name}{Fore.RESET}
Info:
    Username: {self.bot.user.name}
    Display Name: {self.bot.user.display_name}
    ID: {self.bot.user.id}
    Discriminator: {self.bot.user.discriminator}""")


async def setup(bot):
    await bot.add_cog(Events(bot))
