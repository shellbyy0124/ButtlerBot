import asyncio
import json
import discord
import psycopg2

from os import error
from discord.ext import commands, tasks
from discord.ext.commands import cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)


TOKEN = data["guild"]["BUTTLER_TOKEN"]
command_prefix = data["guild"]["command_prefix"]
members_join = data["channels"]["members_join"]
members_leave = data["channels"]["members_leave"]
LT = data["guild"]["LT"]
bot_spam = data["channels"]["bot_spam"]
warnings = data["channels"]["warnings"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=command_prefix, intents=intents, nickname_command=None)

@bot.event
async def on_ready():

    cogs = ["cogs.announcement", "cogs.challenges_command", "cogs.coinflip", "cogs.generalcommands",
            "cogs.menu", "cogs.profiles", "cogs.rules", "cogs.staff", "cogs.staffapplication",
            "cogs.support", "cogs.taskloops", "cogs.teams", "cogs.welcome"]

    for cog in cogs:
        bot.load_extension(cog)
        channel = bot.get_channel(bot_spam)
        await channel.send(f"{cog} loaded")
        await asyncio.sleep(1)

    channel = bot.get_channel(bot_spam)
    await channel.send("Cogs Loaded and Ready To Go!")
    await channel.purge(limit=14, check=lambda m: not m.pinned)

@bot.event
async def on_member_remove(member):

    channel = bot.get_channel(members_leave)
    await channel.send(f'{member.mention} has left the server')

@bot.listen('on_message') 
async def bprefix(message):

    if message.content.startswith("buttlerprefix"):
        msg = await message.channel.send("my prefix is `>`")
        await asyncio.sleep(10)
        await msg.delete()

@bot.event
async def on_message(message):
    member = message.author
    if not message.author.bot:
        filtered_words = ['newb', 'noob', 'shit', 'fuck', 'fck', 'FucK', 'fUck', 'dam', 'damn', 'danm', 'd@mn', 'dmn', 'shat', 'motherfucker', 'mf', 'smmfh', 'stfu', 'god damn', 'god dam', 'dang', 'cunt', 'bitch', 'b!tch', 'sob', 's.o.b', 'mf', 'mfs']
        for word in filtered_words:
            if word in message.content:
                await message.delete()
                await message.channel.send(f':red_circle: That word(s) is/are not allowed in this discord!, {member.mention} Try, Again! :red_circle:')

                warning = discord.Embed(color=discord.Colour.red(), title=f"{member.name}", description=f"**__Offending Content:__**{message.content}")
                channel = bot.get_channel(warnings)
                await channel.send(embed=warning)
    await bot.process_commands(message)

@commands.Cog.listener()
async def on_command_error(ctx,error):
    if isinstance(error.command, commands.CommandNotFound):
        emb = discord.Embed(title = "Error",description = "Command not found",color=discord.Colour.red())
        await ctx.send(embed = emb)
    else:
        embed = discord.Embed(title="Error",description = error,colour=discord.Colour.red())
        embed.timestamp = ctx.message.created_at
        await ctx.send(embed = embed)

bot.run(TOKEN)