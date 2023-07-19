import discord
from discord.ext import commands
from colorama import Fore
import random


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
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

    # Taken From https://github.com/KxleLmao/DiscordSelfbot
    @commands.command()
    async def minesweeper(self, ctx, size: int = 5):
        await ctx.message.delete()
        global m_offets
        global m_numbers
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


async def setup(bot):
    await bot.add_cog(Games(bot))
