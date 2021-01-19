import discord
import json
import os
import datetime
import asyncio
import random

from os import error
from discord.ext import commands
from discord.ext.commands import cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

BOTOUTPUT = data["channels"]["bot_spam"]
team_code_submissions = data["channels"]["team_code_submissions"]
discord_suggestions = data["channels"]["discord_suggestions"]
bot_suggestions = data["channels"]["bot_suggestions"]
bot_spam = data["channels"]["bot_spam"]
suggestions = data["channels"]["suggestions"]
bots_added = data["channels"]["bots_added"]
botbugs = data["channels"]["botbugs"]
challenge_updates = data["channels"]["challenge_updates"]

class GeneralCommands(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.color = random.randint(0, 0xFFFFFF)
        self.time = datetime.datetime.utcnow()
        self.bot = self.bot.user.avatar_url
        self.channel = self.bot.get_channel(challenge_updates)

    @commands.command()
    async def btsubmit(self, ctx, *, message):
        
        await ctx.message.delete()
        submitembed1 = discord.Embed(color=self.color, timestamp=self.time, title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted Code**: {message}", inline=False)
        submitembed1.set_thumbnail(url=ctx.author.avatar_url)
        channel = self.bot.get_channel(team_code_submissions)
        await channel.send(embed=submitembed1)
        
    @commands.command()
    async def bdsubmit(self, ctx, *, message):
        
        await ctx.message.delete()
        submitembed2 = discord.Embed(color=self.color, timestamp=self.time, title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted A Suggestion For The Discord:** {message}", inline=False)
        submitembed2.set_thumbnail(url=ctx.author.avatar_url)
        channel=self.bot.get_channel(discord_suggestions)
        await channel.send(embed=submitembed2)

    @commands.command()
    async def bbsubmit(self, ctx, *, message):
        
        await ctx.message.delete()
        submitembed3 = discord.Embed(color=self.color, timestamp=self.time, title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted A Suggestion For Bots:** {message}", inline=False)
        submitembed3.set_thumbnail(url=ctx.author.avatar_url)
        channel = self.bot.get_channel(bot_suggestions)
        await channel.send(embed=submitembed3)

    @commands.command()
    async def bpaste(self, ctx):

        await ctx.message.delete()
        paste1 = discord.Embed(color=self.color, timestamp=self.time, title="When Posting Code In {ctx.guild.name}!**", description=f"Please use [Pastebin](https://pastebin.com/), [hastebin for Python](https://paste.pythondiscord.com/), or [mystb.in](https://mystb.in/)")
        msg = await ctx.send(embed=paste1)
        await asyncio.sleep(10)
        await msg.delete()

    @commands.command()
    async def bblist(self, ctx):

        await ctx.message.delete()    
        bots = []
        for m in ctx.guild.members:
            if m.bot:
                bots.append(m.name)
        botlist = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot's Companions:", description=f'{", ".join(bots)}')
        botlist.set_thumbnail(url=self.bot.user.avatar_url)
        botlist.timestamp = datetime.datetime.now()
        msg = await ctx.send(embed=botlist)
        await asyncio.sleep(10)
        await msg.delete()

    @commands.command()
    async def bping(self, ctx):
        
        await ctx.message.delete()
        await ctx.send(f'Pong! _takes a deep breath_ PHEW! That took: {self.bot.latency*1000}ms')


    @commands.command()
    async def binvite(self, ctx):
        
        await ctx.message.delete()
        inv = discord.Embed(color=self.color, timestamp=self.time, title=f"Inviting Your Friends:", description=f"Any and Everyone of ages 13+ are allowed to join our discord. Please do not create your own invite link, as you can use [this one](https://discord.gg/DEzK4vStfC)")
        inv.add_field(name="Discord Support Server:", value="To obtain all updates, and to receive support with Buttler Bot, please join us at our [support server](https://discord.gg/w2AjHF6Nra)")
        inv.set_thumbnail(url=self.bot.user.avatar_url)
        inv.set_footer(text=datetime.datetime.now())
        msg = await ctx.send(embed=inv)
        await asyncio.sleep(30)
        await msg.delete()

    @commands.command()
    async def bbadlist(self, ctx, message):

        await ctx.message.delete()
        member = ctx.author.name
        message = message
        bls = discord.Embed(color=self.color, timestamp=self.time, title=f"Bad List Suggestion From {member}", description=f"{message}")
        channel = self.bot.get_channel(suggestions)
        await channel.send(embed=bls)


    @commands.command()
    async def bbug(self, ctx):

        await ctx.message.delete()

        bug1 = discord.Embed(color=self.color, timestamp=self.time, title="Please Enter The Name Of The Bot")
        send1 = await ctx.send(embed=bug1)
        ans1 = await self.bot.wait_for('message')

        if all(i.isprintable() for i in ans1.content):

            bug2 = discord.Embed(color=self.color, timestamp=self.time, title="Please Enter The Issue:")
            await send1.edit(embed=bug2)
            ans2 = await self.bot.wait_for('message')

            if all(x.isprintable() for x in ans2.content):

                bug3 = discord.Embed(color=self.color, timestamp=self.time, title="Please enter anymore details about the bot that you feel are needed")
                await send1.edit(embed=bug3)
                ans3 = await self.bot.wait_for('message')

                if all(i.isprintable() for i in ans3.content):

                    await send1.delete()
                    await ans1.delete()
                    await ans2.delete()
                    await ans3.delete()

                    finale = discord.Embed(color=self.color, timestamp=self.time, title=f"{ans1.content}")
                    finale.add_field(name="\u200b", value=f"__{ans2.content}:__")
                    finale.add_field(name="\u200b", value=f"```{ans3.content}```")
                    finale.timestamp = datetime.datetime.utcnow()       

                    channel = self.bot.get_channel(botbugs)
                    await channel.send(embed=finale)

    @commands.command()
    async def think(self, ctx):

        await ctx.message.delete()
        think = discord.Embed(color=self.color, timestamp=self.time, title="Did you think before you spoke?", description="""**__T – TRUE:__**\nIs what you are saying actually true, or is it ‘fake news’? Lies and misinformation hurt others and reflect the liar as someone untrustworthy.
                                                                                                                             **__H – HELPFUL:__**\nAre your words helpful? Assisting others to make better decisions through offering good advice is also important.
                                                                                                                             **__I – INSPIRING:__**\nAre others inspired by what you are saying? People are greatly inspired by words which have the influence to prompt others to do amazing things.
                                                                                                                             **__N – NECESSARY:__**\nDo your words really need to be said? Useless chatter is annoying, while language that actively hurts others is wholly unnecessary.
                                                                                                                             **__K – KIND__**\nIs what you want to say kind? We all know the saying “if you don’t have anything nice to say, say nothing at all
                                                                                                                             Unkind sentences obviously have the power to hurt people, so please, THINK before you speak!""")

        file = discord.File("/home/shellbyy/Desktop/repofolder/discord_bots/ButtlerBot/BBotV0.2.2/bot_images/ThinkBeforeYouSpeak.png", filename="ThinkBeforeYouSpeak.png")
        think.set_thumbnail(url="attachment://ThinkBeforeYouSpeak.png")
        await ctx.send(embed=think, file=file)

    @commands.command()
    async def bsupport(self, ctx):

        await ctx.message.delete()

        category = discord.utils.get(ctx.guild.categories, name='Save_Us')
        channel = await ctx.guild.create_text_channel(ctx.author.name, category=category)

        embed1 = discord.Embed(color=discord.Colour.blue(), timestamp=self.time, title=f"Welcome To Your Help Channel, {ctx.author.name}", description=f"Please type a brief description, and your code your having problems with and someone will be with you soon :)")
        msg1 = await channel.send(embed=embed1)
        ans = await self.bot.wait_for('message')

        if all(x.isprintable() for x in ans.content):
            await ans.delete()
            embed2 = discord.Embed(color=self.color, timestamp=self.time, title=f"{ctx.author.name}", description=f"{ans.content}")
            await msg1.edit(embed=embed2)
            await msg1.pin()
            await channel.purge(limit=1)

    @commands.command(aliases=['buplist'])
    @commands.has_any_role("Owner", "Head Dev", "Dev")
    async def updatechallengelist(self, ctx):

        def check(m):
            return m.author.id == ctx.author.id

        await ctx.message.delete()
        note = "After 60 seconds, the bot will time out waiting for your response"

        embed1 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Challenge-List Suggestions Editor", description="Hi! Welcome to the setup editor for bring your ideas to us! Let me know when you're ready by typing ready :)", inline=False).set_footer(url=self.bot).set_footer(text=note)
        msg1 = await ctx.send(embed=embed1)
        ans1 = self.bot.wait_for('message', check=check, timeout=60)

        if ans1.content.lower() == "ready":
            
            await ans1.delete()
            embed2 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Challenge-List Suggestions Editor", description="1) What is the name of your challenge?", inline=False).set_footer(url=self.bot).set_footer(text=note)
            await msg1.edit(embed=embed2)
            ans2 = await self.bot.wait_for('message', check=check, timeout=60)

            if all(i.isprintable() for i in ans2.content):
                
                await ans2.delete()
                embed3 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Challenge-List Suggestions Editor", description="2) What language is the challenge writte in? Remember: __We only support Java, JavaScript, C#, Python, and HTML", inline=False).set_footer(url=self.bot).set_footer(text=note)
                await msg1.edit(embed=embed3)
                ans3 = await self.bot.wait_for('message', check=check, timeout=60)

                if all(i.isprintable() for i in ans3.content):
                    
                    await ans3.delete()
                    embed4 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Challenge-List Suggestions Editor", description="3) What is your challenge?", inline=False).set_footer(url=self.bot).set_footer(text=note)
                    await msg1.edit(embed=embed4)
                    ans4 = await self.bot.wait_for('message', check=check, timeout=60)

                    if all(i.isprintable() for i in ans4.content):

                        await ans4.delete()
                        embed5 = discord.Embed(color=self.color, timestamp=self.time, title="Final Result", description="**__Challenge Name:__**\n{ans1.content}\n**__Challenge Language:__**\n{ans2.content}\n**__Challenge Details:__**\n{ans3.content}\n\n**__If you are satisfied with your entry, type save. Otherwise, type start over, and re-run the command__**", inline=False).set_footer(url=self.bot).set_footer(text=note)
                        await msg1.edit(embed=embed5)
                        ans5 = await self.bot.wait_for('message', check=check, timeout=60)

                        if ans5.content.lower() == "save":
                            
                            await ans5.delete()
                            await self.channel.send(embed=embed5)
                            
                        elif ans5.content.lower() == "start over":

                            await ans5.delete()
                            await ctx.send("Please type the command again to start over :)")

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
    bot.add_cog(GeneralCommands(bot))