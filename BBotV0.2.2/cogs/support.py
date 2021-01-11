import discord
import json
import random
import os
import datetime

from os import error
from discord.ext import commands
from discord.ext.commands import Cog 

class Support(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command()
    async def bsupport(self, ctx):

        color = random.randint(0, 0xFFFFFF)
        time = datetime.datetime.utcnow()

        category = discord.utils.get(ctx.guild.categories, name='Save_Us')
        channel = discord.utils.get(ctx.guild.text_channels, name=ctx.author.name, category=category)

        embed1 = discord.Embed(color=discord.Colour.blue(), title=f"Welcome To Your Help Channel, {ctx.author.name}", description=f"Please type a brief description, and your code your having problems with and someone will be with you soon :)")
        msg = await channel.send(embed=embed1)
        ans = await self.bot.wait_for('message')

        if all(x.isprintable() for x in ans.content):
            embed2 = discord.embed(color=color, timestamp=time, title=f"{ctx.author.name}", description=f"{ans.content}")
            await msg.edit(embed=embed2)
            await msg.pin()
        

    @commands.command()
    async def bclose(ctx):
        if ctx.channel.category.name == 'Occupied_Support_Channels':
            await ctx.channel.delete()
            

        
        
def setup(bot):
    bot.add_cog(Support(bot))