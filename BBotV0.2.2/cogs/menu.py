import discord
import json
import random
import datetime
import DiscordUtils
import asyncio

from os import error
from discord.ext import commands
from discord.ext.commands import cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

buttler_info = data["channels"]["buttler_info"]
staff_commands = data["channels"]["staff_commands"]
LT = data["guild"]["LT"]

class HelpCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["bhelp"])
    async def generalhelpmenu(self, ctx):
        
        time = datetime.datetime.utcnow()
        color = random.randint(0, 0xFFFFFF)
        bot = self.bot.user.avatar_url

        embed1 = discord.Embed(color=color, timestamp=time, title=f"Hi! I'm {self.bot.user.name}, and I'm here to help!", description="In the pages to follow are things that I am able to currently help you with, and a list of things that I am currently developing to better help you in the future! :smile: To get my help menu, type `/buttlerhelp` :heart:", inline=False)
        embed1.set_image(url=bot)
        embed1.set_footer(text='Page 1/19')
        
        embed2 = discord.Embed(color=color, timestamp=time, title="Want to invite your friends?", description="Instead of having to go through all those clickable menus to invite your friends, just type `>binvite` to receive a link made for you!", inline=False)
        embed2.set_image(url=bot)
        embed2.set_footer(text='Page 2/19')
        
        embed3 = discord.Embed(color=color, timestamp=time, title="Rules", description="Each member was sent a list of the rules when they joined, however, if the rules need to be referenced, please type `>brules` to receive a list of rules :smile:", inline=False)
        embed3.set_image(url=bot)
        embed3.set_footer(text='Page 3/19')
        
        embed4 = discord.Embed(color=color, timestamp=time, title="Resources", description="Everyone gets tired of having to google stuff all the time. We have a category dedicated to resources for all of our members. Please travel down to _Resources_ for more information!", inline=False)
        embed4.set_image(url=bot)
        embed4.set_footer(text='Page 4/19')

        embed5 = discord.Embed(color=color, timestamp=time, title="Coding Challenges", description="Have an idea for a coding challenge? The tell us about it with a suggestion for the bot :)")
        embed5.set_image(url=bot)
        embed5.set_footer(text="Page 5/19")
        
        embed6 = discord.Embed(color=color, timestamp=time, title="How To Present Your Code In This Discord", description="We ask that you do not post walls of code when asking your question, but to keep things more visual appealing, and using one of the links under the `>bpaste` command to show your code within the community.", inline=False)
        embed6.set_image(url=bot)
        embed6.set_footer(text='Page 6/19')
        
        embed7 = discord.Embed(color=color, timestamp=time, title="Staff Applications", description="If you would like to apply to become a staff member, please type `>bsapp` to start your application. When you go to do your application, please go down to the Applications category, then use the #apply_for_staff channel to start your application. When the command is executed, it will open a new channel with your name on it! Please do not have more than one channel open at a time. Once you've completed your application, and you are satisfied with it, and type 'exit', the channel will automatically delete itself. In addition, if you attempt to enter your answer, and you enter it incorrectly 3 times, the channel will notify you that the channel is being deleted due to insufficient answers being enetered, as well as, the application will time out after a while of not responding to the bot, and will also delete the channel after a certain amoutn of time.", inline=False)
        embed7.set_image(url=bot)
        embed7.set_footer(text='Page 7/19')

        embed8 = discord.Embed(color=color, timestamp=time, title="Bot Updates", description="All information on bot updates, community updates, and bots being added to the community can be found under the ___Announcements___ category.", inline=False)
        embed8.set_image(url=bot)
        embed8.set_footer(text='Page 8/19')
        
        embed9 = discord.Embed(color=color, timestamp=time, title="What bots do we use?", description="To see a list of the bots we use within the community, please type `>bblist` in the #bot_spam channel", inline=False)
        embed9.set_image(url=bot)
        embed9.set_footer(text='Page 9/19')
        
        embed10 = discord.Embed(color=color, timestamp=time, title="Have words you could careless to see?:", description="If you have a word, or a list of words, that you would like have added to the message filter, or would like to have a word removed, then please type `>bbadlist <message>`", inline=False)
        embed10.set_image(url=bot)
        embed10.set_footer(text='Page 10/19')
        
        embed11 = discord.Embed(color=color, timestamp=time, title="Need to have access to a To-Do list?", description=":red_circle:**BE ADVISED! THIS PART OF BUTTLER IS UNDER CONSTRUCTION!**\nAn announcement will be made once we have this section of the bot up and running!", inline=False)
        embed11.set_image(url=bot)
        embed11.set_footer(text="Page 11/19")
        
        embed12 = discord.Embed(color=color, timestamp=time, title="bot not responding?", description="If you know how to read a latency ping, then please use `>bping` to get a pong, and report that pong to the staff.", inline=False)
        embed12.set_image(url=bot)
        embed12.set_footer(text="Page 12/19")
        
        embed13 = discord.Embed(color=color, timestamp=time, title="Nick Names!", description="Type `/nick <new_name>` to change your nickname! Please keep it community appropriate! If you don't, the staff will change it, and you will be issued a warning!", inline=False)
        embed13.set_image(url=bot)
        embed13.set_footer(text="Page 13/19")
        
        embed14 = discord.Embed(color=color, timestamp=time, title="Submitting Your Code To A Team?", description="Submitting your code to be viewed by a team is as simple as going to the #bot_spam channel and typing `>btsubmit <link to code>`!", inline=False)
        embed14.set_image(url=bot)
        embed14.set_footer(text="Page 14/19")

        embed15 = discord.Embed(color=color, timestamp=time, title="Want to give a discord suggestion?", description="To submit your discord suggestion, type `>bdsubmit <your_suggestion>`", inline=False)
        embed15.set_image(url=bot)
        embed15.set_footer(text="Page 15/19")
        
        embed16 = discord.Embed(color=color, timestamp=time, title=f"Submitting A Suggestion For A Future Bot?", description="Want to submit an idea for a future bot? type `>bbsubmit <your_suggestion>`", inline=False)
        embed16.set_image(url=bot)
        embed16.set_footer(text="Page 16/19")
        
        embed17 = discord.Embed(color=color, timestamp=time, title="Don't know buttler's prefix?", description="just simply type `buttlerprefix`, and I'll let you know :smile:", inline=False)
        embed17.set_image(url=bot)
        embed17.set_footer(text="Page 17/19")
        
        embed18 = discord.Embed(color=color, timestamp=time, title="Want to create a profile?", description="To create a profile, head over to the __Profiles__ category, and check out the how-to channel", inline=False)
        embed18.set_image(url=bot)
        embed18.set_footer(text="Page 18/19")

        embed19 = discord.Embed(color=color, timestamp=time, title="Disclaimer!", description='This can/will be changed at any given time. If you are ever unsure of what commands are available to you, you can always type `/help` :smile: :clap:')
        embed19.set_image(url=bot)
        embed19.set_footer(text="Page 19/19")     

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        embeds = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19]
        await paginator.run(embeds)

    @commands.command(aliases=["bstaff"])
    @commands.has_any_role('Owner', 'Head Admin', 'Admin', 'Moderator', 'Community Helper')
    async def staffhelpmenu(self, ctx):

        color = random.randint(0, 0xFFFFFF)
        time = datetime.datetime.utcnow()
        bot = self.bot.user.avatar_url
        
        adminembed1 = discord.Embed(color=color, timestamp=time, title=f"Hi! I'm {self.bot.user.name}'s Staff Menu, and I'm here to help!", description="In the pages to follow are things that I am able to currently help you with, and below that is a list of things that I am currently developing to better help you in the future! :smile: To get my help menu, type `/bstaff`", inline=False)
        adminembed1.set_image(url=bot)
        adminembed1.set_footer(text='Page 1/14')
        
        adminembed2 = discord.Embed(color=color, timestamp=time, title="Server Statistics:", description="Want to help us keep up with the server stats? Type /bstats to get the pertinent info!", inline=False)
        adminembed2.set_thumbnail(url=bot)
        adminembed2.set_footer(text='Page 2/14')
        
        adminembed3 = discord.Embed(color=color, timestamp=time, title="User Inappropriate Nickname?", description="Do you see a user with an inappropriate username? then type /bcnick <username_as_currently_shown> <actual_name> and the user will automatically be dm'd a message of their nickname being changed. Adding a reason for why will be coming in a future update!", inline=False)
        adminembed3.set_thumbnail(url=bot)
        adminembed3.set_footer(text='Page 3/14')
        
        adminembed4 = discord.Embed(color=color, timestamp=time, title="Purging Channels: `>bpurge`", description="Do Not Abuse This Ability! If you are deleting less than 20-ish messages, then right click and delete them individually. This command is only for if someone has hacked us, or spammed us! It will delete pinned messages if you delete it with the bot! Try not to use this command if you are not an admin or higher. If unsure of when to use it, please ask an admin or higher in the staff chat channel", inline=False)
        adminembed4.set_thumbnail(url=bot)
        adminembed4.set_footer(text='Page 4/14')
        
        adminembed5 = discord.Embed(color=color, timestamp=time, title="Who Is Who but a Who!", description="Some have an incomprehensible nickname, and you want to know who they are, or need to change their nickname, then type /bwhois <username> and get that information!", inline=False)
        adminembed5.set_thumbnail(url=bot)
        adminembed5.set_footer(text='Page 5/14')

        adminembed6 = discord.Embed(color=color, timestamp=time, title="Someone being rude? Someone not playing nice?", description="Use `>bwarn <member>` and it will send them a warning in their dm's, and put a copy of the warning in the logs channel.", inline=False)
        adminembed6.set_thumbnail(url=bot)
        adminembed6.set_footer(text="Page 6/14")
        
        adminembed7 = discord.Embed(color=color, timestamp=time, title="A member being obnixious is the voice, or text channel?", description="Type `/btempmute <member_name> <time_in_seconds> <reason>` to mute them").add_field(name="\u200b", value="**THIS COMMAND IS UNDER CONSTRUCTION AND WILL NOT WORK**", inline=False)
        adminembed7.set_thumbnail(url=bot)
        adminembed7.set_footer(text='Page 7/14')
        
        adminembed8 = discord.Embed(color=color, timestamp=time, title="Locking Channels:", description="It is only ok to lock a channel with `>block` when we are being spammed, or a virus of some sort is in the server. Other than that, you can simply use the `>bwarn` or `>btempmute` commands to take care of the problem.", inline=False)
        adminembed8.set_thumbnail(url=bot)
        adminembed8.set_footer(text='Page 8/14')
        
        adminembed9 = discord.Embed(color=color, timestamp=time, title="Unlocking Channels:", description="As stated previously with the locking channels, and the appropriatness of that command, unlocking channels (`>bunlock`) are only to be done by the head admins or higher. We are the only ones with access to the files. We will let you know when it is safe!", inline=False)
        adminembed9.set_thumbnail(url=bot)
        adminembed9.set_footer(text="Page 9/14")
        
        adminembed10 = discord.Embed(color=color, timestamp=time, title="Need To Know Who's Here?", description="Use `>blistmem` to get a list of members within the discord\n`>blistroles` to get a list of the roles within the discord\n`>blistall` to get a list of all members in their perspective roles within the discord.", inline=False)
        adminembed10.set_thumbnail(url=bot)
        adminembed10.set_footer(text="Page 10/14")

        adminembed11 = discord.Embed(color=color, timestamp=time, title="Is a member getting promoted?", description="Use `>bpromotion <member>` to make a special announcement about it!")
        adminembed11.set_thumbnail(url=bot)
        adminembed11.set_footer(text="Page 11/14")
        
        adminembed12 = discord.Embed(color=color, timestamp=time, title="Need to close a channel for a team, or a user has finished receiving support? Just use `>close <channel>` to close it.")
        adminembed12.set_thumbnail(url=bot)
        adminemebd12.set_footer(text="Page 12/14")

        adminembed13 = discord.Embed(color=color, timestamp=time, title="Need to make an announcement?", description="Use `>bannounce` and follow the prompts on the screens to follow to get your announcement made :D", inline=False)
        adminembed13.set_thumbnail(url=bot)
        adminembed13.set_footer(text="Page 13/11")

        adminembed14 = discord.Embed(color=color, timestamp=time, title="Making An Announcement?", description="Use `>bannouce` to make your announcement. When making your announcement, be sure to read the screen carefully!!! **DO NOT USE OPTION C IF YOU ARE NOT THE HEAD DEV OR THE OWNER!!!!**", inline=False)
        adminembed14.set_thumbnail(url=bot)
        adminembed14.set_footer(text="Page 14/14")
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        adminembeds = [adminembed1, adminembed2, adminembed3, adminembed4, adminembed5, adminembed6, adminembed7, adminembed8, adminembed9, adminembed10, adminembed11, adminembed12, adminembed13, adminembed14]
        await paginator.run(adminembeds)

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev')
    async def binfo(self, ctx):

        color = random.randint(0, 0xFFFFFF)
        note1 = "This message will self-destruct after 300 seconds"
        time = datetime.datetime.utcnow()
        bot = self.bot.user.avatar_url
        
        buttler = discord.Embed(color=color, timestamp=time, title=f"{self.bot.user.name}:", description=f"Good Evening, Ladies and Gentlemen. My name is {self.bot.user.name} and I have been asked to escort you :smile:", inline=False)
        buttler.set_thumbnail(url=bot)
        buttler.set_footer(text=note1)

        buttler1 = discord.Embed(color=color, timestamp=time, title="\u200b", description=f"I have been created to become your virtual assistant. I was created by KasMek, LLC., and associates to become your virtual assistant within your community. Please go through this brief tutorial of who I am, what I can do, and how to access my information :smirk:", inline=False)
        buttler1.set_thumbnail(url=bot)
        buttler1.set_footer(text=note1)

        buttler2 = discord.Embed(color=color, timestamp=time, title=f"Moderation:", description=f"I have different moderation commands, of which you can view by typing `>bstaff`. This will display a window of all commands available to staff members at this time.", inline=False)
        buttler2.set_thumbnail(url=bot)
        buttler2.set_footer(text=note1)

        buttler3 = discord.Embed(color=color, timestamp=time, title=f"General Uses:", description=f'I also have commands that are available to your non-staff users. Type `>bhelp` for those.', inline=False)
        buttler3.set_thumbnail(url=bot)
        buttler3.set_footer(text=note1)

        buttler4 = discord.Embed(color=color, timestamp=time, title=f"Developments:", description=f"KasMek, LLC., and associates are currently working on developing so much more. They're goal is to incorporate Coding Challenges, Teams, and much more. Unfortunately at this time, I do not have any information on those delevopments, but you are always welcome to join the [Buttler Support Discord](https://discord.gg/w2AjHF6Nra) and subscribe to the #bot_updates announcement channel to receive all announcements when updates are made to the bot", inline=False)
        buttler4.set_thumbnail(url=bot)
        buttler4.set_footer(text=note1)

        buttler5 = discord.Embed(color=color, timestamp=time, title=f"ButtlerBots's Development Team:", description=f"**__Project Leaders:__**\nMekasu, Kastien\n**__Project Members:__**\n", inline=False)
        buttler5.set_thumbnail(url=bot)
        buttler5.set_footer(text=note1)

        buttler6 = discord.Embed(color=color, timestamp=time, title="To Get In Touch With The Creators:", description="**__Mekasu__**\n**Email:** __mekasurenae@outlook.com__\n**Discord:** __mekasu#7632__\n**Myspace:** __myspace.com/mekasu0124__\n\n\n**Kastien**\n**Email:** __kastiendev@gmail.com__\n**Discord:** __Kastien-Dev#4697__")
        buttler6.set_thumbnail(url=bot)
        buttler6.set_footer(text=note1)

        buttler7 = discord.Embed(color=color, timestamp=time, title=f"Disclaimer:", description=f"Please keep in mind that I am always in development. I am always due to change at any given time. In the event that I ever change, add, or remove a characteristic from myself, I will always let you know in the announcements channel, or by typing `>bbupdates`")
        buttler7.set_thumbnail(url=bot)
        buttler7.set_footer(text=note1)

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        embeds21 = [buttler, buttler1, buttler2, buttler3, buttler4, buttler5, buttler6, buttler7]
        await paginator.run(embeds21)

    @commands.command(aliases=['mekasu'])
    @commands.has_any_role('Owner', 'Head Dev')
    async def ownerhelpmenu(self, ctx):

        color = random.randint(0, 0xFFFFFF)
        time = datetime.datetime.utcnow()

        with open('./master.json', 'r', encoding='utf-8-sig') as apple:
            data = json.load(apple)
        
        mekasu = data["users"]["Shellbyy"]

        with open('./commands.json', 'r', encoding='utf-8-sig') as owner:
            data = json.load(owner)

        stuff = data["commands"]["owner"]

        owner1 = discord.Embed(color=color, timestamp=time, title=f"Welcome Mistress {self.bot.get_user(mekasu).name}. Here's your help menu :)", description=f"{str(stuff)}")
        
        channel = self.bot.get_channel(staff_commands)
        await channel.send(embed=owner1)


    @commands.command(aliases=['kastien'])
    @commands.has_any_role('Owner', 'Head Dev')
    async def help2(self, ctx):

        with open('./master.json', 'r', encoding='utf-8-sig') as apple2:
            data = json.load(apple2)

        kastien = data["users"]["kastien"]

        owner2 = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Welcome Mister {self.bot.get_user(kastien).name}. How may I assist you today?")
        owner2.add_field(name="Are you wanting to display information about me?", value="if so then please use `>binfo`")
        owner2.add_field(name="testing", value="testing")
        owner2.timestamp = datetime.datetime.utcnow()
        owner2.set_thumbnail(url=self.bot.get_user(kastien).avatar_url)

        channel = self.bot.get_channel(staff_commands)
        await channel.send(embed=owner2)
        
    
def setup(bot):
    bot.add_cog(HelpCommands(bot))