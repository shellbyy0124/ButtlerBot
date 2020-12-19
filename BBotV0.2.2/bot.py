import discord
import json
import random
import asyncio

from os import error
from discord import channel
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
warnings = data["warnings"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=command_prefix, intents=intents, nickname_command=None)

@bot.event
async def on_ready():

    channel = bot.get_channel(bot_spam)
    msg = await channel.send("Cogs loaded and ready to go!")
    await asyncio.sleep(5)
    await msg.delete()

cogs = ["cogs.admin", "cogs.announcement", "cogs.botinformation",
        "cogs.dev", "cogs.faqs", "cogs.generalcommands",
        "cogs.menu", "cogs.profiles", "cogs.rules",
        "cogs.staff", "cogs.staffapplication", "cogs.support",
        "cogs.taskloops", "cogs.teams", "cogs.welcome"]

for cog in cogs:
    bot.load_extension(cog)

@bot.event
async def on_member_remove(member):

    channel = bot.get_channel(members_join_and_leave)
    await channel.send(f'{member.mention} has left the server')

    # some code to check database for leaving member. if exist - remove from under "members"

@bot.listen('on_message') 
async def stuff(message):

    if message.content.startswith("buttlerprefix"):
        msg = await message.channel.send("my prefix is `>`")
        await asyncio.sleep(10)
        await msg.delete()

@bot.event
async def on_message(message):
    member = message.author
    if not message.author.bot:
        filtered_words = ['newb', 'noob', 'shit', 'fuck', 'fck', 'FucK', 'fUck', 'dam', 'damn', 'danm', 'd@mn', 'dmn', 'shat', 'motherfucker', 'mf', 'smmfh', 'stfu', 'god damn', 'god dam', 'dang', 'cunt', 'bitch', 'b!tch']
        for word in filtered_words:
            if word in message.content:
                await message.delete()
                await message.channel.send(f'That is not allowed as a sentece, {member.mention}  xD try again :P')

                warning = discord.Embed(color=discord.Colour.red(), title=f"{member.name}", description=f"")
                channel = bot.get_channel(warnings)
                await channel.send(embed=warning)
    await bot.process_commands(message)

    

bot.run(TOKEN)