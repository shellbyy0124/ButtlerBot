import asyncio
import datetime
import discord
import json
import os
import sys
import random

from discord.ext import commands, tasks
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

TOKEN = data["guild"]["TOKEN"]
LT = data["guild"]["LT"]
cp = data["guild"]["command_prefix"]
bot_spam = data["channels"]["bot_spam"]
warnings = data["channels"]["warnings"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=cp, intents=intents)

@tasks.loop(minutes=20)
async def load_cog():
    
    cogs = ["cogs.announcements", "cogs.dev", "cogs.general", "cogs.memberleave", "cogs.menu", "cogs.minigames", "cogs.rules", "cogs.staff", "cogs.staffapplication", "cogs.submissions", "cogs.suggestions", "cogs.taskloops", "cogs.welcome"]
    count = len(cogs)

    msg = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=datetime.datetime.utcnow(), title="I Am Restarting. Please Bare With Me As I Reboot!", description=f"Load Complete\n\nNow Loading Cogs\nLoading {count} cogs in total", inline=False).set_image(url=bot.user.avatar_url)
    channel2 = bot.get_channel(bot_spam)
    await channel2.purge(limit=1)
    msg1 = await channel2.send(embed=msg)
    
    for cog in cogs:
        try:
            bot.load_extension(cog)
        except Exception as e:
            print(e)
        count -= 1
        channel = bot.get_channel(bot_spam)
        embed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=datetime.datetime.utcnow(), title="I Am Restarting. Please Bare With Me As I Reboot!", description=f"Now Loading Cogs\n{count} cogs left to load\n\n{cog} has been loaded.", inline=False).set_image(url=bot.user.avatar_url)
        await msg1.edit(embed=embed1)
        await asyncio.sleep(1)
    
    embed2 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=datetime.datetime.utcnow(), title="I Am Restarting. Please Bare With Me As I Reboot!", description=f"Now Loading Cogs\nAll Cogs Have Been Loaded\n```{', '.join(cogs)}```", inline=False).set_image(url=bot.user.avatar_url)
    await msg1.edit(embed=embed2)
    await asyncio.sleep(5)
    await msg1.delete()

@bot.event
async def on_ready():
    load_cog.start()

@bot.listen('on_message')
async def bprefix(message):
    if message.content.startswith("bprefix"):
        msg = await message.channel.send("my prefix is `>`")
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
    await bot.process_commands(message)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

@bot.command()
@commands.has_any_role('Owner', 'Head Dev')
async def updatescript(ctx):
    
    await ctx.message.delete()
    embed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="I Am Restarting. Please Bare With Me As I Reboot!", inline=False).set_image(url=bot.user.avatar_url)
    message = await ctx.send(embed=embed1)
    await asyncio.sleep(1)
    embed2 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="I Am Restarting. Please Bare With Me As I Reboot!", description="(#--------)", inline=False).set_image(url=bot.user.avatar_url)
    await message.edit(embed=embed2)
    await asyncio.sleep(1)
    embed3 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="I Am Restarting. Please Bare With Me As I Reboot!", description="(##-------)", inline=False).set_image(url=bot.user.avatar_url)
    await message.edit(embed=embed3)
    await asyncio.sleep(1)
    embed4 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="I Am Restarting. Please Bare WIth Me As I Reboot!", description="(###------)", inline=False).set_image(url=bot.user.avatar_url)
    await message.edit(embed=embed4)
    await asyncio.sleep(1)
    embed5 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="I Am Restarting. Please Bare With Me As I Reboot!", description="(####-----)", inline=False).set_image(url=bot.user.avatar_url)
    await message.edit(embed=embed5)
    await asyncio.sleep(1)
    embed6 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="I Am Restarting. Please Bare With Me As I Reboot!", description="(#####----)", inline=False).set_image(url=bot.user.avatar_url)
    await message.edit(embed=embed6)
    await asyncio.sleep(1)
    embed7 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="I Am Restarting. Please Bare With Me As I Reboot!", description="(######---)", inline=False).set_image(url=bot.user.avatar_url)
    await message.edit(embed=embed7)
    await asyncio.sleep(1)
    embed8 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="I Am Restarting. Please Bare With Me As I Reboot!", description="(#######--)", inline=False).set_image(url=bot.user.avatar_url)
    await message.edit(embed=embed8)
    await asyncio.sleep(1)
    embed9 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="I Am Restarting. Please Bare With Me As I Reboot!", description="(########-)", inline=False).set_image(url=bot.user.avatar_url)
    await message.edit(embed=embed9)
    await asyncio.sleep(1)
    embed10 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="I Am Restarting. Please Bare With Me As I Reboot!", description="(########)", inline=False).set_image(url=bot.user.avatar_url)
    await message.edit(embed=embed10)
    await asyncio.sleep(1)
    embed11 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="I Am Restarting. Please Bare With Me As I Reboot!", description="(########)\nLoad Complete\n\nNow Loading Cogs", inline=False).set_image(url=bot.user.avatar_url)
    await message.edit(embed=embed11)
    await restart_program()

bot.run(TOKEN)