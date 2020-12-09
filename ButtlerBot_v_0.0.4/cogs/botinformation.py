import json
import discord
import DiscordUtils
import asyncio
import datetime

from discord.ext import commands
from discord.ext.commands import Cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
mekasu = data["mekasu"]
kastien = data["kastien"]
shellbyy = data["shellbyy"]
TheOnlyCarl = data["TheOnlyCarl"]

######### the colors in the buttlerinfo embed are for specific colors. please don't change them


class ButtlerInformation(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def binfo(self, ctx):

        roles = []

        for r in ctx.guild.roles:
            if r.name == "Bots":
                pass
            elif not r.managed:
                roles.append(r.name)

        buttler = discord.Embed(color = discord.Colour.red(), title=f"{self.bot.user.name}:", description=f"Good Evening, Ladies and Gentlemen. My name is {self.bot.user.name} and I have been asked to escort you. Please click Next to continue :smile:", inline=False)
        buttler.set_image(url=self.bot.user.avatar_url)
        buttler.set_footer(text="Page 1/")
        buttler.timestamp = datetime.datetime.utcnow()
        
        buttler1 = discord.Embed(color = discord.Colour.orange(), title=f"", description=f"My name is {self.bot.user.name}, and I have been created to become your virtual assistant. I was created by {self.bot.get_user(mekasu).display_name}, {self.bot.get_user(kastien).display_name}, and associates to become your virtual assistant within your community. Please go through this brief tutorial of who I am, what I can do, and how to access my information :smirk:", inline=False)
        buttler1.set_image(url=self.bot.user.avatar_url)
        buttler1.set_footer(text="Page 2/")
        buttler1.timestamp = datetime.datetime.utcnow()
        
        buttler2 = discord.Embed(color = 0xFFFF00, title=f"Moderation:", description="I have different moderation commands, of which you can view by typing `>buttlerstaffhelp`. This will display a window of all commands available to staff members at this time.", inline=False)
        buttler2.set_image(url=self.bot.user.avatar_url)
        buttler2.set_footer(text="Page 3/")
        buttler2.timestamp = datetime.datetime.utcnow()
        
        buttler3 = discord.Embed(color=discord.Colour.green(), title=f"General Uses:", description='I also have commands that are available to your non-staff users. Type `>buttlerhelp` for those.', inline=False)
        buttler3.set_image(url=self.bot.user.avatar_url)
        buttler3.set_footer(text="Page 4/")
        buttler3.timestamp = datetime.datetime.utcnow()
        
        buttler4 = discord.Embed(color = discord.Colour.blue(), title=f"Developments:", description=f"{self.bot.get_user(mekasu).name}, {self.bot.get_user(kastien).name}, and associates are currently working on developing so much more. They're goal is to incorporate Coding Challenges, Teams, and much more. Unfortunately at this time, I do not have any information on those delevopments, but you are always welcome to check the [github]() in the event that you're curious :)", inline=False)
        buttler4.set_image(url=self.bot.user.avatar_url)
        buttler4.set_footer(text="Page 5/")
        buttler4.timestamp = datetime.datetime.utcnow()
        
        buttler5 = discord.Embed(color = 0x4B0082, title=f"{ctx.guild.name}'s Staff Members':", description=f"**{roles[4]}:**\n{self.bot.get_user(shellbyy).name}\n{self.bot.get_user(TheOnlyCarl).name}\n**{roles[5]}:**\n{self.bot.get_user(mekasu).name}\n{self.bot.get_user(kastien).name}", inline=False)
        buttler5.set_image(url=self.bot.user.avatar_url) 
        buttler5.set_footer(text="Page 6/")
        buttler5.timestamp = datetime.datetime.utcnow()
        
        buttler6 = discord.Embed(color = 0xEE82EE, title=f"Disclaimer:", description=f"Please keep in mind that I am always in development. I am always due to change at any given time. In the event that I ever change, add, or remove a characteristic from myself, I will always let you know in the announcements channel, or by typing `>buttlerbotupdates`")
        buttler6.set_image(url=self.bot.user.avatar_url)
        buttler6.set_footer(text="Page 7/")
        buttler6.timestamp = datetime.datetime.utcnow()
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('🔐', "lock")
        embeds = [buttler, buttler1, buttler2, buttler3, buttler4, buttler5, buttler6]
        await paginator.run(embeds)


def setup(bot):
    bot.add_cog(ButtlerInformation(bot))