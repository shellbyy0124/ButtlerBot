import asyncio
import datetime
import discord
import json

from discord.ext import commands
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

TOKEN = data["guild"]["TOKEN"]
LT = data["guild"]["LT"]
cp = data["guild"]["command_prefix"]

members_join = data["channels"]["members_join"]
members_leave = data["channels"]["members_leave"]
bot_spam = data["channels"]["bot_spam"]
warnings = data["channels"]["warnings"]
botbugs = data["channels"]["botbugs"]
rules_agreement_logs = data["channels"]["rules_agreements_logs"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=cp, intents=intents)

@bot.event
async def on_ready():

    cogs = []

    for cog in cogs:
        bot.load_extension(cog)
        channel = bot.get_channel(bot_spam)
        a = await channel.send(f"{cog} loaded")
        await asyncio.sleep(1)
        await a.delete()
        await asyncio.sleep(1)
    channel1 = bot.get_channel(bot_spam)
    await channel1.send(f"**__ButtlerBot Extension Loader__** Start Up Complete!\nAll cogs have been loaded, and are ready to go\n```{', '.join(cogs)}```\nThis is an automated message. This message will delete in 5 seconds.")
    await asyncio.sleep(5)
    for i in range(cogs):
        channel2 = bot.get_channel(bot_spam)
        await channel2.purge(limit=i)

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

bot.run(TOKEN)