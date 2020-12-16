import discord
import asyncio

from discord.ext import commands, tasks
from discord.ext.commands import Cog

class TaskLoops(commands.Cog):

    def __init__(self, bot):

        self.bot=bot
        self.changepresence.start()

    @tasks.loop(seconds=10)
    async def changepresence(self):
        """Will loop every 60 seconds and change the bots presence"""
        sleeper = 10
        await self.bot.wait_until_ready()
        await self.bot.change_presence(activity=discord.Game(name='if you cant remember, type >bhelp!'))
        await asyncio.sleep(sleeper)
        await self.bot.change_presence(activity=discord.Game(name=f'Member count: TBD'))
        await asyncio.sleep(sleeper)
        await self.bot.change_presence(activity=discord.Game(name='Released: 12/02/2020 By: Mekasu and Kastien'))
        await asyncio.sleep(sleeper)
        await self.bot.change_presence(activity=discord.Game(name='Team Members: Mekasu, Kastien-Dev'))
        await asyncio.sleep(sleeper)
        await self.bot.change_presence(activity=discord.Game(name='Type buttlerprefix to get the bots prefix!'))
        await asyncio.sleep(sleeper)
        await self.bot.change_presence(activity=discord.Game(name='Accepting Staff Applications'))
        await asyncio.sleep(sleeper)
        
def setup(bot):
    bot.add_cog(TaskLoops(bot))