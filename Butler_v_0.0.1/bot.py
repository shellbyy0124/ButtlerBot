#* completely remove with open directory, and the BotOutput channel and replace all channels that say BotOutput with all the correct output channels which will be commented
#* next to it's print statement

# All blocks of code that are in comments
# are for future updates in the event that I can
# get them working. if you want to work on them as well
# and comment what you did so that I can go back and write down
# my notes, then please do that :) -mekasu

from datetime import date
import DiscordUtils as DiscordUtils
import discord
import json
import aiohttp
import random
import os
import asyncio
import datetime
import time


from os import error
from discord import member
from discord import role
from discord.ext import commands
from discord.ext.commands import cog
from discord.ext import tasks

with open('/home/shellbyy/Desktop/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

TOKEN = data["BUTLER_TOKEN"]
BotOutput = data["Bot_Output_Testing_Channel"]
command_prefix = data["command_prefix"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=command_prefix, intents=intents, nickname_command=None)

#* works
@bot.event
async def on_ready():
    channel = bot.get_channel(BotOutput)
    await channel.send(f'{bot.user.name} is online')

#* works
@bot.event
async def on_member_join(member:discord.Member):
    await member.send(f"Hi,and Welcome! I am {bot.user.name}, and I'll be your guide today! Let's hope on over to the #verification channel, and type `/buttlerrules`.")


@bot.command(name="buttlerhelp")
async def paginate(ctx):
    now = datetime.datetime.now()+datetime.timedelta(minutes=5)
    async with aiohttp.ClientSession() as session:
        async with session.get('https://rickandmortyapi.com/api/character') as resp:
            x = await resp.json()
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

    embed1 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"Hi! I'm {bot.user.name}, and I'm here to help!",
                                                             value="In the pages to follow are things that I am able to currently help you with, and a list of things that I am currently developing to better help you in the future! :smile: To get my help menu, type `/buttlerhelp`")
    embed1.set_image(url=x["results"][y1]["image"])
    embed1.set_footer(text='Page 1/20')
    embed2 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name="Got Friends?",
                                                             value="Invite Them With This Link! https://discord.gg/QyMuAaD9gs")
    embed2.set_image(url=x["results"][y2]["image"])
    embed2.set_footer(text='Page 2/20')
    embed3 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"Rules:",
                                                             value=f"Each member was sent a list of the rules when they joined {ctx.guild.name}, however, if the rules need to be referenced, please type `/buttlerrules` to receive a list of rules :smile:")
    embed3.set_image(url=x["results"][y3]["image"])
    embed3.set_footer(text='Page 3/20')
    embed4 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"How To Present Your Code In This Discord:",
                                                             value=f"If you're unsure of how to paste code within {ctx.guild.name}, then type /paste to get the insider scoop :smile:")
    embed4.set_image(url=x["results"][y4]["image"])
    embed4.set_footer(text='Page 4/20')
    embed5 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"For A List of FAQ's:",
                                                             value="Please Type `/faqs` to receive the Frequently Asked Questions, and their solutions :thinking:")
    embed5.set_image(url=x["results"][y5]["image"])
    embed5.set_footer(text='Page 5/20')
    embed6 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"Staff Applications:",
                                                             value="If you would like to apply to become a staff member, please type `/staffapplication` to receive the application within the #staff_applications channel")
    embed6.set_image(url=x["results"][y6]["image"])
    embed6.set_footer(text='Page 6/20')
    embed7 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"Bot Updates",
                                                             value="For a list of the most recent bot updates, please type `/botupdates` to get the link to our text channel for our updates that come out for our communities bots.")
    embed7.set_image(url=x["results"][y7]["image"])
    embed7.set_footer(text='Page 7/20')
    embed8 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"List Of Bots In {ctx.guild.name}",
                                                             value="To see a list of the bots we have, and their open source github links, please type `/botlist`")
    embed8.set_image(url=x["results"][y8]["image"])
    embed8.set_footer(text='Page 8/20')
    embed9 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"Project Ideas:",
                                                             value="If you have a project that you would like to obtain collaboration on, please type `/buttlerproject`")
    embed9.set_image(url=x["results"][y9]["image"])
    embed9.set_footer(text='Page 9/20')
    embed10 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"Need Help?",
                                                              value=f"Do you need help with your code? Then type `/buttlerhelp<language>` to get help with your code! Be sure to replace `<languange>` with the language of the code you're needing assistance with! **Be advised, this discord only provides support for Java, C#, Python, JavaScript, and HTML!**")
    embed10.set_image(url=x["results"][y10]["image"])
    embed10.set_footer(text='Page 10/20')
    embed11 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name="Resources:",
                                                              value=f"We have 2 categories dedicated to resources for all of our members. Please travel down to _Resources For Beginners_ and _Resources_ for more information!")
    embed11.set_image(url=x["results"][y11]["image"])
    embed11.set_footer(text='Page 11/20')
    embed12 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name='Coding Challenges:',
                                                              value=f"The coding challenges section of ButtlerBot is currently under construction.")
    embed12.set_image(url=x["results"][y12]["image"])
    embed12.set_footer(text="Page 12/20")
    embed13 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"Need to have access to a To-Do list?",
                                                              value="Head on over to #to_do and use our ToDo Bot! \n\n\n**BE ADVISED! THIS PART OF BUTTLER IS UNDER CONSTRUCTION! FOR THE TIME BEING WE ARE USING TODO BOT! WE DO NOT OWN NOR DO WE HAVE A SUPPORT CHANNEL FOR THIS BOT! EVERYONE CAN SEE YOUR TODO LIST. NO ONE CAN ACCESS IT!**")
    embed13.set_image(url=x["results"][y13]["image"])
    embed13.set_footer(text="Page 13/20")
    embed14 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"Keep getting fussed at to use the allowed links to post your code, but keep forgetting?",
                                                              value="When submitting code, please use it in the following way!\n`/submit https://pastebin.com/<rest_of_url>`\n`/submit https://paste.pythondiscord.com/<rest_of_url>`\n`/submit bot_suggestion <suggestion>`\n`/submit discord_suggestion <suggestion>` if you do not do it in one of these formats, it will not work!.")
    embed14.set_image(url=x["results"][y14]["image"])
    embed14.set_footer(text="Page 14/20")
    embed15 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"{bot.user.name} not responding?",
                                                              value="type `/ping` to get a pong!")
    embed15.set_image(url=x["results"][y15]["image"])
    embed15.set_footer(text="Page 15/20")
    embed16 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"Nick Names!",
                                                              value="Type `/nick` to change your nickname! Please keep it community appropriate! If you don't, the staff will change it!")
    embed16.set_image(url=x["results"][y16]["image"])
    embed16.set_footer(text="Page 16/20")
    embed17 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"**Submitting Your Code To A Team?**",
                                                              value="To submit your code to the team submissions channel, type `/submitteamcode <link to your pastebin>`")
    embed17.set_image(url=x["results"][y17]["image"])
    embed17.set_footer(text="Page 17/20")
    embed18 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"**Submitting A Discord Suggestion?**",
                                                              value=f"To submit your discord suggestion, type `/submitdiscordsuggestion <your_suggestion>`")
    embed18.set_image(url=x["results"][y18]["image"])
    embed18.set_footer(text="Page 18/20")
    embed19 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"**Submitting A Suggestion For A Future Bot?**",
                                                              value=f"Want to submit an idea for a future bot? type `/submitbotsuggestion <your_suggestion>`")
    embed19.set_image(url=x["results"][y19]["image"])
    embed19.set_footer(text="Page 19/20")
    embed20 = discord.Embed(timestamp = now, color=ctx.author.color).add_field(name=f"Disclaimer!",
                                                              value=f'This can/will be changed at any given time. If you are ever unsure of what commands are available to you, you can always type `/help` :smile: :clap:')
    embed20.set_image(url=x["results"][y20]["image"])
    embed20.set_footer(text="Page 20/20 ")           

    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    embeds = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19, embed20]
    await paginator.run(embeds)
    

