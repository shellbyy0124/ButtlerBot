#* completely remove with open directory, and the BotOutput channel and replace all channels that say BotOutput with all the correct output channels which will be commented
#* next to it's print statement

# All blocks of code that are in comments
# are for future updates in the event that I can
# get them working. if you want to work on them as well
# and comment what you did so that I can go back and write down
# my notes, then please do that :) -mekasu

from datetime import date
import discord
import json
import random
import os
import asyncio
import datetime
import time

from os import error
from discord import member
from discord import role
from discord.ext import commands
from discord.ext.commands import cog
from discord.ext import tasks

with open('/home/shellbyy/Desktop/repofolder/Mekasu/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

TOKEN = data["BUTLER_TOKEN"]
STDOUT = data["STDOUT"]
command_prefix = data["command_prefix"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=command_prefix, intents=intents, nickname_command=None)

#* works
@bot.event
async def on_ready():
    channel = bot.get_channel(STDOUT)
    await channel.send(f'{bot.user.name} is online')

bot.load_extension("cogs.generalcommands")

bot.run(TOKEN)