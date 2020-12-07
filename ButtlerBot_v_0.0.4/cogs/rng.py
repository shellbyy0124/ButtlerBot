import random
import discord

from discord.ext import commands
from discord.ext.commands import Cog
# test

class RandomNumberGenerator(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.Cog.listener()
    async def randomNumber(self):

        confirmation_number = []

        random1 = random.randint(0, 999999)
        confirmation_number.append(random1)

def setup(bot):
    bot.add_cog(RandomNumberGenerator(bot))