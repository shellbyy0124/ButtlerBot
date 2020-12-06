import DiscordUtils as DiscordUtils
import discord
import json
import aiohttp
import random
import datetime
import os

from os import error
from discord import member
from discord.ext import commands
from discord.ext.commands import cog
from discord.utils import get
from isort import logo

with open('/home/shellbyy/Desktop/repofolder/Mekasu/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
BOTOUTPUT = data["BOTOUTPUT"]


class Rules(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def buttlerrules(self, ctx):
        now = datetime.datetime.now()+datetime.timedelta(minutes=5)
        embedrules1 = discord.Embed(timestamp=now, color=ctx.author.color, title="These Are The Rules For The Learning Together Community Discord!").add_field(name="\u200b",
                                                                            value="These rules are to be followed at all times!", inline=False)
        embedrules1.set_image(url=self.bot.user.avatar_url)
        embedrules1.set_footer(text="Page 1/12")
        embedrules2 = discord.Embed(timestamp=now, color=ctx.author.color, title="Below You Will See The Tiers Of Warnings").add_field(name="\u200b", 
                                                            value="""1-3 Warnings: temp mute from text/voice chat channels < 10 minutes
                                                                        4th Warning: 12 hour silence from text/voice chat channels
                                                                        5th Warning: 1-3 Day Tempban or Perma Ban""", inline=False)
        embedrules2.set_image(url=self.bot.user.avatar_url)
        embedrules2.set_footer(text="Pase 2/12")
        embedrules3 = discord.Embed(timestamp=now, color=ctx.author.color).add_field(name="Number 1:", value="Respect of your peers is a must at all times!", inline=False)
        embedrules3.set_image(url=self.bot.user.avatar_url)
        embedrules3.set_footer(text="Pase 3/12")
        embedrules4 = discord.Embed(timestamp=now, color=ctx.author.color).add_field(name="Number 2:", value="Making someone feel inferior to your is prohibited!", inline=False)
        embedrules4.set_image(url=self.bot.user.avatar_url)
        embedrules4.set_footer(text="Page 4/12")
        embedrules5 = discord.Embed(timestamp=now, color=ctx.author.color).add_field(name="Number 3:", value="""Telling someone that their question is stupid is prohibited. If you feel the
                                                                                                                person is not wanting to learn on purpose get with a staff member""", inline=False)
        embedrules5.set_image(url=self.bot.user.avatar_url)
        embedrules5.set_footer(text="Page 5/12")
        embedrules6 = discord.Embed(timestamp=now, color=ctx.author.color).add_field(name="Number 4:", value="""Being rude or indencent because you assume that everyone should have a pre-exisiting
                                                                                                                level of knowledge of python before requesting help is prohibited! We learn together!""", inline=False)
        embedrules6.set_image(url=self.bot.user.avatar_url)
        embedrules6.set_footer(text="Page 6/12")
        embedrules7 = discord.Embed(timestamp=now, color=ctx.author.color).add_field(name="Number 5:", value="""No Spamming! This includes but is not limited to: Over posting asking the same question over and over
                                                                                                                without showing progress or understanding using the @ ability when there are sufficient support channels
                                                                                                                for your needs""", inline=False)
        embedrules7.set_image(url=self.bot.user.avatar_url)
        embedrules7.set_footer(text="page 7/12")
        embedrules8 = discord.Embed(timestamp=now, color=ctx.author.color).add_field(name="Number 6:", value="We have members of all ages that are welcome into this discord. No Cursing: NSFW: etc! It is prohibited!", inline=False)
        embedrules8.set_image(url=self.bot.user.avatar_url)
        embedrules8.set_footer(text="Page 8/12")
        embedrules9 = discord.Embed(timestamp=now, color=ctx.author.color).add_field(name="Number 7:", value="""Keep the chats in accordance with the channels topic. If you're not sure read the top of the channel
                                                                                                                window or ask""", inline=False)
        embedrules9.set_image(url=self.bot.user.avatar_url)
        embedrules9.set_footer(text="Page 9/12")
        embedrules10 = discord.Embed(timestamp=now, color=ctx.author.color).add_field(name="Number 8:", value="No Intimidation! We grow and learn together from day one and on!", inline=False)
        embedrules10.set_image(url=self.bot.user.avatar_url)
        embedrules10.set_footer(text="Page 10/12")
        embedrules11 = discord.Embed(timestamp=now, color=ctx.author.color).add_field(name="Number 9:", value="Use the proper markups when submitting code. Discord supports many languages!", inline=False)
        embedrules11.set_image(url=self.bot.user.avatar_url)
        embedrules11.set_footer(text="Page 11/12")
        embedrules12 = discord.Embed(timestamp=now, color=ctx.author.color).add_field(name="**Disclaimer**:", value="""These rules are subject to change at any time and will be posted to the announcements channel. 
                                                                                                                       This pyramid is at the staff discression as to the punishment they seem fit. You always have 
                                                                                                                       the right to appeal!""", inline=False)
        embedrules12.set_image(url=self.bot.user.avatar_url)
        embedrules12.set_footer(text="Page 12/12")
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏮️', "first")
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('🔐', "lock")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('⏭️', "last")
        embeds = [embedrules1, embedrules2, embedrules3, embedrules4, embedrules5, embedrules6, embedrules7, embedrules8, embedrules9, embedrules10, embedrules11, embedrules12]
        await paginator.run(embeds)




def setup(bot):
    bot.add_cog(Rules(bot))