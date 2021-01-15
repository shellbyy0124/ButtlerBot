import discord
import asyncio
import random
import datetime
import json

from discord.ext import commands, tasks
from discord.ext.commands import Cog

from discord.raw_models import RawBulkMessageDeleteEvent

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data=json.load(f)

general = data["channels"]["general"]
bot_spam = data["channels"]["bot_spam"]
staff_commands = data["channels"]["staff_commands"]


class TaskLoops(commands.Cog):

    def __init__(self, bot):

        self.bot=bot
        self.changepresence.start()

    @tasks.loop(seconds=10)
    async def changepresence(self):
        """Will loop every 60 seconds and change the bots presence"""
        
        await self.bot.change_presence(activity=discord.Game(name='if you cant remember, type >bhelp!'))
        await self.bot.change_presence(activity=discord.Game(name='Member count: TBD'))
        await self.bot.change_presence(activity=discord.Game(name='Released: 12/02/2020 By: Mekasu and Kastien'))
        await self.bot.change_presence(activity=discord.Game(name='Team Members: Mekasu, Kastien-Dev'))
        await self.bot.change_presence(activity=discord.Game(name='Type buttlerprefix to get the bots prefix!'))
        await self.bot.change_presence(activity=discord.Game(name='Accepting Staff Applications'))
                    
def setup(bot):
    bot.add_cog(TaskLoops(bot))