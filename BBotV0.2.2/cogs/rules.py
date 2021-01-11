import DiscordUtils as DiscordUtils
import discord
import json
import datetime
import asyncio

from discord.ext import commands
from discord.ext.commands import cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
BOTOUTPUT = data["channels"]["rules"]


class Rules(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def brules(self, ctx):
        now = datetime.datetime.now()+datetime.timedelta(minutes=5)
        embedrules1 = discord.Embed(timestamp=now, color=ctx.author.color, title="These Are The Rules For The Learning Together Community Discord!")
        embedrules1.add_field(name="\u200b", value="**___These rules are to be followed at all times!___**", inline=False)
        embedrules1.add_field(name="Below You Will See The Tiers Of Warnings", value="1-3 Warnings: temp mute from text/voice chat channels < 10 minutes\n4th Warning: 12 hour silence from text/voice chat channels\n5th Warning: 1-3 Day Tempban or Perma Ban", inline=False)
        embedrules1.add_field(name="Number 1:", value="Respect of your peers is a must at all times!", inline=False)
        embedrules1.add_field(name="Number 2:", value="Making someone feel inferior to your is prohibited!", inline=False)
        embedrules1.add_field(name="Number 3:", value="Telling someone that their question is stupid is prohibited. If you feel the person is not wanting to learn on purpose get with a staff member", inline=False)
        embedrules1.add_field(name="Number 4:", value="Being rude or indencent because you assume that everyone should have a pre-exisiting level of knowledge of python before requesting help is prohibited! We learn together!", inline=False)
        embedrules1.add_field(name="Number 5:", value="No Spamming! This includes but is not limited to: Over posting asking the same question over and over without showing progress or understanding using the @ ability when there are sufficient support channels for your needs", inline=False)
        embedrules1.add_field(name="Number 6:", value="We have members of all ages that are welcome into this discord. No Cursing: NSFW: etc! It is prohibited!", inline=False)
        embedrules1.add_field(name="Number 7:", value="Keep the chats in accordance with the channels topic. If you're not sure read the top of the channel window or ask", inline=False)
        embedrules1.add_field(name="Number 8:", value="No Intimidation! We grow and learn together from day one and on!", inline=False)
        embedrules1.add_field(name="Number 9:", value="Use the proper markups when submitting code. Discord supports many languages!", inline=False)
        embedrules1.add_field(name="**Disclaimer**:", value="These rules are subject to change at any time and will be posted to the announcements channel. This pyramid is at the staff discression as to the punishment they seem fit. You always have the right to appeal!", inline=False)
        msg = await ctx.send(embed=embedrules1)
        await asyncio.sleep(120)
        await msg.delete()




def setup(bot):
    bot.add_cog(Rules(bot))