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

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
BOTOUTPUT = data["BOTOUTPUT"]
kastien = data["kastien"]
mekasu = data["mekasu"]

class GeneralCommands(commands.Cog):

    
    colors = random.randint(0, 0xFFFFFF)
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['btsubmit'])
    async def submitteamcode(self, ctx, *, message):
        submitembed1 = discord.Embed(color=self.color, title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted Code**: {message}", inline=False)
        submitembed1.set_thumbnail(url=ctx.author.avatar_url)
        channel = self.bot.get_channel(BOTOUTPUT)
        await channel.send(embed=submitembed1)
        
    @commands.command(aliases=['bdsubmit'])
    async def submitdiscordsuggestions(self, ctx, *, message):
        submitembed2 = discord.Embed(color=self.color, title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted A Suggestion For The Discord:** {message}", inline=False)
        submitembed2.set_thumbnail(url=ctx.author.avatar_url)
        channel=self.bot.get_channel(BOTOUTPUT)
        await channel.send(embed=submitembed2)

    @commands.command(aliases=['bbsubmit'])
    async def submitbotsuggestions(self, ctx, *, message):
        submitembed3 = discord.Embed(color=self.color, title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted A Suggestion For Bots:** {message}", inline=False)
        submitembed3.set_thumbnail(url=ctx.author.avatar_url)
        channel = self.bot.get_channel(BOTOUTPUT)
        await channel.send(embed=submitembed3)

    @commands.command(aliases=['bpaste'])
    async def paste(self, ctx):
        paste1 = discord.Embed(color=self.color).add_field(name=f"**When Posting Code In {ctx.guild.name}!**",
                                                                value=f"Please use [Pastebin](https://pastebin.com/), [hastebin for Python](https://paste.pythondiscord.com/), or [mystb.in](https://mystb.in/)")
        await ctx.send(embed=paste1)


    @commands.command(aliases=['bblist'])
    async def bbotlist(self, ctx):

        bots = []

        for m in ctx.guild.members:
            if m.bot:

                bots.append(m.name)

        botlist = discord.Embed(color=self.color, title="ButtlerBot's Companions:", description=f'{", ".join(bots)}')
        botlist.set_thumbnail(url=self.bot.user.avatar_url)
        botlist.timestamp = datetime.datetime.now()
        await ctx.send(embed=botlist)


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
        
        inv = discord.Embed(color=self.color, title=f"Inviting Your Friends:", description=f"Any and Everyone of ages 13+ are allowed to join our discord. Please do not create your own invite link, as you can use this one https://discord.gg/DEzK4vStfC")
        inv.set_image(url=self.bot.user.avatar_url)
        inv.set_footer(text=datetime.datetime.now())

        await ctx.send(embed=inv)

    @commands.command(aliases=['bsuggest'])
    async def suggestions(self, ctx, message):

        member = ctx.author.name

        sug = discord.Embed(color=self.color, timestamp = datetime.datetime.now(), title=f"Suggestion By: {member}", description=f"{message}")

        channel = self.bot.get_channel(BOTOUTPUT)
        await channel.send(embed=sug)

    @commands.command(aliases=['bbadlist'])
    async def badlistsuggestion(self, ctx, message):

        member = ctx.author.name

        bls = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Bad List Suggestion From {member}", description=f"{message}")

        channel = self.bot.get_channel(BOTOUTPUT)
        await channel.send(embed=bls)


    @commands.command(aliases=['bfaqs'])
    async def faq(self, ctx):

        faq1 = discord.Embed(color=self.color, title="Frequently Asked Questions:", inline=False)
        faq1.add_field(name="\u200b", value="In the following pages you will find the most frequently asked questions. If you know of anymore, then please submit them under `>bdsubmit", inline=False)
        faq1.set_thumbnail(url=self.bot.user.avatar_url)
        faq1.timestamp = datetime.datetime.utcnow()
        faq1.set_footer(text="Page 1/14")

        faq2 = discord.Embed(color=self.color, timestamp = datetime.datetime.utcnow(), title="Why are there no active bots in the server except buttler?", inline=False)
        faq2.add_field(name="\u200b", value=" We are in the very beginning stages of creating this community, and the bots that are used within it. Please bare with us as we are working diligently to get the community up and going as soon as possible :smile:", inline=False)
        faq2.set_thumbnail(url=self.bot.user.avatar_url)
        faq2.timestamp = datetime.datetime.utcnow()
        faq2.set_footer(text="Page 2/14")

        faq3 = discord.Embed(color=self.color,timestamp=datetime.datetime.utcnow(),title="What do I do if I would like to submit an idea for a bot?", inline=False)
        faq3.add_field(name="\u200b", value=" Please submit your ideas for bots to be used within the discord community by typing `>bbsumbit <idea>` in the #bot_spam channel", inline=False)
        faq3.set_thumbnail(url=self.bot.user.avatar_url)
        faq3.timestamp = datetime.datetime.utcnow()
        faq3.set_footer(text="Page 3/14")

        faq4 = discord.Embed(color=self.color, title="Where can I find beginner resources for learning Python?", inline=False)
        faq4.add_field(name="\u200b", value="Please venture over to the _**Resources**_ category where you can find different text channels containing various links for all types of information :smile:", inline=False)
        faq4.set_thumbnail(url=self.bot.user.avatar_url)
        faq4.timestamp = datetime.datetime.utcnow()
        faq4.set_footer(text="Page 4/14")

        faq5 = discord.Embed(color=self.color, title="How often cna I get a coding challenge?", inline=False)
        faq5.add_field(name="\u200b", value=f"Coding challenges are released once every 24 hours in their appropriate channels, however, at this time, this portion of {self.bot.user.name} is under construction.", inline=False)
        faq5.timestamp = datetime.datetime.utcnow()
        faq5.set_footer(text="Page 5/14")

        faq6 = discord.Embed(color=self.color, title="How does your ranking system work?")
        faq6.add_field(name="\u200b", value=f"{self.bot.get_user(kastien.name)} is currently developing us an Exp bot to allow us to play various games, and {self.bot.get_user(mekasu.name)} is currently developing the portion of {self.bot.user.name} to allows us to create profiles which various things on our profiles")
        faq6.set_thumbnail(url=self.bot.user.avatar_url)
        faq6.set_footer(text="Page 6/14")

        faq7 = discord.Embed(color=self.color, title="What do I do after I have posted a submission in the #future_bot_suggestions channel?")
        faq7.add_field(name="\u200b", value="Please be patient with us. We review each submission received, and if we decide on exploring it more in depth, we will set up a date and time with you to add your bot to a test server, and go over it from there")
        faq7.set_thumbnail(url=self.bot.user.avatar_url)
        faq7.timestamp = datetime.datetime.utcnow()
        faq7.set_footer(text="Page 7/14")

        faq8 = discord.Embed(color=self.color, title="So, I know there are bots made in javascript, but what would I use for discord bots made in python?")
        faq8.add_field(name="u200b", value="With bots made in the Python programming language, we use a library called discord.py, and you can find the [discord.py documentation here](https://discordpy.readthedocs.io/en/latest/)")
        faq8.set_thumbnail(url=self.bot.user.avatar_url)
        faq8.timestamp = datetime.datetime.utcnow()
        faq8.set_footer(text="Page 8/14")

        faq9 = discord.Embed(color=self.color, title="How do I need to post my code in the discord?")
        faq9.add_field(name="\u200b", value=f"to see how to paste your code within {ctx.guild.name}, type `>bpaste` 🙂")
        faq9.set_thumbnail(url=self.bot.user.avatar_url)
        faq9.timestamp = datetime.datetime.utcnow()
        faq9.set_footer(text="Page 9/14")

        faq10 = discord.Embed(color=self.color, title="What is a Database?")
        faq10.add_field(name="\u200b", value=" Is an organized collection of interrelated data stored in an elctronic format.")
        faq10.set_thumbnail(url=self.bot.user.avatar_url)
        faq10.timestamp = datetime.datetime.utcnow()
        faq10.set_footer(text="Page 10/14")

        faq11 = discord.Embed(color=self.color, title="10. What is `SQL`?")
        faq11.add_field(name="\u200b", value="SQL is a Structured Query Language which is a language designed for accessing and manipulating information from RDBMS.")
        faq11.set_thumbnail(url=self.bot.user.avatar_url)
        faq11.timestamp = datetime.datetime.utcnow()
        faq11.set_footer(text="Page 11/14")

        faq12 = discord.Embed(color=self.color, title="How Do I Install MySQL?")
        faq12.add_field(name="\u200b", value="Click [here for a guide](https://www.mysql.com/downloads/) to install MySQL and [here for a guide](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm) on installing SQLite")
        faq12.set_thumbnail(url=self.bot.user.avatar_url)
        faq12.timestamp = datetime.datetime.utcnow()
        faq12.set_footer(text="Page 12/14")

        faq13 = discord.Embed(color=self.color, title="How Do I Create A New User In MySQL?")
        faq13.add_field(name="\u200b", value="1) in terminal type `sudo mysql` this will turn into `mysql>` at the beginning of each line. 2) `CREATE USER 'username'@'host' IDENTIFIED BY 'password';` make sure to change `username`, `host`, and `password` to your perferred options. With `'host'` if you want to access the DB locally, change that to `'localhost'`")
        faq13.set_thumbnail(url=self.bot.user.avatar_url)
        faq13.timestamp = datetime.datetime.utcnow()
        faq13.set_footer(text="Page 13/14")


        faq14 = discord.Embed(color=self.color, title="How Do I Grant Privileges To A User In MySQL Database?")
        faq14.add_field(name="\u200b", value=") in terminal type `sudo -u <username> -p` it'll prompt for a password that you just created in #12. 2) `mysql> GRANT <privileges> ON <databasename>.table TO 'username'@'host' WITH GRANT OPTION;`")
        faq14.set_thumbnail(url=self.bot.user.avatar_url)
        faq14.timestamp = datetime.datetime.utcnow()
        faq14.set_footer(text="Page 14/14")

        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('🔐', "lock")
        embeds = [faq1, faq2, faq3, faq4, faq5, faq6, faq7, faq8, faq9, faq10, faq11, faq12, faq13, faq14]
        await paginator.run(embeds)



def setup(bot):
    bot.add_cog(GeneralCommands(bot))