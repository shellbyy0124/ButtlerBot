import discord
import random
import datetime

from discord.ext import commands
from discord.ext.commands import Cog 

class HiddenCommands(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.color = random.randint(0, 0xFFFFFF)
        self.time = datetime.datetime.utcnow()
        self.url = self.bot.user.avatar_url

    @commands.command()
    async def owneronlycommands(self, ctx):
        
        embed1 = discord.Embed(color=self.color, timestamp=self.time, title="Buttler Info", description="Displays the welcome embeds for those who we are showing the bot off to", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 1/")

def setup(bot):
    bot.add_cog(HiddenCommands(bot))