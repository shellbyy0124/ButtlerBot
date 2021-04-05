import discord
import random
import datetime
import json
import asyncio

from discord.ext import commands
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

staff_commands = data["channels"]["staff_commands"]
community_updates = data["channels"]["community_updates"]
errors = data["channels"]["errors"]
bot_updates = data["channels"]["bot_updates"]
bots_added = data["channels"]["bots_added"]

class Announcements(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.color = random.randint(0, 0xFFFFFF)
        self.time = datetime.datetime.utcnow()
        self.url = self.bot.user.avatar_url
    
    @commands.command()
    async def bann(self, ctx):

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

        def check(m):
            return ctx.author == m.author

        channel1 = self.bot.get_channel(staff_commands)
        footer = "All inputs will delete themselves once you've completed the announcement editor"

        if ctx.message.channel == channel1:

            embed1 = discord.Embed(color=self.color, timestamp=self.time, title="Welcome To The ButtlerBot Announcement Editor", description="To use this editor, please read each screen correctly, and follow the prompts. Any mistypes, and you will need to start over", inline=False).set_thumbnail(url=self.url).set_footer(text=footer)
            msg1 = await ctx.send(embed=embed1)

            await asyncio.sleep(10)
            embed2 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Announcement Editor:", description="Are you: A) Making A General Announcement?, B) Adding A Bot To The Discord?, or C) Updating A Bots Notes?\n**__Option B, and C Are Strictly For Our Dev Team", inline=False).set_thumbnail(url=self.url).set_footer(text=footer)
            await msg1.edit(embed=embed2)
            ans1 = await self.bot.wait_for('message', check=check)

            if ans1.content.lower() == "a":

                embed3 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Announcement Editor:", description="What is the subject of your announcement?", inline=False).set_thumbnail(url=self.url).set_footer(text=footer)
                await msg1.edit(embed=embed3)
                ans2 = await self.bot.wait_for('message', check=check)

                if all(i.isprintable() for i in ans2.content):

                    embed4 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Announcement Editor:", description=f"**__Announcement Subject:__**\n{ans2.content}\nWhat Is Your Announcement?", inline=False).set_thumbnail(url=self.url).set_footer(text=footer)
                    await msg1.edit(embed=embed4)
                    ans3 = await self.bot.wait_for('message', check=check)

                    if all(i.isprintable() for i in ans3.content):

                        embed5 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Announcement Editor:", description=f"**__Announcement Subject:__**\n{ans2.content}\n**__Announcement Message:__**\n{ans3.content}\nIf you are satisfied with your announcement, then type `!save`. If not, then please type `!exit`.", inline=False).set_thumbnail(url=self.url).set_footer(text=footer)
                        await msg1.edit(embed=embed5)
                        ans4 = await self.bot.wait_for('message', check=check)

                        if ans4.content == "!save":
                            
                            await ctx.message.delete()
                            await msg1.delete()
                            await ans1.delete()
                            await ans2.delete()
                            await ans3.delete()
                            await ans4.delete()

                            channel = self.bot.get_channel(community_updates)
                            final_embed = discord.Embed(color=self.color, timestamp=self.time, title=f":star:**__INCOMING ANNOUNCEMENT FROM {ctx.author.name}__**:star:", description=f"**__Announcement Subject__**\n{ans2.content}\n**__Announcement:__**\n{ans3.content}", inline=False).set_thumbnail(url=ctx.author.avatar_url)
                            a = await channel.send(embed=final_embed)
                            await a.pin()
                            await channel.purge(limit=1)
                        
                        elif ans4.content == "!exit":

                            await ctx.message.delete()
                            await msg1.delete()
                            await ans1.delete()
                            await ans2.delete()
                            await ans3.delete()
                            await ans4.delete()

                            a = await ctx.send("**__PLEASE TYPE THE COMMAND AGAIN TO START OVER__**")
                            await asyncio.sleep(10)
                            await a.delete()

            elif ans1.content.lower() == "b":
                
                embed1 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Announcement Editor", description="What is the subject of your announcement?", inline=False).set_thumbnail(url=self.url).set_footer(text=footer)
                msg1 = await ctx.send(embed=embed1)
                ans1 = await self.bot.wait_for('message', check=check)

                if all(i.isprintable() for i in ans1.content):

                    embed2 = discord.Embed(color=self.color, timetsamp=self.time, title="ButtlerBot Announcement Editor", description=f"**__Announcement Subject:__**\n{ans1.content}\nWhat is the bots name?", inline=False).set_thumbnail(url=self.url).set_footer(text=footer)
                    await msg1.edit(embed=embed2)
                    ans2 = await self.bot.wait_for('message', check=check)

                    if all(i.isprintable() for i in ans2.content):

                        embed3 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Announcement Editor", description=f"**__Announcement Subject:__**\n{ans1.content}\n**__Bots' Name:__**\n{ans2.content}\nWhat is the bots purpose?", inline=False).set_thumbnail(url=self.url).set_footer(text=footer)
                        await msg1.edit(embed=embed3)
                        ans3 = await self.bot.wait_for('message', check=check)

                        if all(i.isprintable() for i in ans3.content):

                            embed4 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Announcement Editor", description=f"**__Announcement Subject:__**\n{ans1.content}\n**__Bots' Name:__**\n{ans2.content}\n**__Bots' Purpose:__**\n{ans3.content}\nWhat is your teams' thoughts on this bot?", inline=False).set_thumbnail(url=self.url).set_footer(text=footer)
                            await msg1.edit(embed=embed4)
                            ans4 = await self.bot.wait_for('message', check=check)

                            if all(i.isprintable() for i in ans3.content):

                                embed5 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Announcement Editor", description=f"**__Announcement Subject:__**\n{ans1.content}\n**__Bots' Name:__**\n{ans2.content}\n**__Bots' Purpose:__**\n{ans3.content}\n**__Dev Teams' Thoughts:__**\n{ans4.content}\nIf you are satisfied with your entries, then please type `!save`. If not, then type `!exit`", inline=False).set_thumbnail(url=self.url).set_footer(text=footer)
                                await msg1.edit(embed=embed5)
                                ans5 = await self.bot.wait_for('message', check=check)

                                if ans5.content == "!save":

                                    await ctx.message.delete()
                                    await msg1.delete()
                                    await ans1.delete()
                                    await ans2.delete()
                                    await ans3.delete()
                                    await ans4.delete()
                                    await ans5.delete()

                                    final_embed = discord.Embed(color=self.color, timestamp=self.time, title=f":star:**__ANNOUNCEMENT INCOMING FROM {ctx.author.name}__**:star:", description=f"**__Announcement Subject:__**\n{ans1.content}\n**__Bots' Name:__**\n{ans2.content}\n**__Bots' Purpose:__**\n{ans3.content}\n**__Dev Teams' Thoughts:__**\n{ans4.cont}", inline=False).set_thumbnail(url=ctx.author.avatar_url)
                                    channel = self.bot.get_channel(bots_added)
                                    a = await channel.send(embed=final_embed)
                                    await a.pin()
                                    await channel.purge(limit=1)
                                
                                elif ans5.content == "!exit":

                                    await ctx.message.delete()
                                    await msg1.delete()
                                    await ans1.delete()
                                    await ans2.delete()
                                    await ans3.delete()
                                    await ans4.delete()
                                    await ans5.delete()

                                    a = await ctx.send("**__PLEASE TYPE THE COMMAND AGAIN TO START OVER__**")
                                    await asyncio.sleep(10)
                                    await a.delete()

            elif ans1.content.lower() == "c":

                embed1 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Announcement Editor", description="What is the subject of your announcement?", inline=False).set_thumbnail(url=self.url).set_footer(text=footer)
                await msg1.edit(embed=embed1)
                ans1 = await self.bot.wait_for('message', check=check)

                if all(i.isprintable() for i in ans1.content):

                    embed2 = discord.Embed(color=self.color, timetsamp=self.time, title="ButtlerBot Announcement Editor", description=f"**__Announcement Subject:__**\n{ans1.content}\nWhat is the bots name?", inline=False).set_thumbnail(url=self.url).set_footer(text=footer)
                    await msg1.edit(embed=embed2)
                    ans2 = await self.bot.wait_for('message', check=check)

                    if all(i.isprintable() for i in ans2.content):
                        
                        embed3 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Announcement Editor", description=f"**__Announcement Subject:__**\n{ans1.content}\n**__Bots' Name:__**\n{ans2.content}\nWhat are your teams update notes?", inline=False).set_thumbnail(url=self.url).set_footer(text=footer)
                        await msg1.edit(embed=embed3)
                        ans3 = await self.bot.wait_for('message', check=check)

                        if all(i.isprintable() for i in ans3.content):

                            embed4 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Announcement Editor", description=f"**__Announcement Subject:__**\n{ans1.content}\n**__Bots' Name:__**\n{ans2.content}\n**__Update Notes:__**\n{ans3.content}\nIf you are satisfied with your entries, then type `!save`. If not, then type `!exit`.", inline=False).set_thumbnail(url=self.url).set_footer(text=footer)
                            await msg1.edit(embed=embed4)
                            ans4 = await self.bot.wait_for('message', check=check)

                            if ans4.content == "!save":

                                await ctx.message.delete()
                                await msg1.delete()
                                await ans1.delete()
                                await ans2.delete()
                                await ans3.delete()
                                await ans4.delete()

                                final_embed = discord.Embed(color=self.color, timestamp=self.time, title=f"**__INCOMING ANNOUNCEMENT FROM {ctx.author.name}__**", description=f"**__Announcement Subject:__**\n{ans1.content}\n**__Bots' Name:__**\n{ans2.content}\n**__Update Notes:__**\n{ans3.content}", inline=False).set_thumbnail(url=self.url)
                                channel = self.bot.get_channel(bot_updates)
                                a = await channel.send(embed=final_embed)
                                await a.pin()
                                await channel.purge(limit=1)
                                
                            elif ans4.content == "!exit":

                                await ctx.message.delete()
                                await msg1.delete()
                                await ans1.delete()
                                await ans2.delete()
                                await ans3.delete()
                                await ans4.delete()

                                a = await ctx.send("**__PLEASE TYPE THE COMMAND AGAIN TO RESTART YOUR ANNOUCNEMENT__**")
                                await asyncio.sleep(60)
                                await a.delete()
        else:
            a = await ctx.send(":red_circle:**__Y0U ARE NOT IN THE CORRECT CHANNEL!__**\nPlease go to the staff commands channel to execute this command!")
            await asyncio.sleep(10)
            await a.delete()

def setup(bot):
    bot.add_cog(Announcements(bot))