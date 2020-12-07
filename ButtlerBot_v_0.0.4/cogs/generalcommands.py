import discord
import json
import os
import datetime
import time
import random
import DiscordUtils

from os import error
from discord import member
from discord import embeds
from discord.ext import commands
from discord.ext.commands import cog

with open('/home/shellbyy/Desktop/repofolder/Mekasu/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
BOTOUTPUT = data["BOTOUTPUT"]

class GeneralCommands(commands.Cog):

    
    colors = [discord.Colour.teal(), discord.Colour.dark_teal(), discord.Colour.green(), discord.Colour.dark_green(), discord.Colour.blue(), 
              discord.Colour.dark_blue(), discord.Colour.purple(), discord.Colour.dark_purple(), discord.Colour.magenta(), discord.Colour.dark_magenta(), 
              discord.Colour.gold(), discord.Colour.orange(), discord.Colour.dark_orange(), discord.Colour.red(), discord.Colour.dark_red(),
              discord.Colour.lighter_grey(), discord.Colour.lighter_gray(), discord.Colour.dark_grey(), discord.Colour.dark_gray(), discord.Colour.light_grey(),
              discord.Colour.light_gray(), discord.Colour.darker_grey(), discord.Colour.darker_gray(), 
              discord.Colour.blurple(),
              discord.Colour.greyple(),
              discord.Colour.dark_theme()]

    color = random.choice(colors)
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['buttlerteamsubmit'])
    async def submitteamcode(self, ctx, *, message):
        submitembed1 = discord.Embed(color=self.color, title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted Code**: {message}", inline=False)
        submitembed1.set_thumbnail(url=ctx.author.avatar_url)
        channel = self.bot.get_channel(BOTOUTPUT)
        await channel.send(embed=submitembed1)
        
    @commands.command(aliases=['buttlerdiscordsubmit'])
    async def submitdiscordsuggestions(self, ctx, *, message):
        submitembed2 = discord.Embed(color=self.color, title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted A Suggestion For The Discord:** {message}", inline=False)
        submitembed2.set_thumbnail(url=ctx.author.avatar_url)
        channel=self.bot.get_channel(BOTOUTPUT)
        await channel.send(embed=submitembed2)

    @commands.command(aliases=['buttlerbotsubmit'])
    async def submitbotsuggestions(self, ctx, *, message):
        submitembed3 = discord.Embed(color=self.color, title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted A Suggestion For Bots:** {message}", inline=False)
        submitembed3.set_thumbnail(url=ctx.author.avatar_url)
        channel = self.bot.get_channel(BOTOUTPUT)
        await channel.send(embed=submitembed3)

    @commands.command(aliases=['buttlerpaste'])
    async def paste(self, ctx):
        paste1 = discord.Embed(color=self.color).add_field(name=f"**When Posting Code In {ctx.guild.name}!**",
                                                                value=f"Please use [Pastebin](https://pastebin.com/), [hastebin for Python](https://paste.pythondiscord.com/), or [mystb.in](https://mystb.in/)")
        await ctx.send(embed=paste1)


    @commands.command(aliases=['buttlerbotlist'])
    async def bbotlist(self, ctx):

        bots = []

        for m in ctx.guild.members:
            if m.bot:

                bots.append(m.name)

        botlist = discord.Embed(color=discord.Colour.blurple(), title="ButtlerBot's Companions:", description=f'{", ".join(bots)}')
        botlist.set_thumbnail(url=self.bot.user.avatar_url)
        botlist.timestamp = datetime.datetime.now()
        await ctx.send(embed=botlist)

    @commands.command(aliases=['buttlerstaffapp'])
    async def staffapp(self, ctx):
        await ctx.send(f"Unfortunately at this time, {ctx.guild.name} is not accepting applications for staff members. Please check #announcements for when applications will open back up")


    @commands.command(asliases=['buttlerbotupdates'])
    async def botupdates(self, ctx):

        await ctx.send("Hobo :panda_face:")


    @commands.command(aliases=['buttlerproject'])
    async def project(self, ctx):

        await ctx.send("Hobo :panda_face:")


    @commands.command(aliases=['buttlerhelplanguage'])
    async def helplanguage(self, ctx):

        await ctx.send("Hobo :panda_face:")

    @commands.command(aliases=['buttlerping'])
    async def ping(self, ctx):

        await ctx.send('Pong! _takes a deep breath_ PHEW! That took: {0}'.format(round(self.bot.latency, 1)))



def setup(bot):
    bot.add_cog(GeneralCommands(bot))