import json
import discord
import DiscordUtils
import asyncio
import datetime

from discord.ext import commands
from discord.ext.commands import Cog

with open('/home/shellbyy/Desktop/repofolder/Mekasu/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

mekasu = data["mekasu"]
kastien = data["kastien"]




class ButtlerInformation(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def buttlerinfo(self, ctx):

        now = datetime.datetime.now()+datetime.timedelta(minutes=5)

        buttler = discord.Embed(color = discord.Colour.red(), title=f"{self.bot.user.name}:", description=f"Good Evening, Ladies and Gentlemen. My name is {self.bot.user.name} and I have been asked to escort you. If you would please click the right arrow at the bottom of this window to continue with your virtual introduction :smile:", inline=False)
        buttler.set_image(url=self.bot.user.avatar_url)
        buttler.set_footer(text="Page 1/")
        buttler.timestamp = datetime.datetime.utcnow()
        
        buttler1 = discord.Embed(color = discord.Colour.orange(), title=f"", description=f"My name is {self.bot.user.name}, and I have been created to become your virtual assistant. I was created by {self.bot.get_user(mekasu).display_name}, {self.bot.get_user(kastien).display_name}, and associates to become your virtual assistant within your community. Please go through this brief tutorial of who I am, what I can do, and how to access my information :smirk:", inline=False)
        buttler1.set_image(url=self.bot.user.avatar_url)
        buttler1.set_footer(text="Page 2/")
        buttler1.timestamp = datetime.datetime.utcnow()
        
        buttler2 = discord.Embed(color = discord.Colour.from_rgb(0, 255, 255), title=f"Moderation:", description=f"""`/buttlerstats` to get feedback such as """, inline=False)
        buttler2.set_image(url=self.bot.user.avatar_url)
        buttler2.set_footer(text="Page 3/")
        buttler2.timestamp = datetime.datetime.utcnow()
        
        buttler3 = discord.Embed(color=discord.Colour.green(), title=f"", desription=f"", inline=False)
        buttler3.set_image(url=self.bot.user.avatar_url)
        buttler3.set_footer(text="Page 4/")
        buttler3.timestamp = datetime.datetime.utcnow()
        
        buttler4 = discord.Embed(color = discord.Colour.blue(), title=f"", description="", inline=False)
        buttler4.set_image(url=self.bot.user.avatar_url)
        buttler4.set_footer(text="Page 4/")
        buttler4.timestamp = datetime.datetime.utcnow()
        
        buttler5 = discord.Embed(color = 0x4B0082, title=f"", description="", inline=False)
        buttler5.set_image(url=self.bot.user.avatar_url) 
        buttler5.set_footer(text="Page 5/")
        buttler5.timestamp = datetime.datetime.utcnow()
        
        buttler6 = discord.Embed(color = 0xEE82EE, title=f"", description=f"")
        buttler6.set_image(url=self.bot.user.avatar_url)
        buttler6.set_footer(text="Page 6/")
        buttler6.timestamp = datetime.datetime.utcnow()
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('🔐', "lock")
        embeds = [buttler, buttler1, buttler2, buttler3, buttler4, buttler5]
        await paginator.run(embeds)


def setup(bot):
    bot.add_cog(ButtlerInformation(bot))