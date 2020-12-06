import discord
import json
import random
import os
import asyncio
import datetime
import pytz

from os import error
from discord import member
from discord import role
from discord.ext import commands
from discord.ext.commands import cog
from discord.ext import tasks
from datetime import date
from pytz import timezone

with open('/home/shellbyy/Desktop/repofolder/Mekasu/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

TOKEN = data["BUTTLER_TOKEN"]
BOTOUTPUT = data["BOTOUTPUT"]
command_prefix = data["command_prefix"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=command_prefix, intents=intents, nickname_command=None)

@bot.event
async def on_ready():

    colors = [discord.Colour.teal(), discord.Colour.dark_teal(), discord.Colour.green(), discord.Colour.dark_green(),
              discord.Colour.blue(), discord.Colour.dark_blue(), discord.Colour.purple(), discord.Colour.dark_purple(),
              discord.Colour.magenta(), discord.Colour.dark_magenta(), discord.Colour.gold(), discord.Colour.orange(),
              discord.Colour.dark_orange(), discord.Colour.red(), discord.Colour.dark_red(), discord.Colour.lighter_grey(),
              discord.Colour.lighter_gray(), discord.Colour.dark_grey(), discord.Colour.dark_gray(), discord.Colour.light_grey(),
              discord.Colour.light_gray(), discord.Colour.darker_grey(), discord.Colour.darker_gray(), discord.Colour.blurple(),
              discord.Colour.greyple(), discord.Colour.dark_theme()]

    color = random.choice(colors)

    mekasu = bot.get_user(260009824945831936)
    kastien = bot.get_user(770311161559646299)

    onready = discord.Embed(color = color, title=f"{bot.user.name}").add_field(name=f"Welcome To {bot.user.name}", value=f"Hi! I'm {bot.user.name}, and I'll be your guide! If you need assistance, please type `>buttlerhelp` and I'll be right there!")
    onready.set_image(url=bot.user.avatar_url)
    onready.set_footer(text=f"Created By: {mekasu.name} and {kastien.name}")
    onready.timestamp = datetime.datetime.utcnow()

    channel = bot.get_channel(BOTOUTPUT)
    await channel.send(embed=onready)

bot.load_extension("cogs.onjoin")
bot.load_extension("cogs.botinformation")
bot.load_extension("cogs.generalcommands")
bot.load_extension("cogs.menu")
bot.load_extension("cogs.rules")
bot.load_extension("cogs.staff")
bot.load_extension("cogs.staffapplication")


bot.run(TOKEN)