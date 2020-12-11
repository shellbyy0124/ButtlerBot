import discord
import json
import os
import datetime
import asyncio
import random
import DiscordUtils

from os import error
from discord import member
from discord import embeds
from discord.ext import commands
from discord.ext.commands import cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
BOTOUTPUT = data["BOTOUTPUT"]
kastien = data["kastien"]
mekasu = data["mekasu"]
team_code_submissions = data["team_code_submissions"]
discord_suggestions = data["discord_suggestions"]
bot_suggestions = data["bot_suggestions"]
bot_spam = data["bot_spam"]
suggestions = data["suggestions"]

class GeneralCommands(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['btsubmit'])
    async def submitteamcode(self, ctx, *, message):
        submitembed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted Code**: {message}", inline=False)
        submitembed1.set_thumbnail(url=ctx.author.avatar_url)
        channel = self.bot.get_channel(team_code_submissions)
        await channel.send(embed=submitembed1)
        
    @commands.command(aliases=['bdsubmit'])
    async def submitdiscordsuggestions(self, ctx, *, message):
        submitembed2 = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted A Suggestion For The Discord:** {message}", inline=False)
        submitembed2.set_thumbnail(url=ctx.author.avatar_url)
        channel=self.bot.get_channel(discord_suggestions)
        await channel.send(embed=submitembed2)

    @commands.command(aliases=['bbsubmit'])
    async def submitbotsuggestions(self, ctx, *, message):
        submitembed3 = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted A Suggestion For Bots:** {message}", inline=False)
        submitembed3.set_thumbnail(url=ctx.author.avatar_url)
        channel = self.bot.get_channel(bot_suggestions)
        await channel.send(embed=submitembed3)

    @commands.command(aliases=['bpaste'])
    async def paste(self, ctx):

        paste1 = discord.Embed(color=random.randint(0, 0xFFFFFF)).add_field(name=f"**When Posting Code In {ctx.guild.name}!**",
                                                                value=f"Please use [Pastebin](https://pastebin.com/), [hastebin for Python](https://paste.pythondiscord.com/), or [mystb.in](https://mystb.in/)")
        msg = await ctx.send(embed=paste1)
        await asyncio.sleep(10)
        await msg.delete()


    @commands.command(aliases=['bblist'])
    async def bbotlist(self, ctx):

        bots = []
        for m in ctx.guild.members:
            if m.bot:
                bots.append(m.name)
        botlist = discord.Embed(color=random.randint(0, 0xFFFFFF), title="ButtlerBot's Companions:", description=f'{", ".join(bots)}')
        botlist.set_thumbnail(url=self.bot.user.avatar_url)
        botlist.timestamp = datetime.datetime.now()
        msg = await ctx.send(embed=botlist)
        await asyncio.sleep(10)
        await msg.delete()


    @commands.command(aliases=['bbupdates'])
    async def botupdates(self, ctx):

        await ctx.send("Hobo :panda_face:")


    @commands.command(aliases=['bproject'])
    async def project(self, ctx):

        await ctx.send("Hobo :panda_face:")


    @commands.command(aliases=['bhlang'])
    async def helplanguage(self, ctx):

        await ctx.send("Hobo :panda_face:")

    @commands.command(aliases=['bping'])
    async def ping(self, ctx):

        await ctx.send('Pong! _takes a deep breath_ PHEW! That took: {0}'.format(round(self.bot.latency, 1)))


    @commands.command(aliases=['binvite'])
    async def invitation(self, ctx):
        
        inv = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Inviting Your Friends:", description=f"Any and Everyone of ages 13+ are allowed to join our discord. Please do not create your own invite link, as you can use this one https://discord.gg/DEzK4vStfC")
        inv.set_thumbnail(url=self.bot.user.avatar_url)
        inv.set_footer(text=datetime.datetime.now())
        msg = await ctx.send(embed=inv)
        await asyncio.sleep(30)
        await msg.delete()

    @commands.command(aliases=['bsuggest'])
    async def suggestions(self, ctx, message):

        member = ctx.author.name
        sug = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp = datetime.datetime.now(), title=f"Suggestion By: {member}", description=f"{message}")
        channel = self.bot.get_channel(suggestions)
        await channel.send(embed=sug)

    @commands.command(aliases=['bbadlist'])
    async def badlistsuggestion(self, ctx, message):

        member = ctx.author.name
        bls = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Bad List Suggestion From {member}", description=f"{message.content}")
        channel = self.bot.get_channel(suggestions)
        await channel.send(embed=bls)


    


def setup(bot):
    bot.add_cog(GeneralCommands(bot))