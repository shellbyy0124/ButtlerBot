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
buttler_info = data["buttler_info"]

######### the colors in the buttlerinfo embed are for specific colors. please don't change them


class ButtlerInformation(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Team Leader')
    async def binfo(self, ctx):

        roles = []

        for r in ctx.guild.roles:
            if r.name == "Bots":
                pass
            elif not r.managed:
                roles.append(r.name)

        buttler = discord.Embed(color = discord.Colour.red(), title=f"{self.bot.user.name}:", description=f"Good Evening, Ladies and Gentlemen. My name is {self.bot.user.name} and I have been asked to escort you :smile:", inline=False)
        buttler.add_field(name=f"\u200b", value=f"My name is {self.bot.user.name}, and I have been created to become your virtual assistant. I was created by {self.bot.get_user(mekasu).display_name}, {self.bot.get_user(kastien).display_name}, and associates to become your virtual assistant within your community. Please go through this brief tutorial of who I am, what I can do, and how to access my information :smirk:", inline=False)
        buttler.add_field(name=f"Moderation:", value="I have different moderation commands, of which you can view by typing `>buttlerstaffhelp`. This will display a window of all commands available to staff members at this time.", inline=False)
        buttler.add_field(name=f"General Uses:", value='I also have commands that are available to your non-staff users. Type `>buttlerhelp` for those.', inline=False)
        buttler.add_field(name=f"Developments:", value=f"{self.bot.get_user(mekasu).name}, {self.bot.get_user(kastien).name}, and associates are currently working on developing so much more. They're goal is to incorporate Coding Challenges, Teams, and much more. Unfortunately at this time, I do not have any information on those delevopments, but you are always welcome to check the [github]() in the event that you're curious :)", inline=False)
        buttler.add_field(name=f"{ctx.guild.name}'s Staff Members':", value=f"**{roles[10]}:**\n{self.bot.get_user(mekasu).name}\n**{roles[9]}:**\n{self.bot.get_user(kastien).name}\n**{roles[8]}:**\n{self.bot.get_user(shellbyy).name}\n**{roles[7]}:**\n{self.bot.get_user(TheOnlyCarl).name}\n**{roles[6]}:**\n\n**{roles[5]}:**\n\n**{roles[3]}:**\n", inline=False)
        buttler.add_field(name="Creators:", value=f"**{self.bot.get_user(mekasu).name}**\n**Email:** __mekasurenae@outlook.com__\n**Discord:** __mekasu#7632__\n**Myspace:** __myspace.com/mekasu0124__\n\n\n**{self.bot.get_user(kastien).name}**\n**Email:** __katarebornmc@gmail.com__\n**Discord:** __Kastien-Dev#4697__")
        buttler.add_field(name=f"Disclaimer:", value=f"Please keep in mind that I am always in development. I am always due to change at any given time. In the event that I ever change, add, or remove a characteristic from myself, I will always let you know in the announcements channel, or by typing `>buttlerbotupdates`")
        buttler.set_thumbnail(url=self.bot.user.avatar_url)
        buttler.timestamp = datetime.datetime.utcnow()
        channel = self.bot.get_channel(buttler_info)
        await channel.send(embed=buttler)


def setup(bot):
    bot.add_cog(ButtlerInformation(bot))