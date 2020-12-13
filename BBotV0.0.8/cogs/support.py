import discord
import json
import random
import os

from os import error
from discord.ext import commands
from discord.ext.commands import Cog 
from discord.ext.commands.core import check

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)



class Support(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command()
    async def bsupport(self, ctx):

        member = ctx.author

        category = discord.utils.get(ctx.guild.categories, name='Occupied_Support_Channels')
        channel = await ctx.guild.create_text_channel(ctx.author.name, overwrites=None, category=category)

        first = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Welcome to your support channel, {ctx.author.display_name}", description=f"**__Please Follow the Template Below:__**\n```Operating System:\nText Editor:\nLanguage:\nWhat you're expecting to happen:\nWhat The Problem Is:\nLink To Code:\nLink To Error:```\n\nEach line is required when submitting a support ticket. If it doesn't apply to you then put N/A instead.\n\n**__:red_circle:ATTENTION:red_circle:__**\nYou will need a moderator or higher to close your support channel!!!")
        msg1 = await channel.send(embed=first)
        response = await self.bot.wait_for('message')
        await response.pin()

        if message.content.startswith("!>close"):
            await channel.delete()

        
        
def setup(bot):
    bot.add_cog(Support(bot))