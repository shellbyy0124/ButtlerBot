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
        await self.bot.wait_until_ready()
        await self.bot.change_presence(activity=discord.Game(name='if you cant remember, type >bhelp!'))
        await asyncio.sleep(10)
        await self.bot.change_presence(activity=discord.Game(name=f'Member count: TBD'))
        await asyncio.sleep(10)
        await self.bot.change_presence(activity=discord.Game(name='Released: 12/02/2020 By: Shellbyy'))
        await asyncio.sleep(10)
        await self.bot.change_presence(activity=discord.Game(name='Team Members: Mekasu, Kastien-Dev, KortaPo'))
        await asyncio.sleep(10)
        await self.bot.change_presence(activity=discord.Game(name='buttlerprefix will tell you the bots prefix!'))
        await asyncio.sleep(10)

def setup(bot):
    print('Task Loops cog has loaded...')
    bot.add_cog(TaskLoops(bot))