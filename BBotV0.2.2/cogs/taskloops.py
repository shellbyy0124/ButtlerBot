import discord
import asyncio
import random
import datetime
import json
import calendar

from discord.ext import commands, tasks
from discord.ext.commands import Cog
from os import error

from discord.raw_models import RawBulkMessageDeleteEvent

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data=json.load(f)

information = data["channels"]["information"]


class TaskLoops(commands.Cog):

    def __init__(self, bot):

        self.bot=bot
        self.changepresence.start()
        self.automatedmessage.start()

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
        

    @tasks.loop(seconds = 300)
    async def automatedmessage(self):
        """Will send a message every 300 seconds"""
        sleeper=300
        color=random.randint(0, 0xFFFFFF)
        time=datetime.datetime.utcnow()
        bot=self.bot.user.avatar_url
        this = "This is an automated message."

        channel_one = self.bot.get_channel(information)

        embed1 = discord.Embed(color=color, timestamp=time, title="If you find any problems, or bugs, with the bots in this discord, Please use `>bbug` to send a report to the dev team!", inline=False)
        embed1.set_thumbnail(url=bot)
        embed1.set_footer(text=this)
        await channel_one.send(embed=embed1)
        await asyncio.sleep(300)

        embed2 = discord.Embed(color=color, timestamp=time, title="fill in info", description="fill in info", inline=False)
        embed2.set_thumbnail(url=bot)
        embed2.set_footer(text=this)
        await channel_one.send(embed=embed2)
        await asyncio.sleep(300)

        embed3 = discord.Embed(color=color, timestamp=time, title="fill in info", description="fill in infor", inline=False)
        embed3.set_thumbnail(url=bot)
        embed3.set_footer(text=this)
        await channel_one.send(embed=embed2)
        await asyncio.sleep(300)
        
def setup(bot):
    bot.add_cog(TaskLoops(bot))