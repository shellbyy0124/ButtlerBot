#* completely remove with open directory, and the STDOUT channel and replace all channels that say STDOUT with all the correct output channels which will be commented
#* next to it's print statement

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

with open('/home/shellbyy/Desktop/playground/Butler_v_0.0.3a/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

TOKEN = data["TOKEN"]
STDOUT = data["STDOUT"]
command_prefix = data["command_prefix"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=command_prefix, intents=intents, nickname_command=None)

#* works
@bot.event
async def on_ready():
    channel = bot.get_channel(STDOUT)
    await channel.send(f'{bot.user.name} is online')

#* works
@bot.event
async def on_member_join(member:discord.Member):
    await member.send(embed=embedrules)

#* works
@bot.event
async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```You Do Not Have All The Requirements For That Command!```")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("```You Do Not Have All The Required Permissions For That Command!```")
        else:
            raise error

#* works
#*commands that are in the help menu that have not been coded yet are going to be in the 0.0.2 release

@bot.command(name="buttlerhelp")
async def paginate(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://rickandmortyapi.com/api/character') as resp:
            x = await resp.json()
    y = random.randint(0, 19)
    y1 = random.randint(0, 19)
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
    y22 = random.randint(0, 19)

    embed1 = discord.Embed(color=ctx.author.color).add_field(name=f"Hi! I'm {bot.user.name}, and I'm here to help!",
                                                             value="In the pages to follow are things that I am able to currently help you with, and below that is a list of things that I am currently developing to better help you in the future! :smile:")
    embed1.set_image(url=x["results"][y]["image"])
    embed1.set_footer(text='Page 1/23')
    embed2 = discord.Embed(color=ctx.author.color).add_field(name="Got Friends?",
                                                             value="Invite Them With This Link! https://discord.gg/QyMuAaD9gs")
    embed2.set_image(url=x["results"][y1]["image"])
    embed2.set_footer(text='Page 2/23')
    embed3 = discord.Embed(color=ctx.author.color).add_field(name=f"Rules:",
                                                             value=f"Each member was dm'd a list of the rules when they joined {ctx.guild.name}, however, if the rules need to be referenced, please type /buttlerrules to receive a list of rules :)")
    embed3.set_image(url=x["results"][y2]["image"])
    embed3.set_footer(text='Page 3/23')
    embed4 = discord.Embed(color=ctx.author.color).add_field(name=f"How To Present Your Code In This Discord:",
                                                             value=f"When Pasting Code Within {ctx.guild.name}, please use [Paste Bin](https://pastebin.com/) or [Paste For Python](https://paste.pythondiscord.com/)")
    embed4.set_image(url=x["results"][y3]["image"])
    embed4.set_footer(text='Page 4/23')
    embed5 = discord.Embed(color=ctx.author.color).add_field(name=f"For A List of FAQ's:",
                                                             value="Please Type /buttlerfaqs to receive the Frequently Asked Questions, and their solutions :)")
    embed5.set_image(url=x["results"][y4]["image"])
    embed5.set_footer(text='Page 5/23')
    embed6 = discord.Embed(color=ctx.author.color).add_field(name=f"Staff Applications:",
                                                             value="If you would like to apply to become a staff member, please type /buttlerapplication to receive the application within the #staff_applications channel")
    embed6.set_image(url=x["results"][y5]["image"])
    embed6.set_footer(text='Page 6/23')
    embed7 = discord.Embed(color=ctx.author.color).add_field(name=f"Bot Updates",
                                                             value="For a list of the most recent bot updates, please type /botupdates.")
    embed7.set_image(url=x["results"][y6]["image"])
    embed7.set_footer(text='Page 7/23')
    embed8 = discord.Embed(color=ctx.author.color).add_field(name=f"List Of Bots In {ctx.guild.name}",
                                                             value="To see a list of the bots we have, and their open source github links, please type /botlist")
    embed8.set_image(url=x["results"][y7]["image"])
    embed8.set_footer(text='Page 8/23')
    embed9 = discord.Embed(color=ctx.author.color).add_field(name=f"Project Ideas:",
                                                             value="If you have a project that you would like to obtain collaboration on, please type /buttlerproject.")
    embed9.set_image(url=x["results"][y8]["image"])
    embed9.set_footer(text='Page 9/23')
    embed10 = discord.Embed(color=ctx.author.color).add_field(name=f"To Submit Your Code To A Team:",
                                                              value="For information on how to submit your code to a team, please type /buttlerteams")
    embed10.set_image(url=x["results"][y9]["image"])
    embed10.set_footer(text='Page 10/23')
    embed11 = discord.Embed(color=ctx.author.color).add_field(name=f"**Have An Idea For The Discord?**",
                                                              value="Do you have an idea for the discord? Type /buttlerdiscordsuggestions. Is your idea for a bot you might want to see in the discord? then type /buttlerbotsuggestion")
    embed11.set_image(url=x["results"][y10]["image"])
    embed11.set_footer(text='Page 11/23')
    embed12 = discord.Embed(color=ctx.author.color).add_field(name=f"Need Help?",
                                                              value=f"Do you need help with your code? Then type /buttlerhelp<language> to get help with your code! Be sure to replace <languange> with the language of the code you're needing assistance with! ***Be advised, this discord only provides support for Java, C#, Python, JavaScript, and HTML.")
    embed12.set_image(url=x["results"][y11]["image"])
    embed12.set_footer(text='Page 12/23')
    embed13 = discord.Embed(color=ctx.author.color).add_field(name="Resources:",
                                                              value=f"The command to obtain links to beginner resources, and resources for those who are more experienced, however, we do have 2 categories dedicated to resources for all of our members. Please travel down to _Resources For Beginners_ and _Resources_ for more information!")
    embed13.set_image(url=x["results"][y12]["image"])
    embed13.set_footer(text='Page 13/23')
    embed14 = discord.Embed(color=ctx.author.color).add_field(name='Coding Challenges Bot:',
                                                              value=f"This bot is controlled by the dev team, and has no general commands at this time.")
    embed14.set_image(url=x["results"][y13]["image"])
    embed14.set_footer(text="Page 14/23")
    embed15 = discord.Embed(color=ctx.author.color).add_field(name='Help Links:',
                                                              value=f"Type /buttlerbegin for a list of beginner links for the languages we currently support within this discord.")
    embed15.set_image(url=x["results"][y14]["image"])
    embed15.set_footer(text="Page 15/23")
    embed16 = discord.Embed(color=ctx.author.color).add_field(name=f"Need to have access to a To-Do list?",
                                                              value="Head on over to #to_do and use our ToDo Bot! **BE ADVISED! THIS PART OF BUTTLER IS UNDER CONSTRUCTION! FOR THE TIME BEING WE ARE USING TODO BOT! WE DO NOT OWN NOR DO WE HAVE A SUPPORT CHANNEL FOR THIS BOT! EVERYONE CAN SEE YOUR TODO LIST. NO ONE CAN ACCESS IT!**")
    embed16.set_image(url=x["results"][y15]["image"])
    embed16.set_footer(text="Page 16/23")
    embed17 = discord.Embed(color=ctx.author.color).add_field(name=f"Submitting Code",
                                                              value="When submitting code, please use it in the following way! ```/submit https://pastebin.com/<rest_of_url>\n/submit httos://paste.pythondiscord.com/<rest_of_url>\n/submit bot_suggestion <suggestion>\n/submit discord_suggestion <suggestion>``` if you do not do it in one of these formats, it will not work!.")
    embed17.set_image(url=x["results"][y16]["image"])
    embed17.set_footer(text="Page 17/23")
    embed18 = discord.Embed(color=ctx.author.color).add_field(name=f"{bot.user.name} not responding?",
                                                              value="type /ping to get a pong!")
    embed18.set_image(url=x["results"][y17]["image"])
    embed18.set_footer(text="Page 18/23")
    embed19 = discord.Embed(color=ctx.author.color).add_field(name=f"Nick Names!",
                                                              value="Type /nick to change your nickname! Please keep it community appropriate!")
    embed19.set_image(url=x["results"][y18]["image"])
    embed19.set_footer(text="Page 19/23")
    embed20 = discord.Embed(color=ctx.author.color).add_field(name=f"**Submitting Your Code To A Team?**",
                                                              value="To submit your code to the team submissions channel, type `/submitteamcode _<link to your pastebin>_`")
    embed20.set_image(url=x["results"][y20]["image"])
    embed20.set_footer(text="Page 20/23")
    embed21 = discord.Embed(color=ctx.author.color).add_field(name=f"**Submitting A Discord Suggestion?**",
                                                              value=f"To submit your discord suggestion, type `/submitdiscordsuggestion _<your_suggestion>_`")
    embed21.set_image(url=x["results"][y21]["image"])
    embed21.set_footer(text="Page 21/23")
    embed22 = discord.Embed(color=ctx.author.color).add_field(name=f"**Submitting A Suggestion For A Future Bot?**",
                                                              value=f"Want to submit an idea for a future bot? type `/submitbotsuggestion _<your_suggestion>_`")
    embed22.set_image(url=x["results"][y19]["image"])
    embed22.set_footer(text="Page 22/23")
    embed23 = discord.Embed(color=ctx.author.color).add_field(name=f"Disclaimer!",
                                                              value="This can/will be changed at any given time. If you're ever unsure of what commands are available to you for {bot.user.name} then please refer back to the #available_commands channel for updated commands :)")
    embed23.set_image(url=x["results"][y22]["image"])
    embed23.set_footer(text="Page 23/23 ")

    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    embeds = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19, embed20, embed21, embed22, embed23]
    await paginator.run(embeds)


#* works

@bot.command()
async def rules(ctx):
    global embedrules
    embedrules = discord.Embed(color=discord.Colour.red(), title="Rules For {ctx.guild.name}").add_field(name="\u200b",
                                                                value="""**These rules are to be followed at all times!
                                                                        tiers of consequences:***
                                                                        Warninings 1-3
                                                                        4th Warning = 1 Day Temp Ban
                                                                        5th Warning = 3 Day Temp ban
                                                                        6+ Warnings = Perma Ban
                                                                        **These rules are subject to change at any given time. In that event, an announcement will be made in the announcements channel!
                                                                        All warning levels are subject to change/tiers to be skipped depending on severity of infraction!!!**""")
    embedrules.set_image(url=bot.user.avatar_url)
    embedrules.set_footer(text="Page 1/10")
    embedrules1 = discord.Embed(color=discord.Colour.red(), title="**Rule #1**").add_field(name="\u200b",
                                                                value="You will be respectful of each and every member/staff member within this discord at all times.")
    embedrules1.set_image(url=bot.user.avatar_url)
    embedrules1.set_footer(text="Page 2/10")
    embedrules2 = discord.Embed(color=discord.Colour.red(), title="**Rule #2**").add_field(name="\u200b",
                                                                value="""Bullying will not be tolerated whatsoever within this discord. This is including, but not limited to:
                                                                1) Making someone feel inferior to your superirority complex
                                                                2) Making anyone feel like they asked a stupid question
                                                                3) Being an asshole because you assume that everyone should know something to a certain degree. This is a
                                                                learning community of 5 different languages. Get over yourself""")
    embedrules2.set_image(url=bot.user.avatar_url)
    embedrules2.set_footer(text="Page 3/10")
    embedrules3 = discord.Embed(color=discord.Colour.red(), title="**Rule #3**").add_field(name="\u200b",
                                                                value="""**NO SPAMMING!!!** Spamming includes, but is not limited to:
                                                                1) Over Posting unnecessary comments repetatively
                                                                2) Asking the same question over and over, and not showing any improvements, or results
                                                                3) Using the `@` ability to ping any staff member. Please use the support channels to receive
                                                                help with non-code related that cannot be answered in the non_code help channels.""")
    embedrules3.set_image(url=bot.user.avatar_url)
    embedrules3.set_footer("Page 4/10")
    embedrules4 = discord.Embed(color=discord.Colour.red(), title="**Rule #4**").add_field(name="\u200b",
                                                                value="We have members of all ages that are welcome into that discord. Please keep the chats clean!")
    embedrules4.set_image(url=bot.useravatar_url)
    embedrules4.set_footer("Page 5/10")
    embedrules5 = discord.Embed(color=discord.Colour.red(), title="**Rule #5**").add_field(name="\u200b",
                                                                value="""Keep the chats to their pertinent categories! If you're not sure of the text channels' category, elif you looked at the
                                                                top of the screen to see the category, else ask a staff member in the support channels""")
    embedrules5.set_image(url=bot.user.avatar_url)
    embedrules5.set_footer("Page 6/10")
    embedrules6 = discord.Embed(color=discord.Colour.red(), title="**Rule #6**").add_field(name="\u200b",
                                                                value="""**_NO PINGING STAFF MEMBERS_** If you need help that cannot be answered by asking the community, please use
                                                                the support channels to get in touch with a staff member.""")
    embedrules6.set_image(url=bot.user.avatar_url)
    embedrules6.set_footer(text="Page 7/10")
    embedrules7 = discord.Embed(color=discord.Colour.red(), title="**Rule #7**").add_field(name="\u200b",
                                                                value="""If you are submitting code to join a team, please use the #code_submission channel to submit your code. 
                                                                The bot will submit the code submission to the team leaders.""")
    embedrules7.set_image(url=bot.user.avatar_url)
    embedrules7.set_footer(text="Page 8/10")
    embedrules8 = discord.Embed(color=discord.Colour.red(), title="**Rule #8**").add_field(name="\u200b",
                                                                value="""No intimidating any programmers! We are a community to learn and grow together, and support everyone of all experience levels!
                                                                If you don't know what this means, then refer to Rule #2!""")
    embedrules8.set_image(url=bot.user.avatar_url)
    embedrules8.set_footer(test="Page 9/10")
    embedrules9 = discord.Embed(color=discord.Colour.red(), title="**Rule #9**").add_field(name="\u200b",
                                                                value="Please use the proper markups when submitting code. Discord supports many languages")
    embedrules9.set_image(url=bot.user.avatar_url)
    embedrules9.set_footer("Page 10/10")

    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    embedrules = [embedrules1, embedrules2, embedrules3, embedrules4, embedrules5, embedrules6, embedrules7, embedrules8, embedrules9]
    await paginator.run(embedrules)

#*works
@bot.command()
async def botlist(ctx, role:discord.Role):
    for member in role.members:
        if member.role == member.role is not bot.role:
            pass
        else:
            await ctx.send(bot.role)
#* works
@bot.command()
async def staffapplication(ctx):
    await ctx.send(f"Unfortunately at this time, {ctx.guild.name} is not accepting applications for staff members. Please check #announcements for when applications will open back up")
#* works

@bot.command(name="buttlerbegin")
async def beginnerlinks(ctx):
    await ctx.send(f"**This command is currently under construction. Please be adivsed that once commands become available in updates with {bot.user.name} that they will be posted in the Bot Updates announcement channel.")


#* works

@bot.command()
async def pasting(ctx):
    
    paste1 = discord.Embed(color=ctx.author.color).add_field(name=f"**When Posting Code In {ctx.guild.name}!**",
                                                              value=f"Please use [Pastebin](https://pastebin.com/), or [hastebin for Python](https://paste.pythondiscord.com/)")
    await ctx.send(embed=paste1)

#* works
""" find a way to tie this command in with the command that generates a category, and 2 text channels and 1 voice channel for newly created teams. This needs to sumit code to that teams submission
    channel which when the teams category, 2 text channels, and voice channel are created, the 2 text channel id's need to be exported to the json file so that when the lock and unlock command
    are used, those channel get affected as well"""

@bot.command(name="submitteamcode")
async def submitting(ctx, *, message):
    submitembed1 = discord.Embed(colour=discord.Color.green(), title=f'{ctx.author}').add_field(name="\u200b", value=f"**Code has been submitted to** _<team_name_in_community_discord>:_ {message}", inline=False)
    submitembed1.set_thumbnail(url=ctx.author.avatar_url)
    channel = bot.get_channel(STDOUT)
    await channel.send(embed=submitembed1)
    
#* works


@bot.command(name="submitdiscordsuggestion")
async def submitting2(ctx, *, message):
    submitembed2 = discord.Embed(colour=discord.Color.blue(), title=f'{ctx.author}').add_field(name="\u200b", value=f"**A suggestion for the discord has been submitted:** {message}", inline=False)
    submitembed2.set_thumbnail(url=ctx.author.avatar_url)
    channel=bot.get_channel(STDOUT)
    await channel.send(embed=submitembed2)


#* works


@bot.command(name="submitbotsuggestion")
async def submitting3(ctx, *, message):
    submitembed3 = discord.Embed(colour=discord.Color.orange(), title=f'{ctx.author}').add_field(name="\u200b", value=f"**A suggestion for future discord bots has been submitted:** {message}", inline=False)
    submitembed3.set_thumbnail(url=ctx.author.avatar_url)
    channel = bot.get_channel(STDOUT)
    await channel.send(embed=submitembed3)




#* admin help channel

@bot.command(name="buttleradmin")
@commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
async def adminhelpmenu(ctx):

    adminembed1 = discord.Embed(color=ctx.author.color).add_field(name=f"Hi! I'm {bot.user.name} Staff Menu, and I'm here to help!",
                                                             value="In the pages to follow are things that I am able to currently help you with, and below that is a list of things that I am currently developing to better help you in the future! :smile:")
    adminembed1.set_image(url=bot.user.avatar_url)
    adminembed1.set_footer(text='Page 1/20')
    adminembed2 = discord.Embed(color=ctx.author.color).add_field(name="Server Statistics:",
                                                             value="Want to help us keep up with the server stats? Type /stats to get the pertinent info!")
    adminembed2.set_image(url=bot.user.avatar_url)
    adminembed2.set_footer(text='Page 2/20')
    adminembed3 = discord.Embed(color=ctx.author.color).add_field(name=f"User Inappropriate Nickname?",
                                                             value="Do you see a user with an inappropriate username? then type /changenick <username_as_currently_shown> <actual_name> and the user will automatically be dm'd a message of their nickname being changed. Adding a reason for why will be coming in a future update!")
    adminembed3.set_image(url=bot.user.avatar_url)
    adminembed3.set_footer(text='Page 3/20')
    adminembed4 = discord.Embed(color=ctx.author.color).add_field(name=f"Purging Channels:",
                                                             value="Do Not Abuse This Ability! If you are deleting less than 23 messages, then right click and delete them individually. This command is only for if someone has hacked us, or spammed us! Try not to use this command if you are not an admin or higher. If unsure of when to use it, please ask an admin or higher in the staff chat channel")
    adminembed4.set_image(url=bot.user.avatar_url)
    adminembed4.set_footer(text='Page 4/20')
    adminembed5 = discord.Embed(color=ctx.author.color).add_field(name=f"Who Is Who but a Who!",
                                                             value="Some have an incomprehensible nickname, and you want to know who they are, or need to change their nickname, then type /whois <username> and get that information!")
    adminembed5.set_image(url=bot.user.avatar_url)
    adminembed5.set_footer(text='Page 5/20')
    # adminembed6 = discord.Embed(color=ctx.author.color).add_field(name=f"Staff Applications:",
    #                                                          value="If you would like to apply to become a staff member, please type /buttlerapplication to receive the application within the #staff_applications channel")
    # adminembed6.set_image(url=bot.user.avatar_url)
    # adminembed6.set_footer(text='Page 6/20')
    # adminembed7 = discord.Embed(color=ctx.author.color).add_field(name=f"Bot Updates",
    #                                                          value="For a list of the most recent bot updates, please type /botupdates.")
    # adminembed7.set_image(url=bot.user.avatar_url)
    # adminembed7.set_footer(text='Page 7/20')
    # adminembed8 = discord.Embed(color=ctx.author.color).add_field(name=f"List Of Bots In {ctx.guild.name}",
    #                                                          value="To see a list of the bots we have, and their open source github links, please type /botlist")
    # adminembed8.set_image(url=bot.user.avatar_url)
    # adminembed8.set_footer(text='Page 8/20')
    # adminembed9 = discord.Embed(color=ctx.author.color).add_field(name=f"Project Ideas:",
    #                                                          value="If you have a project that you would like to obtain collaboration on, please type /buttlerproject.")
    # adminembed9.set_image(url=bot.user.avatar_url)
    # adminembed9.set_footer(text='Page 9/20')
    # adminembed10 = discord.Embed(color=ctx.author.color).add_field(name=f"To Submit Your Code To A Team:",
    #                                                           value="For information on how to submit your code to a team, please type /buttlerteams")
    # adminembed10.set_image(url=bot.user.avatar_url)
    # adminembed10.set_footer(text='Page 10/20')
    # adminembed11 = discord.Embed(color=ctx.author.color).add_field(name=f"Have An Idea?",
    #                                                           value="Do you have an idea for the discord? Type /buttlerdiscordsuggestions. Is your idea for a bot you might want to see in the discord? then type /buttlerbotsuggestion")
    # adminembed11.set_image(url=bot.user.avatar_url)
    # adminembed11.set_footer(text='Page 11/20')
    # adminembed12 = discord.Embed(color=ctx.author.color).add_field(name=f"Need Help?",
    #                                                           value=f"Do you need help with your code? Then type /buttlerhelp<language> to get help with your code! Be sure to replace <languange> with the language of the code you're needing assistance with! ***Be advised, this discord only provides support for Java, C#, Python, JavaScript, and HTML.")
    # adminembed12.set_image(url=bot.user.avatar_url)
    # adminembed12.set_footer(text='Page 12/20')
    # adminembed13 = discord.Embed(color=ctx.author.color).add_field(name="Resources:",
    #                                                           value=f"The command to obtain links to beginner resources, and resources for those who are more experienced, however, we do have 2 categories dedicated to resources for all of our members. Please travel down to _Resources For Beginners_ and _Resources_ for more information!")
    # adminembed13.set_image(url=bot.user.avatar_url)
    # adminembed13.set_footer(text='Page 13/20')
    # adminembed14 = discord.Embed(color=ctx.author.color).add_field(name='Coding Challenges Bot:',
    #                                                           value=f"This bot is controlled by the dev team, and has no general commands at this time.")
    # adminembed14.set_image(url=bot.user.avatar_url)
    # adminembed14.set_footer(text="Page 14/20")
    # adminembed15 = discord.Embed(color=ctx.author.color).add_field(name='Help Links:',
    #                                                           value=f"Type /buttlerbegin for a list of beginner links for the languages we currently support within this discord.")
    # adminembed15.set_image(url=bot.user.avatar_url)
    # adminembed15.set_footer(text="Page 15/20")
    # adminembed16 = discord.Embed(color=ctx.author.color).add_field(name=f"Need to have access to a To-Do list?",
    #                                                           value="Head on over to #to_do and use our ToDo Bot! **BE ADVISED! THIS PART OF BUTTLER IS UNDER CONSTRUCTION! FOR THE TIME BEING WE ARE USING TODO BOT! WE DO NOT OWN NOR DO WE HAVE A SUPPORT CHANNEL FOR THIS BOT! EVERYONE CAN SEE YOUR TODO LIST. NO ONE CAN ACCESS IT!**")
    # adminembed16.set_image(url=bot.user.avatar_url)
    # adminembed16.set_footer(text="Page 16/20")
    # adminembed17 = discord.Embed(color=ctx.author.color).add_field(name=f"Submitting Code",
    #                                                           value="When submitting code, please use it in the following way! ```/submit https://pastebin.com/<rest_of_url>\n/submit httos://paste.pythondiscord.com/<rest_of_url>\n/submit bot_suggestion <suggestion>\n/submit discord_suggestion <suggestion>``` if you do not do it in one of these formats, it will not work!.")
    # adminembed17.set_image(url=bot.user.avatar_url)
    # adminembed17.set_footer(text="Page 17/20")
    # adminembed18 = discord.Embed(color=ctx.author.color).add_field(name=f"{bot.user.name} not responding?",
    #                                                           value="type /ping to get a pong!")
    # adminembed18.set_image(url=bot.user.avatar_url)
    # adminembed18.set_footer(text="Page 18/20")
    # adminembed19 = discord.Embed(color=ctx.author.color).add_field(name=f"Nick Names!",
    #                                                           value="Type /nick to change your nickname! Please keep it community appropriate!")
    # adminembed19.set_image(url=bot.user.avatar_url)
    # adminembed19.set_footer(text="Page 19/20")
    # adminembed23 = discord.Embed(color=ctx.author.color).add_field(name=f"Disclaimer!",
    #                                                           value="This can/will be changed at any given time. If you're ever unsure of what commands are available to you for {bot.user.name} then please refer back to the #available_commands channel for updated commands :)")
    # adminembed23.set_image(url=bot.user.avatar_url)
    # adminembed23.set_footer(text="Page 20/20")

    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    adminembeds = [adminembed1, adminembed2, adminembed3, adminembed4, adminembed5] #, adminembed6, adminembed7, adminembed8, adminembed9, adminembed10, adminembed11, adminembed12, adminembed13, adminembed14, adminembed15, adminembed16, adminembed17, adminembed18, adminembed19, adminembed20]
    await paginator.run(adminembeds)



#* works
@bot.command(name='stats')
@commands.has_permissions(ban_members=True)
async def serverinfo(ctx):
    role_count = len(ctx.guild.roles)
    emoji_count = len(ctx.guild.emojis)
    channel_count = len([x for x in ctx.guild.channels if isinstance(x, discord.channel.TextChannel)])
    embed = discord.Embed(timestamp=ctx.message.created_at)
    embed.add_field(name='Name (ID)', value=f"{ctx.guild.name} ({ctx.guild.id})")
    embed.add_field(name='Owner', value=ctx.guild.owner, inline=False)
    embed.add_field(name='Members', value=ctx.guild.member_count)
    embed.add_field(name='Verification Level', value=str(ctx.guild.verification_level))
    embed.add_field(name='Highest role', value=ctx.guild.roles[-1])
    embed.add_field(name='Number of roles', value=str(role_count))
    embed.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)

