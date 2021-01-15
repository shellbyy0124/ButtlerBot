import discord
import json
import random
import os

from os import error
from discord.ext import commands
from discord.ext.commands import Cog 

with open('/home/kastien-dev/Desktop/Discord Bots/ButtlerBot/BBotV0.2.0/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)




class Support(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command()
    async def bsupport(self, ctx):
        names = ['pikachu', 'bulbasaur', 'meowth', 'squirtle', 'togapi']
        name = random.choice(names)
        category = discord.utils.get(ctx.guild.categories, name='Occupied_Support_Channels')
        channels = discord.utils.get(ctx.guild.text_channels, name=name)
        while channels in category is True:    
            if name is not None:
                category = discord.utils.get(ctx.guild.categories, name='Occupied_Support_Channels')
                for channel in category.text_channels:
                    if channel.name == name:
                        Support()                    
                    else:
                        channel = await ctx.guild.create_text_channel(name, overwrites=None, category=category)
                        embed1 = discord.Embed(color=discord.Colour.blue(), title=f"Welcome To Your Help Channel, {ctx.author}", description=f"Please type a brief description, and your code your having problems with and someone will be with you soon :)")
                        await channel.send(embed=embed1)

    @commands.command()
    async def bclose(ctx):
        if ctx.channel.category.name == 'Occupied_Support_Channels':
            await ctx.channel.delete()
            

        
        
def setup(bot):
    bot.add_cog(Support(bot))