#* works

@bot.command()
async def buttlerrules(ctx):
    now = datetime.datetime.now()+datetime.timedelta(minutes=5)
    embedrules1 = discord.Embed(timestamp=now, color=discord.Colour.orange(), title="These Are The Rules For The Learning Together Community Discord!").add_field(name="\u200b",
                                                                         value="These rules are to be followed at all times!", inline=False)
    embedrules1.set_image(url=bot.user.avatar_url)
    embedrules1.set_footer(text="Page 1/12")
    embedrules2 = discord.Embed(timestamp=now, color=discord.Colour.orange(), title="Below You Will See The Tiers Of Warnings").add_field(name="\u200b", 
                                                          value="""1-3 Warnings: temp mute from text/voice chat channels < 10 minutes
                                                                     4th Warning: 12 hour silence from text/voice chat channels
                                                                     5th Warning: 1-3 Day Tempban or Perma Ban""", inline=False)
    embedrules2.set_image(url=bot.user.avatar_url)
    embedrules2.set_footer(text="Pase 2/12")
    embedrules3 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 1:", value="Respect of your peers is a must at all times!", inline=False)
    embedrules3.set_image(url=bot.user.avatar_url)
    embedrules3.set_footer(text="Pase 3/12")
    embedrules4 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 2:", value="Making someone feel inferior to your is prohibited!", inline=False)
    embedrules4.set_image(url=bot.user.avatar_url)
    embedrules4.set_footer(text="Page 4/12")
    embedrules5 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 3:", value="Telling someone that their question is stupid is prohibited. If you feel the person is not wanting to learn on purpose get with a staff member", inline=False)
    embedrules5.set_image(url=bot.user.avatar_url)
    embedrules5.set_footer(text="Page 5/12")
    embedrules6 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 4:", value="Being rude or indencent because you assume that everyone should have a pre-exisiting level of knowledge of python before requesting help is prohibited! We learn together!", inline=False)
    embedrules6.set_image(url=bot.user.avatar_url)
    embedrules6.set_footer(text="Page 6/12")
    embedrules7 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 5:", value="No Spamming! This includes but is not limited to: Over posting asking the same question over and over without showing progress or understanding using the @ ability when there are sufficient support channels for your needs", inline=False)
    embedrules7.set_image(url=bot.user.avatar_url)
    embedrules7.set_footer(text="page 7/12")
    embedrules8 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 6:", value="We have members of all ages that are welcome into this discord. No Cursing: NSFW: etc! It is prohibited!", inline=False)
    embedrules8.set_image(url=bot.user.avatar_url)
    embedrules8.set_footer(text="Page 8/12")
    embedrules9 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 7:", value="Keep the chats in accordance with the channels topic. If you're not sure read the top of the channel window or ask", inline=False)
    embedrules9.set_image(url=bot.user.avatar_url)
    embedrules9.set_footer(text="Page 9/12")
    embedrules10 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 8:", value="No Intimidation! We grow and learn together from day one and on!", inline=False)
    embedrules10.set_image(url=bot.user.avatar_url)
    embedrules10.set_footer(text="Page 10/12")
    embedrules11 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 9:", value="Use the proper markups when submitting code. Discord supports many languages!", inline=False)
    embedrules11.set_image(url=bot.user.avatar_url)
    embedrules11.set_footer(text="Page 11/12")
    embedrules12 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="**Disclaimer**:", value="These rules are subject to change at any time and will be posted to the announcements channel. This pyramid is at the staff discression as to the punishment they seem fit. You always have the right to appeal!", inline=False)
    embedrules12.set_image(url=bot.user.avatar_url)
    embedrules12.set_footer(text="Page 12/12")
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('🔐', "lock")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    embeds = [embedrules1, embedrules2, embedrules3, embedrules4, embedrules5, embedrules6, embedrules7, embedrules8, embedrules9, embedrules10, embedrules11, embedrules12]
    await paginator.run(embeds)



