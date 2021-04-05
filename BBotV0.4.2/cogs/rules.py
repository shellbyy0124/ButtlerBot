import discord
import random
import datetime
import asyncio

from discord.ext import commands
from discord.ext.commands import Cog 

class Rules(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.time = datetime.datetime.utcnow()
        self.url = self.bot.user.avatar_url

    @commands.command()
    async def rules(self, ctx):

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

        def check(m):
            return ctx.message.author == m.author
        
        embed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Please Select From One Of The Following Using The Number (one, two, three):", description="Page 3: Discipline Tier\nPage 4:Respect\nPage 5: Bullying\nPage 6: Learning\nPage 7: Rudeness.Disrespect\nPage 8: Spamming\nPage 9: NSFW\nPage 10: Channel Topics\nPage 11: Intimidation\nPage 12: Mark-Ups\nPage 13: Discord Invites\n**__Note:__**\nThis numbering system starts with three, and goes through thirteen", inline=False).set_thumbnail(url=self.url)
        msg = await ctx.send(embed=embed1)
        ans = await self.bot.wait_for('message', check=check)

        if ans.content.lower() == "three":
            await ctx.message.delete()
            await ans.delete()
            embedrules3 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Below You Will See The Tiers Of Warnings", description="1-3 Warnings: temp mute from text/voice chat channels < 10 minutes\n4th Warning: 12 hour silence from text/voice chat channels\n5th Warning: 1-3 Day Tempban or Perma Ban", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 3/14")
            await msg.edit(embed=embedrules3)
        elif ans.content.lower() == "four":
            await ctx.message.delete()
            await ans.delete()
            embedrules4 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Number 1:", description="Respect of your peers is a must at all times!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 4/14")
            await msg.edit(embed=embedrules4)
        elif ans.content.lower() == "five":
            await ctx.message.delete()
            await ans.delete()
            embedrules5 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Number 2:", description="Making someone feel inferior to your is prohibited!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 5/14")
            await msg.edit(embed=embedrules5)
        elif ans.content.lower() == "six":
            await ctx.message.delete()
            await ans.delete()
            embedrules6 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Number 3:", description="Telling someone that their question is stupid is prohibited. If you feel the person is not wanting to learn on purpose get with a staff member", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 6/14")
            await msg.edit(embed=embedrules6)
        elif ans.content.lower() == "seven":
            await ctx.message.delete()
            await ans.delete()
            embedrules7 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Number 4:", description="Being rude or indencent because you assume that everyone should have a pre-exisiting level of knowledge of python before requesting help is prohibited! We learn together!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 7/14")
            await msg.edit(embed=embedrules7)
        elif ans.content.lower() == "eight":
            await ctx.message.delete()
            await ans.delete()
            embedrules8 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Number 5:", description="No Spamming! This includes but is not limited to: Over posting asking the same question over and over without showing progress or understanding using the @ ability when there are sufficient support channels for your needs", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 8/14")
            await msg.edit(embed=embedrules8)
        elif ans.content.lower() == "nine":
            await ctx.message.delete()
            await ans.delete()
            embedrules9 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Number 6:", description="We have members of all ages that are welcome into this discord. No Cursing: NSFW: etc! It is prohibited!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 9/14")
            await msg.edit(embed=embedrules9)
        elif ans.content.lower() == "ten":
            await ctx.message.delete()
            await ans.delete()
            embedrules10 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Number 7:", description="Keep the chats in accordance with the channels topic. If you're not sure read the top of the channel window or ask", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 10/14")
            await msg.edit(embed=embedrules10)
        elif ans.content.lower() == "eleven":
            await ctx.message.delete()
            await ans.delete()
            embedrules11 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Number 8:", description="No Intimidation! We grow and learn together from day one and on!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 11/14")
            await msg.edit(embed=embedrules11)
        elif ans.content.lower() == "twelve":
            await ctx.message.delete()
            await ans.delete()
            embedrules12 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Number 9:", description="Use the proper markups when submitting code. Discord supports many languages!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 12/14")
            await msg.edit(embed=embedrules12)
        elif ans.content.lower() == "thirteen":
            await ctx.message.delete()
            await ans.delete()
            embedrules13 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Number 10:", description="Do not create your own invite to this discord. An invite link has already been created for you to use. Type `>binbite` for the link", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 13/14")
            await msg.edit(embed=embedrules13)
        

def setup(bot):
    bot.add_cog(Rules(bot))