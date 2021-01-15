import discord
import json
import random
import datetime
import asyncio

from discord.ext import commands
from discord.ext.commands import Cog
from os import error

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data=json.load(f)

bot_updates = data["channels"]["bot_updates"]
community_updates = data["channels"]["community_updates"]
bots_added = data["channels"]["bots_added"]
staff_commands = data["channels"]["staff_commands"]    
    
    
class Devs(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.color = random.randint(0, 0xFFFFFF)
        self.time = datetime.datetime.utcnow()
        self.url = self.bot.user.avatar_url 
        self.channel1 = self.bot.get_channel(staff_commands)
        self.channel2 = self.bot.get_channel(bot_updates)
        self.channel3 = self.bot.get_channel(bots_added)
    
    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev')
    async def bbotupdates(self, ctx):
    
        def check(m):
            return m.author == ctx.author


        embed1 = discord.Embed(color=self.color, timestamp=self.time, title="Welcome To The ButtlerBot Announcement Editor!", description="Please Use This Template To Fill Out Your Announcement For Any Updates To Our Bots:\n```\nBot Name:\nBot Owner:\nBot Updates:\nIn this category you are free to use what emoji's, etc. that you would like to use. You can be as creative as you want to be so long as you show bot update notes in some form\n```", inline=False).set_footer(text="Enter `ready` when you're ready to begin.")
        
        if ctx.channel == self.channel1:
            await ctx.message.delete()
            msg1 = await ctx.channel.send(embed=embed1)
            ans1 = await self.bot.wait_for('message', check=check)
            embed2 = discord.Embed(color=self.color, timestamp=self.time, title="What's The Name Of The Announcement?")

            if ans1.content.lower() == "ready":
                await ans1.delete()
                await msg1.edit(embed=embed2)
                ans2 = await self.bot.wait_for('message', check=check)
                embed3 = discord.Embed(color=self.color, timestamp=self.time, title=f"What's The Name Of The Announcement?\n{ans2.content}", description="**__What's The Name Of The Bot?__**", inline=False)
               
                if all(i.isprintable() for i in ans2.content):
                    await ans2.delete()
                    await msg1.edit(embed=embed3)
                    ans3 = await self.bot.wait_for('message', check=check)
                    embed4 = discord.Embed(color=self.color, timestamp=self.time, title=f"What's The Name Of The Announcement?\n{ans2.content}", description=f"**__What's The Name Of The Bot?__**\n{ans3.content}\n**__Who's The Bot Owner?__**", inline=False)
                
                    if all(i.isprintable() for i in ans3.content):
                        await ans3.delete()
                        await msg1.edit(embed=embed4)
                        ans4 = await self.bot.wait_for('message', check=check)
                        embed5 = discord.Embed(color=self.color, timestamp=self.time, titel=f"What's The Name Of The Announcement?\n{ans2.content}", description=f"**__What's The Name Of The Bot?__**\n{ans3.content}\n**__Who's The Bot Owner?__**\n{ans4.content}\n**__What Are Your Update Notes?__**", inline=False)

                        if all(i.isprintable() for i in ans4.content):
                            await ans4.delete()
                            await msg1.edit(embed=embed5)
                            ans5 = await self.bot.wait_for('message', check=check)

                            if all(i.isprintable() for i in ans5.content):
                                await ans5.delete()
                                await msg1.delete()

                                final_embed=discord.Embed(color=self.color, timestamp=self.time, title=":red_circle:**__INCOMING ANNOUNCEMENT!!!__**:red_circle:", description=f"**__{ans2.content}__**\n\n**__Bots Name:__**\n{ans3.content}\n**__Bot Owner:__**\n{ans4.content}\n**__Update Notes:__**\n{ans5.content}").set_footer(text=f"This announcement has been brought to you by {ctx.author.display_name}")
                                a = await self.channel2.send(embed=final_embed)
                                await a.pin()
                                await self.channel2.purge(limit=1)
        else:
            await ctx.message.delete()
            aa = await ctx.send("You are not in the appropriate channel to execute this command. Please go to the #staff_commands channel to use this command!")
            await asyncio.sleep(15)
            await aa.delete()

    @commands.command()
    @commands.has_any_role("Owner", "Head Dev")
    async def baddingbots(self, ctx):
        
        def check(m):
            return m.author == ctx.author

        embed1 = discord.Embed(color=self.color, timestamp=self.time, title="Welcome To The Buttler Announcement Editor!", description="Please Use This Template To Fill Out Your Announcement For Our Community:\n```\nAnnouncement Name:\nBot Name:\nBot Language:\nWhat Can The Bot Do:\nBots Prefix:\nAnnouncement:\nIn this category you are free to use what emoji's, etc. that you would like to use. You can be as creative as you want to be so long as you stay on topic.\n```").set_footer(text="Enter ready when you're ready to begin")

        if ctx.channel == self.channel1:
            await ctx.message.delete()
            msg1 = await ctx.send(embed=embed1)
            ans1 = await self.bot.wait_for('message', check=check)
            embed2 = discord.Embed(color=self.color, timestamp=self.time, title="What's The Name Of The Announcement?")

            if ans1.content.lower() == "ready":
                await ans1.delete()
                await msg1.edit(embed=embed2)
                ans2 = await self.bot.wait_for('message', check=check)
                embed3 = discord.Embed(color=self.color, timestamp=self.time, title=f"{ans2.content}", description="**__What Is The Bots Name?__**", inline=False)

                if all(i.isprintable() for i in ans2.content):
                    await ans2.delete()
                    await msg1.edit(embed=embed3)
                    ans3 = await self.bot.wait_for('message', check=check)
                    embed4 = discord.Embed(color=self.color, timestamp=self.time, title=f"{ans2.content}", description=f"**__What Is The Bots Name?__**\n{ans3.content}\n**__What Language Is The Bot Written In?__**", inline=False)
                
                    if all(i.isprintable() for i in ans3.content):
                        await ans3.delete()
                        await msg1.edit(embed=embed4)
                        ans4 = await self.bot.wait_for('message', check=check)
                        embed5 = discord.Embed(color=self.color, timestamp=self.time, title=f"{ans2.content}", description=f"**__What Is The Bots Name?__**\n{ans3.content}\n**__What Language Is The Bot Written In?__**\n{ans4.content}\n**__What Can The Bot Do?__**", inline=False)

                        if all(i.isprintable() for i in ans4.content):
                            await ans4.delete()
                            await msg1.edit(embed=embed5)
                            ans5 = await self.bot.wait_for('message', check=check)
                            embed6 = discord.Embed(color=self.color, timestamp=self.time, title=f"{ans2.content}", description=f"**__What Is The Bots Name?__**\n{ans3.content}\n**__What Language Is The Bot Written In?__**\n{ans4.content}\n**__What Can The Bot Do?__**\n{ans5.content}\n**__What Is The Bot's Prefix?__**", inline=False)

                            if all(i.isprintable() for i in ans5.content):
                                await ans5.delete()
                                await msg1.edit(embed=embed6)
                                ans6 = await self.bot.wait_for('message', check=check)
                                embed7 = discord.Embed(color=self.color, timestamp=self.time, title=f"{ans2.content}", description=f"**__What Is The Bots Name?__**\n{ans3.content}\n**__What Language Is The Bot Written In?__**\n{ans4.content}\n**__What Can The Bot Do?__**\n{ans5.content}\n**__What Is The Bot's Prefix?__**\n{ans6.content}\n**__What Is Your Descriptive Announcement?__**", inline=False)

                                if all(i.isprintable() for i in ans6.content):
                                    await ans6.delete()
                                    await msg1.edit(embed=embed7)
                                    ans7 = await self.bot.wait_for('message', check=check)
                                    embed8 = discord.Embed(color=self.color, timestamp=self.time, title=":red_circle:**__INCOMING ANNOUNCEMENT!!!!__**:red_circle:", description=f"{ans2.content}\n**__What Is The Bots Name?__**\n{ans3.content}\n**__What Language Is The Bot Written In?__**\n{ans4.content}\n**__What Can The Bot Do?__**\n{ans5.content}\n**__What Is The Bot's Prefix?__**\n{ans6.content}\n**__What Is Your Descriptive Announcement?__**\n{ans7.content}", inline=False).set_footer(text=f"This announcement has been brought to you by {ctx.author.display_name}")

                                    if all(i.isprintable() for i in ans7.content):
                                        await ans7.delete()
                                        await msg1.delete()
                                        a = await self.channel3.send(embed=embed8)
                                        await a.pin()
                                        await self.channel3.purge(limit=1)
        else:
            await ctx.message.delete()
            dd = await ctx.send("You are not in the appropriate channel to execute this command. Please go to the #staff_commands channel to use this command!")
            await asyncio.sleep(15)
            await dd.delete()

def setup(bot):
    bot.add_cog(Devs(bot))