#* works

@bot.command(name="changenick")
@commands.has_permissions(ban_members=True)
async def changemembernickname(ctx, member:discord.Member, *, nick):
    existing_nick = member.display_name
    new_nick = await member.edit(nick=nick)
    nickembed = discord.Embed(colour=0xFB2605, title="**Inappropriate Nick Name!").add_field(name="\u200b", value=f"{member.name}, you have chosen an inappropriate nickname. The offending name is: '{existing_nick}, and it has been changed to; '{new_nick}''")
    await member.send(embed=nickembed)



#* works

@bot.command(name="purge")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount)



#* works

@bot.command()
@commands.has_any_role('Owner', 'Team Leader', 'Head Dev', 'Head Admin', 'Head Team Member')
async def whois(ctx, user: discord.Member):
    user = user or ctx.author
    if user is None:
        user = ctx.message.author
    if user.activity is not None:
        game = user.activity.name
    else:
        game = None
    voice_state = None if not user.voice else user.voice.channel
    embed = discord.Embed(timestamp=ctx.message.created_at)
    embed.add_field(name='User ID', value=user.id, inline=True)
    embed.add_field(name='Nick', value=user.nick, inline=True)
    embed.add_field(name='Status', value=user.status, inline=True)
    embed.add_field(name='On Mobile', value=user.is_on_mobile(), inline=True)
    embed.add_field(name='In Voice', value=voice_state, inline=True)
    embed.add_field(name='Game', value=game, inline=True)
    embed.add_field(name='Highest Role', value=user.top_role.name, inline=True)
    embed.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    embed.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_author(name=user.name, icon_url=user.avatar_url)
    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)



#* works

@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel locked.')



#* works

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel locked.')





#0.0.2 tbd



bot.run(TOKEN)