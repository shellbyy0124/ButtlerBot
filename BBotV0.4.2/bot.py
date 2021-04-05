import asyncio
import datetime
import discord
import json
import os
import sys

from discord.ext import commands, tasks
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

TOKEN = data["guild"]["TOKEN"]
LT = data["guild"]["LT"]
cp = data["guild"]["command_prefix"]
bot_spam = data["channels"]["bot_spam1"]
warnings = data["channels"]["warnings"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=cp, intents=intents)

@bot.event
async def on_ready():
    await load_cog()
        
def restart_program():

    python = sys.executable
    os.execl(python, python, * sys.argv)

@bot.event
async def load_cog():

    cogs = ["cogs.announcements", "cogs.dev", "cogs.general", "cogs.memberleave", "cogs.menu", "cogs.minigames", "cogs.rules", "cogs.staff", "cogs.staffapplication", "cogs.submissions", 
            "cogs.suggestions", "cogs.taskloops", "cogs.welcome"]

    for cog in cogs:
        try:
            channel1 = bot.get_channel(bot_spam)
            m = await channel1.send(f"{cog} loaded")
            bot.load_extension(cog)
            await asyncio.sleep(1)
            await m.delete()
        except:
            channel2 = bot.get_channel(bot_spam)
            x = await channel2.send(f"{cog} reloaded")
            bot.reload_extension(cog)
            await asyncio.sleep(1)
            await x.delete()

    channel3 = bot.get_channel(bot_spam)
    y = await channel3.send("All Cogs Loaded")
    await asyncio.sleep(1)
    await y.delete()
    print("online")

@bot.command()
@commands.has_any_role('Owner', 'Head Dev')
async def update(ctx):

    await restart_program()

@bot.listen('on_message')
async def bprefix(message):
    if message.content.startswith("bprefix"):
        msg = await message.channel.send(f"my prefix is `{cp}`")
        await asyncio.sleep(10)
        await msg.delete()

@bot.event
async def on_message(message):
    member = message.author
    if not message.author.bot:
        filtered_words = ['newb', 'noob', 'shit', 'fuck', 'fck', 'FucK', 'fUck', 'dam', 'damn', 'danm', 'd@mn', 'dmn', 'shat',
                        'motherfucker', 'mf', 'smmfh', 'stfu', 'god damn', 'god dam', 'dang', 'cunt', 'bitch', 'b!tch', 'sob',
                        's.o.b', 'mf', 'mfs', 'penis', 'dick', 'vagina', 'vajayjay']
        for word in filtered_words:
            if word in message.content:
                await message.delete()
                a = await message.channel.send(f":red_circle: That word(s) is/are not allowed in this discord!, {member.mention}! Try Again! :red_circle:")
                warning = discord.Embed(color=discord.Colour.red(), timestamp=datetime.datetime.utcnow(), title=f"{member.name}", description=f"**__Offending Content:__**\n{message.content}")
                channel = bot.get_channel(warnings)
                await channel.send(embed=warning)
                await asyncio.sleep(10)
                await a.delete()

    with open('./members.json', 'r', encoding='utf-8-sig') as old:
        data = json.load(old)

    if not message.author.bot:

        current = data["members"][str(message.author.name)]["warnings"]
        current += 0.15

        with open('./members.json', 'w', encoding='utf-8-sig') as new:
            data = json.dump(data, new, indent=4)

    await bot.process_commands(message)

@bot.listen('on_message')
async def levelup(message):

    if message.author.bot:return

    with open('./members.json', 'r', encoding='utf-8-sig') as current:
        data = json.load(current)

    length = len(message.content.replace(" ", ""))
    
    data["members"][str(message.author.name)]["points"] += length*0.000001

    with open('./members.json', 'w', encoding='utf-8-sig') as new:
        data = json.dump(data, new, indent=4)
        
bot.run(TOKEN)