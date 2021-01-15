import discord
import json
import random
import datetime
import sqlite3

from discord.ext import commands
from discord.ext.commands import Cog

with open('/home/kastien-dev/Desktop/Discord Bots/ButtlerBot/BBotV0.2.0/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

class DMUser(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
 
def setup(bot):
    bot.add_cog(DMUser(bot))