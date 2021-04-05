import discord
import random
import datetime
import json
import DiscordUtils
import asyncio

from discord.ext import commands
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

kastien = data["kastien"]
shellbyy = data["shellbyy"]
mekasu = data["mekasu"]




class FAQs(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
    
    @commands.command(aliases=['bfaqs'])
    async def faq(self, ctx):

        faq1 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Frequently Asked Questions:", inline=False)
        faq1.add_field(name="\u200b", value="In the following pages you will find the most frequently asked questions. If you know of anymore, then please submit them under `>bdsubmit`", inline=False)
        faq1.set_thumbnail(url=self.bot.user.avatar_url)
        faq1.timestamp = datetime.datetime.utcnow()
        faq1.set_footer(text="Page 1/14")

        faq2 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp = datetime.datetime.utcnow(), title="Why are there no active bots in the server except buttler?", inline=False)
        faq2.add_field(name="\u200b", value=" We are in the very beginning stages of creating this community, and the bots that are used within it. Please bare with us as we are working diligently to get the community up and going as soon as possible :smile:", inline=False)
        faq2.set_thumbnail(url=self.bot.user.avatar_url)
        faq2.timestamp = datetime.datetime.utcnow()
        faq2.set_footer(text="Page 2/14")

        faq3 = discord.Embed(color=random.randint(0, 0xFFFFFF),timestamp=datetime.datetime.utcnow(),title="What do I do if I would like to submit an idea for a bot?", inline=False)
        faq3.add_field(name="\u200b", value=" Please submit your ideas for bots to be used within the discord community by typing `>bbsumbit <idea>` in the #bot_spam channel", inline=False)
        faq3.set_thumbnail(url=self.bot.user.avatar_url)
        faq3.timestamp = datetime.datetime.utcnow()
        faq3.set_footer(text="Page 3/14")

        faq4 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Where can I find beginner resources for learning Python?", inline=False)
        faq4.add_field(name="\u200b", value="Please venture over to the _**Resources**_ category where you can find different text channels containing various links for all types of information :smile:", inline=False)
        faq4.set_thumbnail(url=self.bot.user.avatar_url)
        faq4.timestamp = datetime.datetime.utcnow()
        faq4.set_footer(text="Page 4/14")

        faq5 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="How often cna I get a coding challenge?", inline=False)
        faq5.add_field(name="\u200b", value=f"Coding challenges are released once every 24 hours in their appropriate channels, however, at this time, this portion of {self.bot.user.name} is under construction.", inline=False)
        faq5.timestamp = datetime.datetime.utcnow()
        faq5.set_footer(text="Page 5/14")

        faq6 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="How does your ranking system work?")
        faq6.add_field(name="\u200b", value=f"{self.bot.get_user(kastien).name} is currently developing us an Exp bot to allow us to play various games, and {self.bot.get_user(mekasu).name} is currently developing the portion of {self.bot.user.name} to allows us to create profiles which various things on our profiles")
        faq6.set_thumbnail(url=self.bot.user.avatar_url)
        faq6.set_footer(text="Page 6/14")

        faq7 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="What do I do after I have posted a submission in the #future_bot_suggestions channel?")
        faq7.add_field(name="\u200b", value="Please be patient with us. We review each submission received, and if we decide on exploring it more in depth, we will set up a date and time with you to add your bot to a test server, and go over it from there")
        faq7.set_thumbnail(url=self.bot.user.avatar_url)
        faq7.timestamp = datetime.datetime.utcnow()
        faq7.set_footer(text="Page 7/14")

        faq8 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="So, I know there are bots made in javascript, but what would I use for discord bots made in python?")
        faq8.add_field(name="u200b", value="With bots made in the Python programming language, we use a library called discord.py, and you can find the [discord.py documentation here](https://discordpy.readthedocs.io/en/latest/)")
        faq8.set_thumbnail(url=self.bot.user.avatar_url)
        faq8.timestamp = datetime.datetime.utcnow()
        faq8.set_footer(text="Page 8/14")

        faq9 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="How do I need to post my code in the discord?")
        faq9.add_field(name="\u200b", value=f"to see how to paste your code within {ctx.guild.name}, type `>bpaste` 🙂")
        faq9.set_thumbnail(url=self.bot.user.avatar_url)
        faq9.timestamp = datetime.datetime.utcnow()
        faq9.set_footer(text="Page 9/14")

        faq10 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="What is a Database?")
        faq10.add_field(name="\u200b", value=" Is an organized collection of interrelated data stored in an elctronic format.")
        faq10.set_thumbnail(url=self.bot.user.avatar_url)
        faq10.timestamp = datetime.datetime.utcnow()
        faq10.set_footer(text="Page 10/14")

        faq11 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="10. What is `SQL`?")
        faq11.add_field(name="\u200b", value="SQL is a Structured Query Language which is a language designed for accessing and manipulating information from RDBMS.")
        faq11.set_thumbnail(url=self.bot.user.avatar_url)
        faq11.timestamp = datetime.datetime.utcnow()
        faq11.set_footer(text="Page 11/14")

        faq12 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="How Do I Install MySQL?")
        faq12.add_field(name="\u200b", value="Click [here for a guide](https://www.mysql.com/downloads/) to install MySQL and [here for a guide](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm) on installing SQLite")
        faq12.set_thumbnail(url=self.bot.user.avatar_url)
        faq12.timestamp = datetime.datetime.utcnow()
        faq12.set_footer(text="Page 12/14")

        faq13 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="How Do I Create A New User In MySQL?")
        faq13.add_field(name="\u200b", value="1) in terminal type `sudo mysql` this will turn into `mysql>` at the beginning of each line. 2) `CREATE USER 'username'@'host' IDENTIFIED BY 'password';` make sure to change `username`, `host`, and `password` to your perferred options. With `'host'` if you want to access the DB locally, change that to `'localhost'`")
        faq13.set_thumbnail(url=self.bot.user.avatar_url)
        faq13.timestamp = datetime.datetime.utcnow()
        faq13.set_footer(text="Page 13/14")

        faq14 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="How Do I Grant Privileges To A User In MySQL Database?")
        faq14.add_field(name="\u200b", value=") in terminal type `sudo -u <username> -p` it'll prompt for a password that you just created in #12. 2) `mysql> GRANT <privileges> ON <databasename>.table TO 'username'@'host' WITH GRANT OPTION;`")
        faq14.set_thumbnail(url=self.bot.user.avatar_url)
        faq14.timestamp = datetime.datetime.utcnow()
        faq14.set_footer(text="Page 14/14")

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('🔐', "lock")
        embeds = [faq1, faq2, faq3, faq4, faq5, faq6, faq7, faq8, faq9, faq10, faq11, faq12, faq13, faq14]
        msg = await paginator.run(embeds)
        await asyncio.sleep(300)
        await msg.delete()

def setup(bot):
    bot.add_cog(FAQs(bot))