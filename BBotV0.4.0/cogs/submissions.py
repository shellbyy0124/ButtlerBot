import discord
import json
import random
import datetime
import asyncio

from discord.ext import commands
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

LT = data["guild"]["LT"]
code_submissions = data["channels"]["code_submissions"]

class Submissions(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.url = self.bot.user.avatar_url
        self.color = random.randint(0, 0xFFFFFF)
        self.time = datetime.datetime.utcnow()

    @commands.command()
    async def submit(self, ctx):
        
        def check(m):
            return ctx.author == m.author

        embed1 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Code Submission Editor", description="Who is your code being submitted to?", inline=False).set_thumbnail(url=self.url)
        msg1 = await ctx.send(embed=embed1)
        ans1 = await self.bot.wait_for('message', check=check)
        member = self.bot.get_id(ans1.content)

        members = []
        
        for m in ctx.guild.members:
            if not m.bot:
                members.append(', '.join(m))

        if member == members:

            embed2 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Code Submission Editor", description=f"**__Submission For:__**\n{member.name}\nWhat is your submissions? Remember, you may only submit code into the {LT.name} discord using any of the links on the `>bpaste` command!", inline=False).set_thumbnail(url=self.url)
            await msg1.edit(embed=embed2)
            ans2 = await self.bot.wait_for('message', check=check)

            if all(i.isurl() for i in ans2.content):
                
                embed3 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Code Submission Editor", description=f"**__Submission For:__**\n{member.name}\n**__Submission:__**\n{ans2.content}\nIf you are satisfied with your entries, then type `!save`. If not, then type `!exit`.", inline=False).set_thumbnail(url=self.url)
                await msg1.edit(embed=embed3)
                ans3 = await self.bot.wait_for('message', check=check)

                if ans3.content == "!save":

                    await ctx.message.delete()
                    await msg1.delete()
                    await ans1.delete()
                    await ans2.delete()
                    await ans3.delete()

                    final_embed = discord.Embed(color=self.color, timestamp=self.time, title=f"**__SUBMISSION INCOMING FROM {ctx.author.mention}__**", description=f"**__Submission For:__**\n{member.mention}\n**__Submission:__**\n{ans2.content}", inline=False).set_thumbnail(url=ctx.author.avatar_url)
                    channel = self.bot.get_channel(code_submissions)
                    a = await channel.send(embed=final_embed)
                    await a.pin()
                
                elif ans3.content == "!exit":

                    await ctx.message.delete()
                    await msg1.delete()
                    await ans1.delete()
                    await ans2.delete()
                    await ans3.delete()

                    a = await ctx.send("Please restart the command to correct any entries")
                    await asyncio.sleep(15)
                    await a.delete()

                else:

                    a = await ctx.send("Please take a screenshot of the steps you've gone through, and post that screen shot in the support channels for further assistance")
                    await asyncio.sleep(60)
                    await a.delete()

            else:
                await ctx.message.delete()
                await msg1.delete()
                await ans1.delete()
                await ans2.delete()

                a = await ctx.send("That is not a url. please type the command again to start over")
                await asyncio.sleep(15)
                await a.delete()

        else:

            await ctx.message.delete()
            await msg1.delete()
            await ans1.delete()

            a = await ctx.send("That name is not a member within this discord. Please run the command again!")
            await asyncio.sleep(15)
            await a.delete()

def setup(bot):
    bot.add_cog(Submissions(bot))