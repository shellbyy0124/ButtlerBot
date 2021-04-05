import discord
import json
import random
import datetime
import asyncio

from discord.ext import commands
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

lottery_winner = data["channels"]["lottery_winner"]
lottery_entry = data["channels"]["lottery_entry"]

class General(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.color = random.randint(0, 0xFFFFFF)
        self.time = datetime.datetime.utcnow()
        self.url = self.bot.user.avatar_url

    @commands.command()
    async def bpaste(self, ctx):

        await ctx.message.delete()

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

        embed1 = discord.Embed(color=self.color, timestamp=self.time, title=f"When Posting Code In The {ctx.guild.name} community", description=f"Please use [Pastebin](https://pastebin.com/), [hastebin for Python](https://paste.pythondiscord.com/), or [mystb.in](https://mystb.in/)").set_thumbnail(url=self.url)
        msg1 = await ctx.send(embed=embed1)
        await asyncio.sleep(30)
        await msg1.delete()

    @commands.command()
    async def bblist(self, ctx):

        await ctx.message.delete()

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

        bots = []

        for member in ctx.guild.members:
            if member.bot:
                bots.append(member.name)
        botlist = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBots Companions:", description=f"{', '.join(bots)}").set_thumbnail(url=self.url)
        msg1 = await ctx.send(embed=botlist)
        await asyncio.sleep(30)
        await msg1.delete()

    @commands.command()
    async def bping(self, ctx):
        
        await ctx.message.delete()

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

        await ctx.send(f'Pong! _takes a deep breath_ PHEW! That took: {round(self.bot.latency*1000)}ms')
        a =await asyncio.sleep(10)
        await a.delete()


    @commands.command()
    async def binvite(self, ctx):
        
        await ctx.message.delete()

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

        inv = discord.Embed(color=self.color, timestamp=self.time, title=f"Inviting Your Friends:", description=f"Any and Everyone of ages 13+ are allowed to join our discord. Please do not create your own invite link, as you can use [this one](https://discord.gg/DEzK4vStfC)").set_thumbnail(url=self.url)
        inv.add_field(name="Discord Support Server:", value="To obtain all updates, and to receive support with Buttler Bot, please join us at our [support server]()").set_thumbnail(url=self.url)
        msg = await ctx.send(embed=inv)
        await asyncio.sleep(30)
        await msg.delete()

    @commands.command()
    async def think(self, ctx):

        await ctx.message.delete()

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

        think = discord.Embed(color=self.color, timestamp=self.time, title="Did you think before you spoke?", description="""**__T – TRUE:__**\nIs what you are saying actually true, or is it ‘fake news’? Lies and misinformation hurt others and reflect the liar as someone untrustworthy.
                                                                                                                             **__H – HELPFUL:__**\nAre your words helpful? Assisting others to make better decisions through offering good advice is also important.
                                                                                                                             **__I – INSPIRING:__**\nAre others inspired by what you are saying? People are greatly inspired by words which have the influence to prompt others to do amazing things.
                                                                                                                             **__N – NECESSARY:__**\nDo your words really need to be said? Useless chatter is annoying, while language that actively hurts others is wholly unnecessary.
                                                                                                                             **__K – KIND__**\nIs what you want to say kind? We all know the saying “if you don’t have anything nice to say, say nothing at all
                                                                                                                             Unkind sentences obviously have the power to hurt people, so please, THINK before you speak!""")

        file = discord.File("/root/discord_bots/ButtlerBot/BBotV0.4.0/bot_images/ThinkBeforeYouSpeak.png", filename="ThinkBeforeYouSpeak.png")
        think.set_thumbnail(url="attachment://ThinkBeforeYouSpeak.png")
        await ctx.send(embed=think, file=file)


    @commands.command()
    async def bsupport(self, ctx):

        await ctx.message.delete()

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

        category = discord.utils.get(ctx.guild.categories, name='Occupied_Support_Channels')
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

    @commands.command(aliases=["bwhois"])
    @commands.has_any_role('Owner', 'Head Dev', 'dev', 'Head Admin', 'Admins', 'Moderators', 'Community Helpers')
    async def whois(self, ctx, user:discord.Member=None):

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

        with open('./users.json', 'r', encoding='utf-8-sig') as p:
            data = json.load(p)

        stuff = data["users"][ctx.author.name]["bank"]
        
        user = user or ctx.author
        if user is None:
            user = ctx.message.author
        if user.activity is not None:
            game = user.activity.name
        else:
            game = None
        voice_state = None if not user.voice else user.voice.channel
        embed1 = discord.Embed(timestamp=ctx.message.created_at, color=self.color)
        embed1.add_field(name='User ID', value=user.id, inline=True)
        embed1.add_field(name='Nick', value=user.nick, inline=True)
        embed1.add_field(name='Status', value=user.status, inline=True)
        embed1.add_field(name='On Mobile', value=user.is_on_mobile(), inline=True)
        embed1.add_field(name='In Voice', value=voice_state, inline=True)
        embed1.add_field(name='Highest Role', value=user.top_role.name, inline=True)
        embed1.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        embed1.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        embed1.add_field(name="Balance:", value=f"{stuff}")
        embed1.set_thumbnail(url=user.avatar_url)
        embed1.set_author(name=user.name, icon_url=user.avatar_url)
        embed1.set_footer(text="ButtlerBot")
        await ctx.send(embed=embed1)

    @commands.command()
    async def addnumber(self, ctx):

        async with ctx.typing():

            num = random.randint(0, 5)

            await asyncio.sleep(num)

        await ctx.message.delete()

        channel_check = self.bot.get_channel(lottery_entry)
        lottery_ann = self.bot.get_channel(lottery_winner)

        if ctx.message.channel == channel_check:

            number = random.choice(0, 1000)

            with open('./lottery.json', 'r', encoding='utf-8-sig') as old:
                data = json.load(old)

            data["ticket_numbers"] = {"member_name" : str(ctx.author.name), "ticket_number" : str(number)}

            with open('./lottery.json', 'w', encoding='utf-8-sig') as new:
                data = json.dump(data, new, indent=4)

            embed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title=f"{ctx.author.mention} Has Entered The Lottery!", description=f"{ctx.author.name} you have placed your entry into the lottery! Your ticket number is {number}. The lottery will be drawn in **(need timer inserted here)**", inline=False).set_thumbnail(url=self.bot.user.avatar_url)
            a = await lottery_ann.send(embed=embed1)
            await a.pin()
            await lottery_ann.purge(limit=1)

        else:

            a = await ctx.send(f"**__You are in the wrong channel. Please go to the {channel_check.mention} channel to enter the lottery!__**")
            await asyncio.sleep(10)
            await a.delete()

def setup(bot):
    bot.add_cog(General(bot))