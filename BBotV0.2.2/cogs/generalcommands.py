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

class GeneralCommands(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['btsubmit'])
    async def submitteamcode(self, ctx, *, message):
        await ctx.message.delete()
        submitembed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=datetime.datetime.utcnow(), title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted Code**: {message}", inline=False)
        submitembed1.set_thumbnail(url=ctx.author.avatar_url)
        channel = self.bot.get_channel(team_code_submissions)
        await channel.send(embed=submitembed1)
        
    @commands.command(aliases=['bdsubmit'])
    async def submitdiscordsuggestions(self, ctx, *, message):
        submitembed2 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=datetime.datetime.utcnow(), title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted A Suggestion For The Discord:** {message}", inline=False)
        submitembed2.set_thumbnail(url=ctx.author.avatar_url)
        channel=self.bot.get_channel(discord_suggestions)
        await channel.send(embed=submitembed2)

    @commands.command(aliases=['bbsubmit'])
    async def submitbotsuggestions(self, ctx, *, message):
        submitembed3 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=datetime.datetime.utcnow(), title=f'{ctx.author.name}').add_field(name="\u200b", value=f"**Has Submitted A Suggestion For Bots:** {message}", inline=False)
        submitembed3.set_thumbnail(url=ctx.author.avatar_url)
        channel = self.bot.get_channel(bot_suggestions)
        await channel.send(embed=submitembed3)

    @commands.command(aliases=['bpaste'])
    async def paste(self, ctx):

        await ctx.message.delete()

        paste1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=datetime.datetime.utcnow()).add_field(name=f"**When Posting Code In {ctx.guild.name}!**",
                                                                value=f"Please use [Pastebin](https://pastebin.com/), [hastebin for Python](https://paste.pythondiscord.com/), or [mystb.in](https://mystb.in/)")
        msg = await ctx.send(embed=paste1)
        await asyncio.sleep(10)
        await msg.delete()


    @commands.command(aliases=['bblist'])
    async def bbotlist(self, ctx):

        bots = []
        for m in ctx.guild.members:
            if m.bot:
                bots.append(m.name)
        botlist = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=datetime.datetime.utcnow(), title="ButtlerBot's Companions:", description=f'{", ".join(bots)}')
        botlist.set_thumbnail(url=self.bot.user.avatar_url)
        botlist.timestamp = datetime.datetime.now()
        msg = await ctx.send(embed=botlist)
        await asyncio.sleep(10)
        await msg.delete()


    @commands.command(aliases=['bbupdates'])
    async def botupdates(self, ctx):

        await ctx.send("Hobo :panda_face:")

    @commands.command(aliases=['bping'])
    async def ping(self, ctx):

        await ctx.send(f'Pong! _takes a deep breath_ PHEW! That took: {self.bot.latency*1000}ms')


    @commands.command(aliases=['binvite'])
    async def invitation(self, ctx):
        
        inv = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=datetime.datetime.utcnow(), title=f"Inviting Your Friends:", description=f"Any and Everyone of ages 13+ are allowed to join our discord. Please do not create your own invite link, as you can use [this one](https://discord.gg/DEzK4vStfC)")
        inv.add_field(name="Discord Support Server:", value="To obtain all updates, and to receive support with Buttler Bot, please join us at our [support server](https://discord.gg/w2AjHF6Nra)")
        inv.set_thumbnail(url=self.bot.user.avatar_url)
        inv.set_footer(text=datetime.datetime.now())
        msg = await ctx.send(embed=inv)
        await asyncio.sleep(30)
        await msg.delete()

    @commands.command(aliases=['bbadlist'])
    async def badlistsuggestion(self, ctx, message):

        member = ctx.author.name
        message = message
        bls = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=datetime.datetime.utcnow(), title=f"Bad List Suggestion From {member}", description=f"{message}")
        channel = self.bot.get_channel(suggestions)
        await channel.send(embed=bls)


    @commands.command()
    async def bbug(self, ctx):

        await ctx.message.delete()

        bug1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=datetime.datetime.utcnow(), title="Please Enter The Name Of The Bot")
        send1 = await ctx.send(embed=bug1)
        ans1 = await self.bot.wait_for('message')

        if all(i.isprintable() for i in ans1.content):

            bug2 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=datetime.datetime.utcnow(), title="Please Enter The Issue:")
            await send1.edit(embed=bug2)
            ans2 = await self.bot.wait_for('message')

            if all(x.isprintable() for x in ans2.content):

                bug3 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=datetime.datetime.utcnow(), title="Please enter anymore details about the bot that you feel are needed")
                await send1.edit(embed=bug3)
                ans3 = await self.bot.wait_for('message')

                if all(i.isprintable() for i in ans3.content):

                    await send1.delete()
                    await ans1.delete()
                    await ans2.delete()
                    await ans3.delete()

                    finale = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=datetime.datetime.utcnow(), title=f"{ans1.content}")
                    finale.add_field(name="\u200b", value=f"__{ans2.content}:__")
                    finale.add_field(name="\u200b", value=f"```{ans3.content}```")
                    finale.timestamp = datetime.datetime.utcnow()       

                    channel = self.bot.get_channel(botbugs)
                    await channel.send(embed=finale)

    @commands.command()
    async def think(self, ctx):

        color = random.randint(0, 0xFFFFFF)
        time = datetime.datetime.utcnow()

        think = discord.Embed(color=color, timestamp=time, title="Did you think before you spoke?", description="""**__T – TRUE:__**\nIs what you are saying actually true, or is it ‘fake news’? Lies and misinformation hurt others and reflect the liar as someone untrustworthy.
                                                                                                                   **__H – HELPFUL:__**\nAre your words helpful? Assisting others to make better decisions through offering good advice is also important.
                                                                                                                   **__I – INSPIRING:__**\nAre others inspired by what you are saying? People are greatly inspired by words which have the influence to prompt others to do amazing things.
                                                                                                                   **__N – NECESSARY:__**\nDo your words really need to be said? Useless chatter is annoying, while language that actively hurts others is wholly unnecessary.
                                                                                                                   **__K – KIND__**\nIs what you want to say kind? We all know the saying “if you don’t have anything nice to say, say nothing at all
                                                                                                                   Unkind sentences obviously have the power to hurt people, so please, THINK before you speak!""")

        file = discord.File("/home/shellbyy/Desktop/repofolder/ButtlerBot/BBotV0.2.2/bot_images/ThinkBeforeYouSpeak.png", filename="ThinkBeforeYouSpeak.png")
        think.set_thumbnail(url="attachment://ThinkBeforeYouSpeak.png")
        await ctx.send(embed=think, file=file)

    @commands.command()
    async def bsupport(self, ctx):

        color = random.randint(0, 0xFFFFFF)
        time = datetime.datetime.utcnow()

        category = discord.utils.get(ctx.guild.categories, name='Save_Us')
        channel = await ctx.guild.create_text_channel(ctx.author.name, category=category)

        embed1 = discord.Embed(color=discord.Colour.blue(), title=f"Welcome To Your Help Channel, {ctx.author.name}", description=f"Please type a brief description, and your code your having problems with and someone will be with you soon :)")
        msg1 = await channel.send(embed=embed1)
        ans = await self.bot.wait_for('message')

        if all(x.isprintable() for x in ans.content):
            await ans.delete()
            embed2 = discord.Embed(color=color, timestamp=time, title=f"{ctx.author.name}", description=f"{ans.content}")
            await msg1.edit(embed=embed2)
            await msg1.pin()
            await channel.purge(limit=1)

def setup(bot):
    bot.add_cog(GeneralCommands(bot))