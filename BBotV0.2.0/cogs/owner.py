import datetime
import discord
import random
import json

from discord.ext import commands
from discord.ext.commands import Cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

mekasu = data["mekasu"]
kastien = data["kastien"]
staff_commands = data["staff_commands"]

class OwnerCommands(commands.Cog):

    def __init__(self, bot):

        self.bot=bot

    @commands.command(aliases=['mekasu'])
    @commands.has_any_role('Owner')
    async def ownerhelpmenu(self, ctx):

        owner1 = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Welcome Mistress {self.bot.get_user(mekasu).name}. How may I assist you today?")
        owner1.add_field(name="Are you wanting to display information about me?", value="if so then please use `>binfo`")
        owner1.add_field(name="__", value="__")
        owner1.timestamp = datetime.datetime.utcnow()
        owner1.set_thumbnail(url=self.bot.get_user(mekasu))

        channel = self.bot.get_channel(staff_commands)
        await channel.send(embed=owner1)


    @commands.command(aliases=['kastien'])
    @commands.has_role('Head Dev')
    async def help2(self, ctx):

        owner2 = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Welcome Mister {self.bot.get_user(kastien).name}. How may I assist you today?")
        owner2.add_field(name="Are you wanting to display information about me?", value="if so then please use `>binfo`")
        owner2.add_field(name="__", value="__")
        owner2.timestamp = datetime.datetime.utcnow()
        owner2.set_thumbnail(url=self.bot.get_user(kastien))

        channel = self.bot.get_channel(staff_commands)
        await channel.send(embed=owner2)

        
def setup(bot):
    print('Owner cog has loaded...')
    bot.add_cog(OwnerCommands(bot))