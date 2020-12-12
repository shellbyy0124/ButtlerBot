import discord
import json
import random
import datetime
import sqlite3
import os
import asyncio

from os import error
from discord.ext import commands, tasks
from discord.ext.commands import cog


with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

TOKEN = data["BUTTLER_TOKEN"]
BOTOUTPUT = data["BOTOUTPUT"]
KPT = data["KasMek_Programming_Team"]
command_prefix = data["command_prefix"]
bot_spam = data["bot_spam"]
members_join_and_leave = data["members_join_and_leave"]
LT = data["LT"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=command_prefix, intents=intents, nickname_command=None)

@bot.event
async def on_ready():

    color = random.randint(0, 0xFFFFFF)

    mekasu = bot.get_user(260009824945831936)
    kastien = bot.get_user(770311161559646299)

    onready = discord.Embed(color = color, title=f"{bot.user.name}").add_field(name=f"Mistress {mekasu.name},", value=f"Cogs have fully loadedmadame!")
    onready.set_thumbnail(url=bot.user.avatar_url)
    onready.set_footer(text=f"Created By: {mekasu.name} and {kastien.name}")
    onready.timestamp = datetime.datetime.utcnow()

    channel = bot.get_channel(bot_spam)
    msg = await channel.send(embed=onready)
    await asyncio.sleep(5)
    await msg.delete()

    print('\nBot is online...')

@bot.event
async def on_member_join(member:discord.Member):

    welcome = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Hi and Welcome!", value=f"My name is {bot.user.name}, and I will be your virtual assistant during your stay here at the Learning Together Discord Community! :smile:", inline=False)
    welcome.add_field(name="To Get Started:", value=f"You must be a member of {bot.get_guild(KPT)} for at least 5 minutes before being able to chat with the community, so in the meantime I would like to cover some ground rules:", inline=False)
    welcome.add_field(name="First:", value="Respect of your peers is a must at all times.", inline=False)
    welcome.add_field(name="Second:", value="Making someone feel inferior to your is prohibited!", inline=False)
    welcome.add_field(name="Third:", value="Telling someone that their question is stupid is prohibited.", inline=False)
    welcome.add_field(name="Fourth", value="No Spamming! This includes: using the @ ability when there are sufficient support channels for your needs", inline=False)
    welcome.add_field(name="Fifth:", value="We have members of all ages that are welcome into this discord. No Cursing: NSFW: etc! It is prohibited!", inline=False)
    welcome.add_field(name="Sixth:", value="Keep the chats in accordance with the channels topic. Not sure? Look Up :smile:", inline=False)
    welcome.add_field(name="Seventh:", value="No Intimidation! We grow and learn together from day one and on", inline=False)
    welcome.add_field(name="Eighth:", value="Use the proper markups when submitting code. Discord supports many languages!", inline=False)
    welcome.add_field(name="And Finally:", value="If you have any more questions, use `>buttlerhelp` to call me, and if you'd like to get a better look at the rules, `>buttlerrules`", inline=False)
    welcome.add_field(name="Note:", value="This message will delete after 5 minutes. Once this message deletes, you will have access to the discord. If not, then please get in touch with a staff member!", inline=False)
    msg = await member.send(embed=welcome)
    channel = bot.get_channel(members_join_and_leave)
    await channel.send(f"Let's welcome {member.name} to {bot.get_guild(LT).name}!")
    await asyncio.sleep(300)
    await msg.delete()

@bot.event
async def on_member_remove(member):

    channel = bot.get_channel(members_join_and_leave)
    await channel.send(f'{member.mention} has left the server')

@bot.listen('on_message') 
async def stuff(message):

    if message.content.startswith("buttlerprefix"):
        msg = await message.channel.send("my prefix is `>`")
        await asyncio.sleep(10)
        await msg.delete()

@bot.event
async def on_message(message):
    if not message.author.bot:
        filtered_words = ['bad', 'noob']
        for word in filtered_words:
            if word in message.content:
                await message.delete()
                await message.author.send('What You Wanna Tell Them')
    await bot.process_commands(message)

bot.load_extension("cogs.botinformation")
bot.load_extension("cogs.dev")
bot.load_extension("cogs.generalcommands")
bot.load_extension("cogs.menu")
bot.load_extension("cogs.owner")
bot.load_extension("cogs.rules")
bot.load_extension("cogs.staff")
bot.load_extension("cogs.staffapplication")
bot.load_extension("cogs.taskloops")
bot.load_extension("cogs.welcome")
bot.load_extension("cogs.faqs")
bot.load_extension("cogs.announcement")
bot.load_extension("cogs.support")
bot.load_extension("cogs.admin")      

bot.run(TOKEN)