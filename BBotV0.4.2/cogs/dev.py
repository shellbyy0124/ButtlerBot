import discord
import DiscordUtils
import datetime
import random
import os
import sys
import asyncio
import json
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from discord.ext import commands
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

rules = data["channels"]["rules"]

class Dev(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.time = datetime.datetime.utcnow()
        self.color = random.randint(0, 0xFFFFFF)
        self.url = self.bot.user.avatar_url

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Head Admin', 'Admins', 'Moderators', 'Community Helpers', 'Team Captain')
    async def brules(self, ctx):

        await ctx.message.delete()

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

        channel = self.bot.get_channel(rules)
        await channel.purge(limit=1)

        embedrules1 = discord.Embed(color=self.color, timestamp=self.time, title="Welcome To The Learning Together Community Discord!", description=f"Here at {ctx.guild.name}, We strive to help those who want to learn about programming, what it is/what it does, and how to utilize its' abilities to the best of our knoweldge. In the following pages, you will find the guidelines for residing within our community. Remember, we are all friends here! If you're looking for a specific rule, then please type `>rules <page_number>` and it'll pull it right on up!",inline=False).set_thumbnail(url=self.url).set_footer(text="Page 1/14")
        embedrules1.add_field(name="**___Table Of Contents:__**", value="Page 2: Table Of Contents\nPage 3: Discipline Tier\nPage 4:Respect\nPage 5: Bullying\nPage 6: Learning\nPage 7: Rudeness/Disrespect\nPage 8: Spamming\nPage 9: NSFW\nPage 10: Channel Topics\nPage 11: Intimidation\nPage 12: Mark-Ups\nPage 13: Discord Invites\nPage 14: Disclaimer", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 2/14")
        embedrules1.add_field(name="Below You Will See The Tiers Of Warnings", value=""":red_circle:__DISCIPLINE TIERS - MEMBERS__:red_circle:\n1st - 3rd offense -> 15/30/45 minute mutes\n4th - 6th offense -> 1/3/5 day mutes\n7th + offense will result in you being permanently banned\nIF YOU LEAVE THE DISCORD AFTER BEING PERMA-MUTED IN AN ATTEMPT TO RE-JOIN AND SKIP PAST VERIFICATION, DO UNDERSTAND THAT WE HAVE A SYSTEM SETUP TO AUTOMATICALLY BAN ANYONE WHO HAS THE PERMA-MUTE ROLE, AND LEAVES THE DISCORD\n:red_circle:DISCIPLINE TIERS - STAFF:red_circle:\n1st - 3rd offense -> 1/3/5 hour mutes\n4th+ offense -> immediate removal of staff position for 72 hours (3 days). Once You Have Reached This Point, You Are On Thin Ice. @QueenBeeShellbyy, and @yes will determine your staff positions, and withdraw thereof\n:star:Everyone will be held to a higher standard as this is a community with children in it. No one is above the rules, and no one will be treated like they're special. Staff members are held to a much higher standard as for they are 16 year of age, and older. No Exceptions!:star:""", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 3/14")
        embedrules1.add_field(name="Number 1:", value="Respect of your peers is a must at all times!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 4/14")
        embedrules1.add_field(name="Number 2:", value="Making someone feel inferior to your is prohibited!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 5/14")
        embedrules1.add_field(name="Number 3:", value="Telling someone that their question is stupid is prohibited. If you feel the person is not wanting to learn on purpose get with a staff member", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 6/14")
        embedrules1.add_field(name="Number 4:", value="Being rude or indencent because you assume that everyone should have a pre-exisiting level of knowledge of python before requesting help is prohibited! We learn together!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 7/14")
        embedrules1.add_field(name="Number 5:", value="No Spamming! This includes but is not limited to: Over posting asking the same question over and over without showing progress or understanding using the @ ability when there are sufficient support channels for your needs", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 8/14")
        embedrules1.add_field(name="Number 6:", value="We have members of all ages that are welcome into this discord. No Cursing: NSFW: etc! It is prohibited!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 9/14")
        embedrules1.add_field(name="Number 7:", value="Keep the chats in accordance with the channels topic. If you're not sure, read the top of the channel window or ask", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 10/14")
        embedrules1.add_field(name="Number 8:", value="No Intimidation! We grow and learn together from day one and on!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 11/14")
        embedrules1.add_field(name="Number 9:", value="Use the proper markups when submitting code. Discord supports many languages!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 12/14")
        embedrules1.add_field(name="Number 10:", value="Do not create your own invite to this discord. An invite link has already been created for you to use. Type `>binbite` for the link", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 13/14")
        embedrules1.add_field(name="**Disclaimer**:", value="These rules are subject to change at any time and will be posted to the announcements channel. This pyramid is at the staff discression as to the punishment they seem fit. You always have the right to appeal!", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 14/14")
        
        a = await channel.send(embed=embedrules1)
        await a.pin()
        await channel.purge(limit=1)

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Dev')
    async def faq(self, ctx):

        await ctx.message.delete()

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

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

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

        note1 = "This message will self-destruct after 300 seconds"
        
        buttler = discord.Embed(color=self.color, timestamp=self.time, title="Hi! Welcome To The ButtlerBot Introduction!", description="Table Of Contents:\n1) Introduction\n2) What I Can Do\n3) General Commands\n 4) Staff Commands\n5) Dev Commands", inline=False).set_thumbnail(url=self.url).set_footer(text=note1)
        buttler1 = discord.Embed(color=self.color, timestamp=self.time, title="Introduction", description="ButtlerBot was created just before Christmas of 2020.", inline=False).set_thumbnail(url=self.url).set_footer(text=note1)
        buttler2 = discord.Embed(color=self.color, timestamp=self.time, title="What I Can Do", description="As of now, ButtlerBot can run several moderation commands, as well as, he can send a list of your discords rules to new members who join, play mini-games, send automated messages, and so much more!", inline=False).set_thumbnail(url=self.url).set_footer(text=note1)
        buttler3 = discord.Embed(color=self.color, timestamp=self.time, title="General Commands", description="bprefix - bflip - btsubmit - bdsubmit - bbsubmit - bpaste\nbblist - binvite - bbadlist - bbug - think - bsupport\nbhelp - bcprofile - brules - bsapp", inline=False).set_thumbnail(url=self.url).set_footer(text=note1)
        buttler4 = discord.Embed(color=self.color, timestamp=self.time, title="Staff Commands", description="bbotcommynity - bstats - bcnick - bwhois - bwarn - btempmute\nbpromotion - bteam - bping", inline=False).set_thumbnail(url=self.url).set_footer(text=note1)
        buttler5 = discord.Embed(color=self.color, timestamp=self.time, title="Dev Commands", description="buplist - addingbots - bpurge - blistall - blistmem\nblistroles - bbotupdates - block - bunlock", inline=False).set_thumbnail(url=self.url).set_footer(text=note1)
        buttler6 = discord.Embed(color=self.color, timestamp=self.time, title="Moderation", description="I have commands that the staff can use to warn and tempmute members when they're not following the rules", inline=False).set_thumbnail(url=self.url).set_footer(text=note1)
        buttler7 = discord.Embed(color=self.color, timestamp=self.time, title="The Creators", description="**__Founders:__**\nMekasu\nKastien\n**__Team Members:__**\nKortaPo", inline=False).set_thumbnail(url=self.url).set_footer(text=note1)

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        embeds21 = [buttler, buttler1, buttler2, buttler3, buttler4, buttler5, buttler6, buttler7]
        await paginator.run(embeds21)

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev')
    async def nuke(self, ctx, channels: discord.TextChannel = None):

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

        if channels == None:
            await ctx.send('Mention the channel')
            return

        else:

            checkmsg = await ctx.send('Are you sure!')
            await ctx.send('Type in `yes`. To proceed')

            def check(m):
                user = ctx.author
                return m.author.id == user.id and m.content == 'yes'

            msg = await self.bot.wait_for('message', check=check)
            await ctx.channel.send('Theres no going back!\n**Are you sure.**')

            def check(m):
                user = ctx.author
                return m.author.id == user.id and m.content == 'yes'

            msg = await self.bot.wait_for('message', check=check)
            new = await channels.clone()
            await channels.delete()
            await new.send('https://media1.tenor.com/images/6c485efad8b910e5289fc7968ea1d22f/tenor.gif?itemid=5791468')
            await asyncio.sleep(2)
            await new.send(f'{self.bot.user.name} has cleared this channel!')

        with open('./master.json', 'r', encoding='utf-8-sig') as old:
            data = json.load(old)

        data["channels"] = {"bot_spam1" : str(new.id)}

        with open('./master.json', 'w', encoding='utf-8-sig') as new:
            data = json.dump(data, new, indent=4)


    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev')
    async def changeprefix(self, ctx):

        def check(m):
            return ctx.message.author.id == m.author.id

        await ctx.message.delete()

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

        embed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Prefix Editor", description="Please Enter Your Desired Prefix", inline=False).set_thumbnail(url=self.bot.user.avatar_url)
        msg = await ctx.send(embed=embed1)
        ans = await self.bot.wait_for('message', check=check)

        if all(i.isprintable() for i in ans.content):

            await ans.delete()

            embed2 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Prefix Editor", description=f"You Have Chosen `**__{ans.content}__**` as your new prefix. Are you sure you want to make this change? yes or now", inline=False).set_thumbnail(url=self.bot.user.avatar_url)
            await msg.edit(embed=embed2)
            ans2 = await self.bot.wait_for('message', check=check)

            if ans2.content.lower() == "yes":

                with open('./master.json', 'r', encoding='utf-8-sig') as old:
                    data = json.load(old)

                data["guild"]["command_prefix"] = ans.content

                with open('./master.json', 'w', encoding='utf-8-sig') as new:
                    data = json.dump(data, new, indent=4)

                embed3 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Prefix Editor", description=f"You have successfully set your new prefix to {ans.content}", inline=False).set_thumbnail(url=self.url)
                await msg.edit(embed=embed3)
                await asyncio.sleep(5)
                await msg.delete()

            elif ans2.content.lower() == "no":

                embed4 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Prefix Editor", description="Please enter your desired prefix, or type `!stop` to stop this command", inline=False).set_thumbnail(url=self.bot.user.avatar_url)
                await msg.edit(embed=embed4)
                ans3 = await self.bot.wait_for('message', check=check)

                if ans3.content.lower() != "!stop": 

                    embed5 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Prefix Editor", description=f"You entered {ans3.content} as your new prefix. Are you sure? yes or no", inline=False).set_thumbnail(url=self.bot.user.avatar_url)
                    await msg.edit(embed=embed4)
                    ans4 = await self.bot.wait_for('message', check=check)

                    if ans4.content.lower() == "yes":
                        
                        with open('./master.json', 'r', encoding='utf-8-sig') as old1:
                            data = json.load(old1)

                        data["guild"]["command_prefix"] = ans.content

                        with open('./master.json', 'w', encoding='utf-8-sig') as new1:
                            data = json.dump(data, new1, indent=4)
                        
                        embed6 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Prefix Editor", description=f"You have successfully set your new prefix to {ans3.content}", inline=False).set_thumbnail(url=self.bot.user.avatar_url)
                        await msg.edit(embed=embed6)
                        await asyncio.sleep(5)
                        await msg.delete()
        else:
            await ctx.send("nope. . . . .")

def setup(bot):
    bot.add_cog(Dev(bot))