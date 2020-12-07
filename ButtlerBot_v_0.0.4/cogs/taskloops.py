import discord
import asyncio

from discord.ext import commands, tasks
from discord.ext.commands import Cog
from pytz import country_names 

class TaskLoops(commands.Cog):

    def __init__(self, bot):

        self.bot=bot

#* not changing presence

    @tasks.loop(seconds=10)
    async def changepresence(self, ctx):

        mem = []

        for m in ctx.guild.members:
            if not m.bot:
                mem.append(m)
                if count in range(len(int(mem))) > 0:
                    
                    """Will loop every 60 seconds and change the bots presence"""
                    await self.bot.change_presence(activity=discord.Game(name='if you cant remember, type /help!'))
                    await asyncio.sleep(10)
                    await self.bot.change_presence(activity=discord.Game(name=f'Member count: {count}'))
                    await asyncio.sleep(10)
                    await self.bot.change_presence(activity=discord.Game(name='Released: 12/02/2020 By: Shellbyy'))
                    await asyncio.sleep(10)
                    await self.bot.change_precense(activity=discord.Game(name='Team Members: Kastien-Dev, KortaPo'))
                    await asyncio.sleep(10)

def setup(bot):
    bot.add_cog(TaskLoops(bot))