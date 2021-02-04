import discord
import asyncio

from discord.ext import commands, tasks
from discord.ext.commands import Cog 

class TaskLoops(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.changepresence.start()

    @tasks.loop(seconds=30)
    async def changepresence(self):

        list = ["If you can't remember, type >bhelp", "Released: 12/02/2020 By: Mekasu & Kastien", "Team Members: Mekasu, KataReborn, KortaPo", "Type bprefix to get the bots prefix", "Staff Applications = Open"]

        for item in list:
            await self.bot.change_presence(activity=discord.Game(name=list))
            await asyncio.sleep(30)

def setup(bot):
    bot.add_cog(TaskLoops(bot))