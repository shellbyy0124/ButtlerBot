import discord
import random

from discord.ext import commands
from discord.ext.commands import Cog

class OwnerCommands(commands.Cog):

    def __init__(self, bot):

        self.bot=bot


def setup(bot):
    bot.add_cog(OwnerCommands(bot))