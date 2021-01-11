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
error_logs = data["errors"]["error_logs"]
announcement_errors = data["errors"]["announcement_errors"]
staff_commands = data["channels"]["staff_commands"]

class Announcements(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
    
    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Head Admin', 'Admins')
    async def bbotupdates(self, ctx):
    
        def check(m):
            return m.author == ctx.author

        color = random.randint(0, 0xFFFFFF)
        time = datetime.datetime.utcnow()
        channel1 = self.bot.get_channel(staff_commands)
        channel2 = self.bot.get_channel(bot_updates)

        embed1 = discord.Embed(color=color, timestamp=time, title="Welcome To The ButtlerBot Announcement Editor!", description="Please Use This Template To Fill Out Your Announcement For Any Updates To Our Bots:\n```\nBot Name:\nBot Owner:\nBot Updates:\nIn this category you are free to use what emoji's, etc. that you would like to use. You can be as creative as you want to be so long as you show bot update notes in some form\n```", inline=False).set_footer(text="Enter `ready` when you're ready to begin.")
        
        if ctx.channel == channel1:
            await ctx.message.delete()
            msg1 = await ctx.channel.send(embed=embed1)
            ans1 = await self.bot.wait_for('message', check=check)
            embed2 = discord.Embed(color=color, timestamp=time, title="What's The Name Of The Announcement?")

            if ans1.content.lower() == "ready":
                await ans1.delete()
                await msg1.edit(embed=embed2)
                ans2 = await self.bot.wait_for('message', check=check)
                embed3 = discord.Embed(color=color, timestamp=time, title=f"What's The Name Of The Announcement?\n{ans2.content}", description="**__What's The Name Of The Bot?__**", inline=False)
               
                if all(i.isprintable() for i in ans2.content):
                    await ans2.delete()
                    await msg1.edit(embed=embed3)
                    ans3 = await self.bot.wait_for('message', check=check)
                    embed4 = discord.Embed(color=color, timestamp=time, title=f"What's The Name Of The Announcement?\n{ans2.content}", description=f"**__What's The Name Of The Bot?__**\n{ans3.content}\n**__Who's The Bot Owner?__**", inline=False)
                
                    if all(i.isprintable() for i in ans3.content):
                        await ans3.delete()
                        await msg1.edit(embed=embed4)
                        ans4 = await self.bot.wait_for('message', check=check)
                        embed5 = discord.Embed(color=color, timestamp=time, titel=f"What's The Name Of The Announcement?\n{ans2.content}", description=f"**__What's The Name Of The Bot?__**\n{ans3.content}\n**__Who's The Bot Owner?__**\n{ans4.content}\n**__What Are Your Update Notes?__**", inline=False)

                        if all(i.isprintable() for i in ans4.content):
                            await ans4.delete()
                            await msg1.edit(embed=embed5)
                            ans5 = await self.bot.wait_for('message', check=check)

                            if all(i.isprintable() for i in ans5.content):
                                await ans5.delete()
                                await msg1.delete()

                                final_embed=discord.Embed(color=color, timestamp=time, title=":red_circle:**__INCOMING ANNOUNCEMENT!!!__**:red_circle:", description=f"**__{ans2.content}:__**\n**__Bots Name:__**\n{ans3.content}\n**__Bot Owner:__**\n{ans4.content}\n**__Update Notes:__**\n{ans5.content}").set_footer(text=f"This announcement has been brought to you by {ctx.author.display_name}")
                                a = await channel2.send(embed=final_embed)
                                await a.pin()
                                await channel2.purge(limit=1)
        else:
            await ctx.message.delete()
            aa = await ctx.send("You are not in the appropriate channel to execute this command. Please go to the #staff_commands channel to use this command!")
            await asyncio.sleep(15)
            await aa.delete()


    @commands.command()
    @commands.has_any_role("Owner", "Head Dev", "Dev", "Head Admin", "Admins")
    async def bbotcommunity(self, ctx):

        def check(m):
            return m.author == ctx.author

        color = random.randint(0, 0xFFFFFF)
        time = datetime.datetime.utcnow()
        channel1 = self.bot.get_channel(staff_commands)
        channel2 = self.bot.get_channel(community_updates)

        embed1 = discord.Embed(color=color, timestamp=time, title="Welcome To The Buttler Announcement Editor:", description="Please Use This Template To Fill Out Your Announcement For Our Community:\n```\nAnnouncement Name:\nAnnouncement:\nIn this category you are free to use what emoji's, etc. that you would like to use. You can be as creative as you want to be so long as you stay on topic.\n```", inline=False).set_footer(text="Enter `ready` when you're ready to begin.")

        if ctx.channel == channel1:
            await ctx.message.delete()
            msg1 = await ctx.send(embed=embed1)
            ans1 = await self.bot.wait_for('message', check=check)
            embed2 = discord.Embed(color=color, timestamp=time, title="What Is The Announcement Name?")

            if ans1.content.lower() == "ready":
                await ans1.delete()
                await msg1.edit(embed=embed2)
                ans2 = await self.bot.wait_for('message', check=check)
                embed3 = discord.Embed(color=color, timestamp=time, title=f"{ans2.content}", description="**__What is the announcement?__**", inline=False)

                if all(i.isprintable() for i in ans2.content):
                    await ans2.delete()
                    await msg1.edit(embed=embed3)
                    ans3 = await self.bot.wait_for('message', check=check)
                    final_embed = discord.Embed(color=color, timestamp=time, title=f":red_circle:**__ANNOUNCEMENT INCOMING!__**:red_circle:", description=f"**__{ans2.content}:__**\n{ans3.content}", inline=False).set_footer(text=f"This announcement has been brought to you by {ctx.author.display_name}")

                    if all(i.isprintable() for i in ans3.content):
                        await ans3.delete()
                        await msg1.delete()
                        msg2 = await channel2.send(embed=final_embed)
                        await msg2.pin()
                        await channel2.purge(limit=1)
        else:
            await ctx.message.delete()
            bb = await ctx.send("You are not in the appropriate channel to execute this command. Please go to the #staff_commands channel to use this command!")
            await asyncio.sleep(15)
            await bb.delete()



    @commands.command()
    @commands.has_any_role("Owner", "Head Dev")
    async def addingbots(self, ctx):
        
        def check(m):
            return m.author == ctx.author

        color = random.randint(0, 0xFFFFFF)
        time = datetime.datetime.utcnow()
        channel1 = self.bot.get_channel(staff_commands)
        channel2 = self.bot.get_channel(bots_added)

        embed1 = discord.Embed(color=color, timestamp=time, title="Welcome To The Buttler Announcement Editor!", description="Please Use This Template To Fill Out Your Announcement For Our Community:\n```\nAnnouncement Name:\nBot Name:\nBot Language:\nWhat Can The Bot Do:\nBots Prefix:\nAnnouncement:\nIn this category you are free to use what emoji's, etc. that you would like to use. You can be as creative as you want to be so long as you stay on topic.\n```").set_footer(text="Enter ready when you're ready to begin")

        if ctx.channel == channel1:
            await ctx.message.delete()
            msg1 = await ctx.send(embed=embed1)
            ans1 = await self.bot.wait_for('message', check=check)
            embed2 = discord.Embed(color=color, timestamp=time, title="What's The Name Of The Announcement?")

            if ans1.content.lower() == "ready":
                await ans1.delete()
                await msg1.edit(embed=embed2)
                ans2 = await self.bot.wait_for('message', check=check)
                embed3 = discord.Embed(color=color, timestamp=time, title=f"{ans2.content}", description="**__What Is The Bots Name?__**", inline=False)

                if all(i.isprintable() for i in ans2.content):
                    await ans2.delete()
                    await msg1.edit(embed=embed3)
                    ans3 = await self.bot.wait_for('message', check=check)
                    embed4 = discord.Embed(color=color, timestamp=time, title=f"{ans2.content}", description=f"**__What Is The Bots Name?__**\n{ans3.content}\n**__What Language Is The Bot Written In?__**", inline=False)
                
                    if all(i.isprintable() for i in ans3.content):
                        await ans3.delete()
                        await msg1.edit(embed=embed4)
                        ans4 = await self.bot.wait_for('message', check=check)
                        embed5 = discord.Embed(color=color, timestamp=time, title=f"{ans2.content}", description=f"**__What Is The Bots Name?__**\n{ans3.content}\n**__What Language Is The Bot Written In?__**\n{ans4.content}\n**__What Can The Bot Do?__**", inline=False)

                        if all(i.isprintable() for i in ans4.content):
                            await ans4.delete()
                            await msg1.edit(embed=embed5)
                            ans5 = await self.bot.wait_for('message', check=check)
                            embed6 = discord.Embed(color=color, timestamp=time, title=f"{ans2.content}", description=f"**__What Is The Bots Name?__**\n{ans3.content}\n**__What Language Is The Bot Written In?__**\n{ans4.content}\n**__What Can The Bot Do?__**\n{ans5.content}\n**__What Is The Bot's Prefix?__**", inline=False)

                            if all(i.isprintable() for i in ans5.content):
                                await ans5.delete()
                                await msg1.edit(embed=embed6)
                                ans6 = await self.bot.wait_for('message', check=check)
                                embed7 = discord.Embed(color=color, timestamp=time, title=f"{ans2.content}", description=f"**__What Is The Bots Name?__**\n{ans3.content}\n**__What Language Is The Bot Written In?__**\n{ans4.content}\n**__What Can The Bot Do?__**\n{ans5.content}\n**__What Is The Bot's Prefix?__**\n{ans6.content}\n**__What Is Your Descriptive Announcement?__**", inline=False)

                                if all(i.isprintable() for i in ans6.content):
                                    await ans6.delete()
                                    await msg1.edit(embed=embed7)
                                    ans7 = await self.bot.wait_for('message', check=check)
                                    embed8 = discord.Embed(color=color, timestamp=time, title=":red_circle:**__INCOMING ANNOUNCEMENT!!!!__**:red_circle:", description=f"{ans2.content}\n**__What Is The Bots Name?__**\n{ans3.content}\n**__What Language Is The Bot Written In?__**\n{ans4.content}\n**__What Can The Bot Do?__**\n{ans5.content}\n**__What Is The Bot's Prefix?__**\n{ans6.content}\n**__What Is Your Descriptive Announcement?__**\n{ans7.content}", inline=False).set_footer(text=f"This announcement has been brought to you by {ctx.author.display_name}")

                                    if all(i.isprintable() for i in ans7.content):
                                        await ans7.delete()
                                        await msg1.delete()
                                        a = await channel2.send(embed=embed8)
                                        await a.pin()
                                        await channel2.purge(limit=1)
        else:
            await ctx.message.delete()
            dd = await ctx.send("You are not in the appropriate channel to execute this command. Please go to the #staff_commands channel to use this command!")
            await asyncio.sleep(15)
            await dd.delete()
def setup(bot):
    bot.add_cog(Announcements(bot))