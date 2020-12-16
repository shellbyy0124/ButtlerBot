import discord
import json
import random
import asyncio

from os import error
from discord.ext import commands
from discord.ext.commands import cog
from discord.ext import tasks

with open('/home/shellbyy/Desktop/repofolder/ButtlerBot/BBotV0.2.2/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)


TOKEN = data["BUTTLER_TOKEN"]
command_prefix = data["command_prefix"]
members_join_and_leave = data["members_join_and_leave"]
LT = data["LT"]
bot_spam = data["bot_spam"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=command_prefix, intents=intents, nickname_command=None)

@bot.event
async def on_ready():

    channel = bot.get_channel(bot_spam)
    msg = await channel.send("Cogs loaded and ready to go!")
    await asyncio.sleep(5)
    await msg.delete()

bot.load_extension("cogs.admin")
bot.load_extension("cogs.announcement")
bot.load_extension("cogs.botinformation")
bot.load_extension("cogs.dev")
bot.load_extension("cogs.faqs")
bot.load_extension("cogs.generalcommands")
bot.load_extension("cogs.menu")
bot.load_extension("owner")
bot.load_extension("cogs.profiles")
bot.load_extension("cogs.ruels")
bot.load_extension("cogs.staff")
bot.load_extension("cogs.staffapplication")
bot.load_extension("cogs.support")
bot.load_extension("cogs.taskloops")
bot.load_extension("cogs.teams")
bot.load_extension("cogs.welcome")

@bot.event
async def on_member_remove(member):

    channel = bot.get_channel(members_join_and_leave)
    await channel.send(f'{member.mention} has left the server')

    with open("test.json") as fp:
        data = json.load(fp)
    if str(member.id) in data:
        with open("test.json") as d:
            data = json.load(d)
        if str(member.id) in data:
            del data[str(member.id)]

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

    

bot.run(TOKEN)