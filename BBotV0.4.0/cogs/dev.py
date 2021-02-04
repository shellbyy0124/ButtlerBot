import discord
import DiscordUtils
import datetime
import random

from discord.ext import commands
from discord.ext.commands import Cog 



class Dev(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.time = datetime.datetime.utcnow()
        self.color = random.randint(0, 0xFFFFFF)

    @commands.command()
    async def brules(self, ctx):

        embedrules1 = discord.Embed(color=self.color, timestamp=self.time, title="Welcome To The Learning Together Community Discord!", description=f"Welcome To The {ctx.guild.name} discord! Here at {ctx.guild.name}, We strive to help those who want to learn about programming, what it is/what it does, and how to utilize its' abilities to the best of our knoweldge. In the following pages, you will find the guidelines for residing within our community. Remember, we are all friends here! If you're looking for a specific rule, then please type `>brules <page_number>` and it'll pull it right on up!",inline=False).set_thumbnail(url=self.url).set_footer(text="Page 1/14")
        embedrules2 = discord.Embed(color=self.color, timestamp=self.time, name="**___These rules are to be followed at all times!___**", value="Page 1: Welcome\nPage 2: Table Of Contents\nPage 3: Discipline Tier\nPage 4:Respect\nPage 5: Bullying\nPage 6: Learning\nPage 7: Rudeness.Disrespect\nPage 8: Spamming\nPage 9: NSFW\nPage 10: Channel Topics\nPage 11: Intimidation\nPage 12: Mark-Ups\nPage 13: Discord Invites\nPage 14: Disclaimer", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 2/14")
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

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Dev')
    async def faq(self, ctx):

        await ctx.message.delete()

        faq1 = discord.Embed(color=self.color, timestamp=self.time, title="FAQ's").set_thumbnail(url=self.url)
        faq2 = discord.Embed(color=self.color, timestamp=self.time, title="Why are there no active bots in the server except buttler?", description="We are in the very beginning stages of creating this community, and the bots that are used within it. We are building custom bots from scratch for our community, and to match what our community is about. Please bare with us as we are working diligently to get this community started, and rocketed off to the moon!", inline=False)
        faq3 = discord.Embed(color=self.color, timestamp=self.time, title="What do I do if I would like to submit an idea for a bot?", description="Please submit your ideas for bots by using `>bbsubmit <idea>` to send your submission to our lovely developers!", inline=False)
        faq4 = discord.Embed(color=self.color, timestamp=self.time, title="Where can I find beginner resources for Python?", description="You can venture over to the _**Resources**_ category where you can find different channels containing various links for all types of information. You're also welcome to post your own links for others to use as well, however, please stick to the rules when doing so!", inline=False)
        faq5 = discord.Embed(color=self.color, timestamp=self.time, title="How often can I get a coding challenge?", description="Coding Challenges are setup on a 24 hour timer. There is no command to receive a challenge. They will be posted in the **__Coding Challenges__** category as they are sent out.", inline=False)
        faq6 = discord.Embed(color=self.color, timestamp=self.time, title="How does the ranking system work?", description="Kastien is currently developing that system, and thus at this time we have no information. It is still a product in progress :penguin:", inline=False)
        faq7 = discord.Embed(color=self.color, timestamp=self.time, title="How do I need to post my code in the community?", description="Please use the backticks before and after your code when posting. If you're unsure of what a backtick is, it's the key underneath your ESC key and next to your `1` key on your keyboared.", inline=False)
        
        faqs = [faq1, faq2, faq3, faq4, faq5, faq6, faq7]

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        await paginator.run(faqs)

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev')
    async def binfo(self, ctx):

        note1 = "This message will self-destruct after 300 seconds"
        
        buttler = discord.Embed(color=self.color, timestamp=self.time, title="Hi! Welcome To The ButtlerBot Introduction!", description="Table Of Contents:\n1) Introduction\n2) What I Can Do\n3) General Commands\n 4) Staff Commands\n5) Dev Commands", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)
        buttler1 = discord.Embed(color=self.color, timestamp=self.time, title="Introduction", description="ButtlerBot was created just before Christmas of 2020.", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)
        buttler2 = discord.Embed(color=self.color, timestamp=self.time, title="What I Can Do", description="As of now, ButtlerBot can run several moderation commands, as well as, he can send a list of your discords rules to new members who join, play mini-games, send automated messages, and so much more!", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)
        buttler3 = discord.Embed(color=self.color, timestamp=self.time, title="General Commands", description="bprefix - bflip - btsubmit - bdsubmit - bbsubmit - bpaste\nbblist - binvite - bbadlist - bbug - think - bsupport\nbhelp - bcprofile - brules - bsapp", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)
        buttler4 = discord.Embed(color=self.color, timestamp=self.time, title="Staff Commands", description="bbotcommynity - bstats - bcnick - bwhois - bwarn - btempmute\nbpromotion - bteam - bping", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)
        buttler5 = discord.Embed(color=self.color, timestamp=self.time, title="Dev Commands", description="buplist - addingbots - bpurge - blistall - blistmem\nblistroles - bbotupdates - block - bunlock", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)
        buttler6 = discord.Embed(color=self.color, timestamp=self.time, title="Moderation", description="I have commands that the staff can use to warn and tempmute members when they're not following the rules", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)
        buttler7 = discord.Embed(color=self.color, timestamp=self.time, title="The Creators", description="**__Founders:__**\nMekasu\nKastien\n**__Team Members:__**\nKortaPo", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)

        paginator = DU.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        embeds21 = [buttler, buttler1, buttler2, buttler3, buttler4, buttler5, buttler6, buttler7]
        await paginator.run(embeds21)

def setup(bot):
    bot.add_cog(Dev(bot))