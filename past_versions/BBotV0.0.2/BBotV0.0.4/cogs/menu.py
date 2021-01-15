import discord
import json
import aiohttp
import random
import os
import datetime
import DiscordUtils
import asyncio

from os import error
from discord import member
from discord.ext import commands
from discord.ext.commands import cog
from discord.utils import get
from isort import logo

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
BOTOUTPUT = data["BOTOUTPUT"]

class HelpCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["bhelp"])
    async def paginate(self, ctx):
        now = datetime.datetime.now()+datetime.timedelta(minutes=5)
        async with aiohttp.ClientSession() as session:
            async with session.get('https://rickandmortyapi.com/api/character') as resp:
                x = await resp.json()
                
        y2 = random.randint(0, 19)
        y3 = random.randint(0, 19)
        y4 = random.randint(0, 19)
        y5 = random.randint(0, 19)
        y6 = random.randint(0, 19)
        y7 = random.randint(0, 19)
        y8 = random.randint(0, 19)
        y9 = random.randint(0, 19)
        y10 = random.randint(0, 19)
        y11 = random.randint(0, 19)
        y12 = random.randint(0, 19)
        y13 = random.randint(0, 19)
        y14 = random.randint(0, 19)
        y15 = random.randint(0, 19)
        y16 = random.randint(0, 19)
        y17 = random.randint(0, 19)
        y18 = random.randint(0, 19)
        y19 = random.randint(0, 19)
        y20 = random.randint(0, 19)
        y21 = random.randint(0, 19)

        embed1 = discord.Embed(color=ctx.author.color).add_field(name=f"Hi! I'm {self.bot.user.name}, and I'm here to help!",
                                                                value="In the pages to follow are things that I am able to currently help you with, and a list of things that I am currently developing to better help you in the future! :smile: To get my help menu, type `/buttlerhelp`, and please enjoy these Rick and Morty meme's while you flip through the pages :heart:")
        embed1.set_image(url=self.bot.user.avatar_url)
        embed1.set_footer(text='Page 1/20')
        embed1.timestamp = datetime.datetime.now()
        embed2 = discord.Embed(color=ctx.author.color).add_field(name="Got Friends?",
                                                                value="Invite Them With `>binvite`")
        embed2.set_image(url=x["results"][y2]["image"])
        embed2.set_footer(text='Page 2/20')
        embed2.timestamp = datetime.datetime.now()
        embed3 = discord.Embed(color=ctx.author.color).add_field(name=f"Rules:",
                                                                value=f"Each member was sent a list of the rules when they joined {ctx.guild.name}, however, if the rules need to be referenced, please type `>brules` to receive a list of rules :smile:")
        embed3.set_image(url=x["results"][y3]["image"])
        embed3.set_footer(text='Page 3/20')
        embed3.timestamp = datetime.datetime.now()
        embed4 = discord.Embed(color=ctx.author.color).add_field(name=f"How To Present Your Code In This Discord:",
                                                                value=f"If you're unsure of how to paste code within {ctx.guild.name}, then type `>bpaste` to get the insider scoop :smile:")
        embed4.set_image(url=x["results"][y4]["image"])
        embed4.set_footer(text='Page 4/20')
        embed4.timestamp = datetime.datetime.now()
        embed5 = discord.Embed(color=ctx.author.color).add_field(name=f"For A List of FAQ's:",
                                                                value="Please Type `>bfaqs` to receive the Frequently Asked Questions, and their solutions :thinking:")
        embed5.set_image(url=x["results"][y5]["image"])
        embed5.set_footer(text='Page 5/20')
        embed5.timestamp = datetime.datetime.now()
        embed6 = discord.Embed(color=ctx.author.color).add_field(name=f"Staff Applications:",
                                                                value="If you would like to apply to become a staff member, please type `>bsapp` to receive the application within the #staff_applications channel")
        embed6.set_image(url=x["results"][y6]["image"])
        embed6.set_footer(text='Page 6/20')
        embed6.timestamp = datetime.datetime.now()
        embed7 = discord.Embed(color=ctx.author.color).add_field(name=f"Bot Updates",
                                                                value="For a list of the most recent bot updates, please type `>bbupdates` to get the link to our text channel for our updates that come out for our communities bots.")
        embed7.add_field(name="**ATTENTION**", value="`**THIS COMMAND IS CURRENTLY UNDER CONSTRUCTION, AND THUS WILL RETURN HOBO IF YOU USE IT**`")                                                            
        embed7.set_image(url=x["results"][y7]["image"])
        embed7.set_footer(text='Page 7/20')
        embed7.timestamp = datetime.datetime.now()
        embed8 = discord.Embed(color=ctx.author.color).add_field(name=f"List Of Bots In {ctx.guild.name}",
                                                                value="To see a list of the bots we have, please type `>bblist`")
        embed8.set_image(url=x["results"][y8]["image"])
        embed8.set_footer(text='Page 8/20')
        embed8.timestamp = datetime.datetime.now()
        embed9 = discord.Embed(color=ctx.author.color).add_field(name=f"Have words you could careless to see?:",
                                                                value="If you have a word, or a list of words, that you would like have added to the message filter, or would like to have a word removed, then please type `>bbadlist <message>`")
        embed9.add_field(name="**ATTENTION**", value="`**THIS COMMAND IS CURRENTLY UNDER CONSTRUCTION, AND THUS WILL RETURN HOBO IF YOU USE IT**`")
        embed9.set_image(url=x["results"][y9]["image"])
        embed9.set_footer(text='Page 9/20')
        embed9.timestamp = datetime.datetime.now()
        embed10 = discord.Embed(color=ctx.author.color).add_field(name=f"Need Help?",
                                                                value=f"Do you need help with your code? Then type `>bhlang` to get help with your code! Be sure to replace `<languange>` with the language of the code you're needing assistance with! **Be advised, this discord only provides support for Java, C#, Python, JavaScript, and HTML!**")
        embed10.add_field(name="**ATTENTION**", value="`**THIS COMMAND IS CURRENTLY UNDER CONSTRUCTION, AND THUS WILL RETURN HOBO IF YOU USE IT**`")
        embed10.set_image(url=x["results"][y10]["image"])
        embed10.set_footer(text='Page 10/20')
        embed10.timestamp = datetime.datetime.now()
        embed11 = discord.Embed(color=ctx.author.color).add_field(name="Resources:",
                                                                value=f"We have 2 categories dedicated to resources for all of our members. Please travel down to _Resources For Beginners_ and _Resources_ for more information!")
        embed11.set_image(url=x["results"][y11]["image"])
        embed11.set_footer(text='Page 11/20')
        embed11.timestamp = datetime.datetime.now()
        embed12 = discord.Embed(color=ctx.author.color).add_field(name='Coding Challenges:',
                                                                value=f"The coding challenges section of ButtlerBot is currently under construction.")
        embed12.set_image(url=x["results"][y12]["image"])
        embed12.set_footer(text="Page 12/20")
        embed12.timestamp = datetime.datetime.now()
        embed13 = discord.Embed(color=ctx.author.color).add_field(name=f"Need to have access to a To-Do list?",
                                                                value="Head on over to #to_do and use our ToDo Bot! \n\n\n**BE ADVISED! THIS PART OF BUTTLER IS UNDER CONSTRUCTION! FOR THE TIME BEING WE ARE USING TODO BOT! WE DO NOT OWN NOR DO WE HAVE A SUPPORT CHANNEL FOR THIS BOT! EVERYONE CAN SEE YOUR TODO LIST. NO ONE CAN ACCESS IT!**")
        embed13.set_image(url=x["results"][y13]["image"])
        embed13.set_footer(text="Page 13/20")
        embed13.timestamp = datetime.datetime.now()
        embed14 = discord.Embed(color=ctx.author.color).add_field(name=f"{self.bot.user.name} not responding?",
                                                                value="type `>bping` to get a pong!")
        embed14.set_image(url=x["results"][y15]["image"])
        embed14.set_footer(text="Page 14/20")
        embed14.timestamp = datetime.datetime.now()
        embed15 = discord.Embed(color=ctx.author.color).add_field(name=f"Nick Names!",
                                                                value="Type `/nick` to change your nickname! Please keep it community appropriate! If you don't, the staff will change it!")
        embed15.set_image(url=x["results"][y16]["image"])
        embed15.set_footer(text="Page 15/20")
        embed15.timestamp = datetime.datetime.now()
        embed16 = discord.Embed(color=ctx.author.color).add_field(name=f"**Submitting Your Code To A Team?**",
                                                                value="To submit your code to the team submissions channel, type `>btsubmit <link to your pastebin>`")
        embed16.set_image(url=x["results"][y17]["image"])
        embed16.set_footer(text="Page 16/20")
        embed16.timestamp = datetime.datetime.now()
        embed17 = discord.Embed(color=ctx.author.color).add_field(name=f"**Submitting A Discord Suggestion?**",
                                                                value=f"To submit your discord suggestion, type `>bdsubmit <your_suggestion>`")
        embed17.set_image(url=x["results"][y18]["image"])
        embed17.set_footer(text="Page 17/20")
        embed17.timestamp = datetime.datetime.now()
        embed18 = discord.Embed(color=ctx.author.color).add_field(name=f"**Submitting A Suggestion For A Future Bot?**",
                                                                value=f"Want to submit an idea for a future bot? type `>bbsubmit <your_suggestion>`")
        embed18.set_image(url=x["results"][y19]["image"])
        embed18.set_footer(text="Page 18/20")
        embed18.timestamp = datetime.datetime.now()
        embed19 = discord.Embed(color=ctx.author.color).add_field(name="**Don't know buttler's prefix?**", 
                                                                value="just simply type `bprefix`, and I'll let you know :smile:")
        embed19.set_image(url=x["results"][y20]["image"])
        embed19.set_footer(text="Page 19/20")
        embed19.timestamp = datetime.datetime.now()
        embed20 = discord.Embed(color=ctx.author.color).add_field(name=f"Disclaimer!",
                                                                value=f'This can/will be changed at any given time. If you are ever unsure of what commands are available to you, you can always type `/help` :smile: :clap:')
        embed20.set_image(url=x["results"][y21]["image"])
        embed20.set_footer(text="Page 20/20")     
        embed20.timestamp = datetime.datetime.now()      

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏮️', "first")
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('⏭️', "last")
        embeds = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19]
        await paginator.run(embeds)


    @commands.command(aliases=["buttlerstaffhelp"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def staffhelpmenu(self, ctx):

        adminembed1 = discord.Embed(color=ctx.author.color).add_field(name=f"Hi! I'm {self.bot.user.name} Staff Menu, and I'm here to help!",
                                                                value="In the pages to follow are things that I am able to currently help you with, and below that is a list of things that I am currently developing to better help you in the future! :smile: To get my help menu, type `/buttlerstaffhelp`")
        adminembed1.set_image(url=self.bot.user.avatar_url)
        adminembed1.set_footer(text='Page 1/20')
        adminembed1.timestamp = datetime.datetime.now()
        adminembed2 = discord.Embed(color=ctx.author.color).add_field(name="Server Statistics:",
                                                                value="Want to help us keep up with the server stats? Type /buttlerstats to get the pertinent info!")
        adminembed2.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed2.set_footer(text='Page 2/20')
        adminembed2.timestamp = datetime.datetime.now()
        adminembed3 = discord.Embed(color=ctx.author.color).add_field(name=f"User Inappropriate Nickname?",
                                                                value="Do you see a user with an inappropriate username? then type /buttlerchangenick <username_as_currently_shown> <actual_name> and the user will automatically be dm'd a message of their nickname being changed. Adding a reason for why will be coming in a future update!")
        adminembed3.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed3.set_footer(text='Page 3/20')
        adminembed3.timestamp = datetime.datetime.now()
        adminembed4 = discord.Embed(color=ctx.author.color).add_field(name=f"Purging Channels: `>buttlerpurge`",
                                                                value="Do Not Abuse This Ability! If you are deleting less than 20-ish messages, then right click and delete them individually. This command is only for if someone has hacked us, or spammed us! It will delete pinned messages if you delete it with the bot! Try not to use this command if you are not an admin or higher. If unsure of when to use it, please ask an admin or higher in the staff chat channel")
        adminembed4.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed4.set_footer(text='Page 4/20')
        adminembed4.timestamp = datetime.datetime.now()
        adminembed5 = discord.Embed(color=ctx.author.color).add_field(name=f"Who Is Who but a Who!",
                                                                value="Some have an incomprehensible nickname, and you want to know who they are, or need to change their nickname, then type /buttlerwhois <username> and get that information!")
        adminembed5.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed5.set_footer(text='Page 5/20')
        adminembed5.timestamp = datetime.datetime.now()
        adminembed6 = discord.Embed(color=ctx.author.color).add_field(name=f"A member being obnixious is the voice, or text channel?",
                                                                value="Type `/tempmute <member_name> <time_in_seconds> <reason>` to mute them").add_field(name="\u200b", value="**THIS COMMAND IS UNDER CONSTRUCTION AND WILL NOT WORK**")
        adminembed6.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed6.set_footer(text='Page 6/20')
        adminembed6.timestamp = datetime.datetime.now()
        adminembed7 = discord.Embed(color=ctx.author.color).add_field(name=f"Locking Channels:", value="It is only ok to lock a channel with `>buttlerlock` when we are being spammed, or a virus of some sort is in the server. Other than that, you can simply use the `>buttlerwarn` or `>butlertempmute` commands to take care of the problem.")
        adminembed7.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed7.set_footer(text='Page 7/20')
        adminembed7.timestamp = datetime.datetime.now()
        adminembed8 = discord.Embed(color=ctx.author.color).add_field(name="Unlocking Channels:", value="As stated previously with the locking channels, and the appropriatness of that command, unlocking channels (`>buttlerunlock`) are only to be done by the head admins or higher. We are the only ones with access to the files. We will let you know when it is safe!")
        adminembed8.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed8.set_footer(text="Page 8/20")
        adminembed8.timestamp = datetime.datetime.now()
        adminembed9 = discord.Embed(color=ctx.author.color).add_field(name="Need To Know Who's Here?", value="Use `>buttlerlistmembers` to get a list of members within the discord :smile:")
        adminembed9.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed9.set_footer(text="Page 9/20")
        adminembed9.timestamp = datetime.datetime.now()
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction('⏮️', "first")
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('⏭️', "last")
        adminembeds = [adminembed1, adminembed2, adminembed3, adminembed4, adminembed5, adminembed6, adminembed7, adminembed8, adminembed9]
        await paginator.run(adminembeds)
        await asyncio.sleep(90)
        await adminembeds.delete()




def setup(bot):
    bot.add_cog(HelpCommands(bot))