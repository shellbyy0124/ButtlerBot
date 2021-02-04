import discord
import random
import datetime
import json

from discord.ext import commands
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

staff_commands = data["channels"]["staff_commands"]

class Teams(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.url = self.bot.user.avatar_url
        self.color = random.randint(0, 0xFFFFFF)
        self.time = datetime.datetime.utcnow()

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Head Admins', 'Administrators')
    async def bteam(self, ctx):

        await ctx.message.delete()

        def check(m):
            return ctx.author == m.author

        if ctx.message.channel == staff_commands:

            embed1 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Teams Editor", description="What Is The Team Captains Member ID?", inline=False).set_thumbnail(url=self.url)
            msg1 = await ctx.send(embed=embed1)
            ans1 = await self.bot.wait_for('message', check=check)
            members = []

            for m in ctx.guild.members:
                if not m.bot:
                    members.append(', '.join(m.id))

            if int(ans1) == members:

                embed2 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Teams Editor", description=f"**__Team Captain:__**\n{int(ans1).name}\nWhat Is The Name Of The Team?", inline=False).set_thumbanil(url=self.url)
                await msg1.edit(embed=embed2)
                ans2 = await self.bot.wait_for('message', check=check)

                if all(i.isprintable() for i in ans2.content):

                    embed3 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Teams Editor", description=f"**__Team Captain:__**\n{int(ans1).name}\n**__Team Name:__**\n{ans2.content}")