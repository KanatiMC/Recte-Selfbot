import discord
from discord.ext import commands
from colorama import Fore
import json



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        with open("config.json") as f:
            data = json.load(f)
            self.prefix = data['prefix']

    @commands.group(name="help")
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.reply("```Help Menu"
                            f"\n\n{self.prefix}help admin"
                            "\nShows Admin Commands"
                            f"\n\n{self.prefix}help games"
                            "\nShows Game Commands"
                            f"\n\n{self.prefix}help user"
                            "\nShows User Commands"
                            f"\n\n{self.prefix}help info"
                            "\nShows Info Commands"
                            f"\n\n{self.prefix}help text"
                            "\nShows Text Commands```")

    @help.command()
    async def admin(self, ctx):
        await ctx.reply("```Admin Help Menu"
                        f"\n\n{self.prefix}clone <guild1 ID> <guild2 ID>"
                        "Clones The Guild1 Server To Guild2```")

    @help.command(aliases=['games'])
    async def game(self, ctx):
        await ctx.reply("```Game Help Menu"
                        f"\n\n{self.prefix}minesweeper <size>"
                        "\nCreates A Minesweeper Game With The Chosen Size```")

    @help.command()
    async def user(self, ctx):
        await ctx.reply("```User Help Menu"
                        f"\n\n{self.prefix}status <mode> <name>"
                        "\nSets A Custom Status To The Bot"
                        f"\n\n{self.prefix}ping"
                        "\nGet's The Bot's Ping```")

    @help.command()
    async def info(self, ctx):
        await ctx.reply("```Info Help Menu"
                        f"\n\n{self.prefix}roleinfo <role>"
                        "\nSends Info On A Picked Role"
                        f"\n\n{self.prefix}chanelinfo <channel>(optional)"
                        "\nSends Info On The Channel, If There Is None Then It Sends Info On The Channel From This Message"
                        f"\n\n{self.prefix}guildinfo <guild>(optional)"
                        "\nSends Info Of The Guild, If There Is None Then It Sends Info On The Guild From This Message```")

    @help.command()
    async def text(self, ctx):
        await ctx.reply("```Text Help Menu"
                        f"\n\n{self.prefix}base64encode <string>"
                        "\nSends The String, But Encoded By Base64"
                        f"\n\n{self.prefix}base64decode <strings>"
                        "\nDecodes The String If It Was Decrypted With Base64"
                        f"\n\n{self.prefix}ascii <font>(optional) <text>"
                        "\nSends ASCII Art Of The Chosen Text With The Chosen Font"
                        f"\n\n{self.prefix}nitro"
                        "\nGenerates A Fake Nitro, With The Possibility Of Being Real"
                        f"\n\n{self.prefix}hide <displayText> <hiddenText>"
                        "\nSends A Message With <hiddenText> Being Hidden, But <displayText> Being Visible"
                        f"\n\n{self.prefix}1337 <text>"
                        "\nSends A Message With Super Hacker Text```")




async def setup(bot):
    await bot.add_cog(Help(bot))
