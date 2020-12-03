import DiscordUtils as DiscordUtils
import discord
import json
import aiohttp
import random
import os
import asyncio
import datetime
import time

from datetime import date
from os import error
from discord import member
from discord import role
from discord.ext import commands
from discord.ext.commands import cog
from discord.ext import tasks

with open('/home/shellbyy/Desktop/repofolder/Mekasu/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

TOKEN = data["BUTLER_TOKEN"]
STDOUT = data["Bot_Output_Testing_Channel"]
command_prefix = data["command_prefix"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=command_prefix, intents=intents, nickname_command=None)

class Greetings(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    #* works
    @commands.cog.listener
    async def on_member_join(self, member:discord.Member):
        await self.STDOUT.send(f"Hi,and Welcome! I am {bot.user.name}, and I'll be your guide today! Let's hope on over to the #verification channel, and type `/buttlerrules`.")

 
def setup(bot):
    bot.add_cog(Greetings(bot))