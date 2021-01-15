import DiscordUtils
import discord
import random
import datetime

from discord.ext import commands
from discord.ext.commands import cog

class Rules(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.color = random.randint(0, 0xFFFFFF)
        self.time = datetime.datetime.utcnow()
        self.url = self.bot.user.avatar_url

    @commands.command()
    async def brules(self, ctx):

        
        embedrules1 = discord.Embed(color=self.color, timestamp=self.time, title="These Are The Rules For The Learning Together Community Discord!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 1/14")
        embedrules2 = discord.Embed(color=self.color, timestamp=self.time, name="\u200b", value="**___These rules are to be followed at all times!___**", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 2/14")
        embedrules3 = discord.Embed(color=self.color, timestamp=self.time, name="Below You Will See The Tiers Of Warnings", value="1-3 Warnings: temp mute from text/voice chat channels < 10 minutes\n4th Warning: 12 hour silence from text/voice chat channels\n5th Warning: 1-3 Day Tempban or Perma Ban", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 3/14")
        embedrules4 = discord.Embed(color=self.color, timestamp=self.time, name="Number 1:", value="Respect of your peers is a must at all times!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 4/14")
        embedrules5 = discord.Embed(color=self.color, timestamp=self.time, name="Number 2:", value="Making someone feel inferior to your is prohibited!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 5/14")
        embedrules6 = discord.Embed(color=self.color, timestamp=self.time, name="Number 3:", value="Telling someone that their question is stupid is prohibited. If you feel the person is not wanting to learn on purpose get with a staff member", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 6/14")
        embedrules7 = discord.Embed(color=self.color, timestamp=self.time, name="Number 4:", value="Being rude or indencent because you assume that everyone should have a pre-exisiting level of knowledge of python before requesting help is prohibited! We learn together!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 7/14")
        embedrules8 = discord.Embed(color=self.color, timestamp=self.time, name="Number 5:", value="No Spamming! This includes but is not limited to: Over posting asking the same question over and over without showing progress or understanding using the @ ability when there are sufficient support channels for your needs", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 8/14")
        embedrules9 = discord.Embed(color=self.color, timestamp=self.time, name="Number 6:", value="We have members of all ages that are welcome into this discord. No Cursing: NSFW: etc! It is prohibited!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 9/14")
        embedrules10 = discord.Embed(color=self.color, timestamp=self.time, name="Number 7:", value="Keep the chats in accordance with the channels topic. If you're not sure read the top of the channel window or ask", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 10/14")
        embedrules11 = discord.Embed(color=self.color, timestamp=self.time, name="Number 8:", value="No Intimidation! We grow and learn together from day one and on!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 11/14")
        embedrules12 = discord.Embed(color=self.color, timestamp=self.time, name="Number 9:", value="Use the proper markups when submitting code. Discord supports many languages!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 12/14")
        embedrules13 = discord.Embed(color=self.color, timestamp=self.time, name="Number 10:", value="Do not create your own invite to this discord. An invite link has already been created for you to use. Type `>binbite` for the link", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 13/14")
        embedrules14 = discord.Embed(color=self.color, timestamp=self.time, name="**Disclaimer**:", value="These rules are subject to change at any time and will be posted to the announcements channel. This pyramid is at the staff discression as to the punishment they seem fit. You always have the right to appeal!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 14/14")
        
        embeds =[embedrules1, embedrules2, embedrules3, embedrules4, embedrules5, embedrules6, embedrules7, embedrules8, embedrules9, embedrules10, embedrules11, embedrules12, embedrules13, embedrules14]

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        await paginator.run(embeds)


def setup(bot):
    bot.add_cog(Rules(bot))