#*works
@bot.command(name='buttlerbotlist')
async def botlist(ctx=None):
    role = discord.utils.get(ctx.guild.roles, name="Bots")
    await ctx.send(", ".join(member.mention for member in role.members if member.bot))


#* works
@bot.command(name="buttlerstaffapp")
async def staffapplication(ctx):
    await ctx.send(f"Unfortunately at this time, {ctx.guild.name} is not accepting applications for staff members. Please check #announcements for when applications will open back up")


#* works

@bot.command(name="buttlerpaste")
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
    submitembed1 = discord.Embed(colour=discord.Color.green(), title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted Code**: {message}", inline=False)
    submitembed1.set_thumbnail(url=ctx.author.avatar_url)
    channel = bot.get_channel(BotOutput)
    await channel.send(embed=submitembed1)
    
#* works


@bot.command(name="submitdiscordsuggestion")
async def submitting2(ctx, *, message):
    submitembed2 = discord.Embed(colour=discord.Color.blue(), title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted A Suggestion For The Discord:** {message}", inline=False)
    submitembed2.set_thumbnail(url=ctx.author.avatar_url)
    channel=bot.get_channel(BotOutput)
    await channel.send(embed=submitembed2)


#* works


@bot.command(name="submitbotsuggestion")
async def submitting3(ctx, *, message):
    submitembed3 = discord.Embed(colour=discord.Color.orange(), title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted A Suggestion For Bots:** {message}", inline=False)
    submitembed3.set_thumbnail(url=ctx.author.avatar_url)
    channel = bot.get_channel(BotOutput)
    await channel.send(embed=submitembed3)




#* admin help channel

@bot.command(name="buttleradminhelp")
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
    adminembed6 = discord.Embed(color=ctx.author.color).add_field(name=f"A member being obnixious is the voice, or text channel?",
                                                             value="Type `/tempmute <member_name> <time_in_seconds> <reason>` to mute them")
    adminembed6.set_image(url=bot.user.avatar_url)
    adminembed6.set_footer(text='Page 6/20')

    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    adminembeds = [adminembed1, adminembed2, adminembed3, adminembed4, adminembed5, adminembed6]
    #adminembed7, adminembed8, adminembed9, adminembed10, adminembed11, adminembed12, adminembed13, adminembed14, adminembed15, adminembed16, adminembed17, adminembed18, adminembed19, adminembed20]
    await paginator.run(adminembeds)



#* works
@bot.command(name='buttlerstats')
@commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
async def serverinfo(ctx):
    role_count = len(ctx.guild.roles)
    emoji_count = len(ctx.guild.emojis)
    channel_count = len([x for x in ctx.guild.channels if isinstance(x, discord.channel.TextChannel)])
    embed = discord.Embed(timestamp=ctx.message.created_at)
    embed.add_field(name='Name (ID)', value=f"{ctx.guild.name} ({ctx.guild.id})", inline=False)
    embed.add_field(name='Owner', value=ctx.guild.owner, inline=False)
    embed.add_field(name='Members', value=ctx.guild.member_count, inline=False)
    embed.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
    embed.add_field(name='Highest role', value=ctx.guild.roles[-1], inline=False)
    embed.add_field(name='Number of roles', value=str(role_count), inline=False)
    embed.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)

#* works

@bot.command(name="buttlerchangenick")
@commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
async def changemembernickname(ctx, member:discord.Member, nick):
    existing_nick = member.display_name
    new_nick = await member.edit(nick=nick)
    nickembed = discord.Embed(colour=0xFB2605, title="**Inappropriate Nick Name!").add_field(name="\u200b", value=f"{member.name}, you have chosen an inappropriate nickname. The offending name is: '{existing_nick}, and it has been changed to; {new_nick}")
    await member.send(embed=nickembed)



#* works

@bot.command(name="buttlerpurge")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{bot.user.name} has purged {amount} messages from this channel!")



#* works

@bot.command(name='buttlerwhois')
@commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
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

@bot.command(name='buttlerlock')
@commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f'{bot.user.name} has locked this channel.')



#* works

@bot.command(name='buttlerunlock')
@commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f'{bot.user.name} has unlocked this channel.')




#* works

@bot.command(name='buttlerlistmembers')
@commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
async def listmembers(ctx):
    now = datetime.datetime.now()+datetime.timedelta(minutes=5)
    members = []
    for m in ctx.guild.members:
        if not m.bot:
            members.append(m.name)

            #stuff1 = discord.Embed(timestamp=now, color=discord.Colour.purple(), title=f"Members:", description=f"""{(", ".join([members]))}""")

    channel = bot.get_channel(BotOutput)
    await channel.send(", ".join(members))
    
    
    



bot.run(TOKEN)