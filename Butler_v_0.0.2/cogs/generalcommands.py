from re import L
import DiscordUtils as DiscordUtils
import discord
import json
import aiohttp
import random
import os

from os import error
from discord import member
from discord.ext import commands
from discord.ext.commands import cog
from discord.utils import get
from isort import logo

with open('/home/shellbyy/Desktop/repofolder/Mekasu/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

TOKEN = data["TOKEN"]
STDOUT = data["STDOUT"]
command_prefix = data["command_prefix"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=command_prefix, intents=intents, nickname_command=None)


class GeneralCommands(cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="submitteamcode")
    async def submitting(self, ctx, *, message):
        submitembed1 = discord.Embed(colour=discord.Color.green(), title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted Code**: {message}", inline=False)
        submitembed1.set_thumbnail(url=ctx.author.avatar_url)
        channel = bot.get_channel(STDOUT)
        await channel.send(embed=submitembed1)
        
    @commands.command(name="submitdiscordsuggestion")
    async def submitting2(self, ctx, *, message):
        submitembed2 = discord.Embed(colour=discord.Color.blue(), title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted A Suggestion For The Discord:** {message}", inline=False)
        submitembed2.set_thumbnail(url=ctx.author.avatar_url)
        channel=bot.get_channel(STDOUT)
        await channel.send(embed=submitembed2)

    @commands.command(name="submitbotsuggestion")
    async def submitting3(self, ctx, *, message):
        submitembed3 = discord.Embed(colour=discord.Color.orange(), title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted A Suggestion For Bots:** {message}", inline=False)
        submitembed3.set_thumbnail(url=ctx.author.avatar_url)
        channel = bot.get_channel(STDOUT)
        await channel.send(embed=submitembed3)

    @commands.command(name="buttlerpaste")
    async def pasting(self, ctx):
        paste1 = discord.Embed(color=ctx.author.color).add_field(name=f"**When Posting Code In {ctx.guild.name}!**",
                                                                value=f"Please use [Pastebin](https://pastebin.com/), or [hastebin for Python](https://paste.pythondiscord.com/)")
        await ctx.send(embed=paste1)

    @commands.command(name='buttlerbotlist')
    async def botlist(self, ctx=None):
        role = discord.utils.get(ctx.guild.roles, name="Bots")
        await ctx.send(", ".join(member.mention for member in role.members if member.bot))

    @commands.command(name="buttlerstaffapp")
    async def staffapplication(self, ctx):
        await ctx.send(f"Unfortunately at this time, {ctx.guild.name} is not accepting applications for staff members. Please check #announcements for when applications will open back up")


def setup(bot):
    bot.add_cog(GeneralCommands(bot))