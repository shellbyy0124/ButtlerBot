import discord
import datetime
import random
import json
import asyncio

from discord.ext import commands
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

errors = data["channels"]["errors"]
suggestions = data["channels"]["suggestions"]
botbugs = data["channels"]["botbugs"]

class Suggestions(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
    
    @commands.command()
    async def suggest(self, ctx):

        def check(m):
            return ctx.author == m.author

        embed1 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Suggestions Editor", description="Please Select One Of The Following:\nA) Discord Suggestion\nB) Bot Suggestion\nC) Bad List\nD) Bot Bugs", inline=False).set_thumbnail(url=self.url)
        msg1 = await ctx.send(embed=embed1)
        ans1 = await self.bot.wait_for('message', check=check)

        if ans1.content.lower() == "a":
            
            embed2 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Suggestions Editor", description="What is the subject of your suggestion?", inline=False).set_thumbnail(url=self.ur)
            await msg1.edit(embed=embed2)
            ans2 = await self.bot.wait_for('message', check=check)

            if all(i.isprintable() for i in ans2.content):

                embed3 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Suggestions Editor", description=f"**__Suggestion Subject:__**\n{ans2.content}\nWhat is your suggestion?", inline=False).set_thumbnail(url=self.url)
                await msg1.edit(embed=embed3)
                ans3 = await self.bot.wait_for('message', check=check)

                if all(i.isprintable() for i in ans3.content):

                    embed4 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Suggestions Editor", description=f"**__Suggestions Subject:__**\n{ans2.content}\n**__Suggestion:_**\n{ans3.content}\nIf you are satisfied with your entries, then type `!save`. If not, then type `!exit`.", inline=False).set_thumbnail(url=self.url)
                    await msg1.edit(embed=embed4)
                    ans4 = await self.bot.wait_for('message', check=check)

                    if ans4.content == "!save":

                        await ctx.message.delete()
                        await ans1.delete()
                        await ans2.delete()
                        await ans3.delete()
                        await ans4.delete()

                        final_embed = discord.Embed(color=self.color, timestamp=self.time, title=f"**__INCOMING SUGGESTION FROM {ctx.author.name}__**", description=f"**__Suggestions Subject:__**\n{ans2.content}\n**__Suggestion:__**\n{ans3.content}", inline=False).set_thumbnail(url=ctx.author.avatar_url)
                        channel = self.bot.get_channel(suggestions)
                        a = await channel.send(embed=final_embed)
                        await a.pin()

        elif ans1.content.lower() == "b":
            
            embed1 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Suggestions Editor", description=f"What is the name of the bot you are making a suggestion for? If you're unsure of the bots name, then type `>bbotlist` for a list of the bots within the {ctx.guild.name} discord", inline=False).set_thumbnail(url=self.url)
            msg1 = await ctx.send(embed=embed1)
            ans1 = await self.bot.wait_for('message', check=check)

            if all(i.isprintable() for i in ans1.content):

                embed2 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Suggestions Editor", description=f"**__Bots Name:__**\n{ans1.content}\nWhat is your suggestion?", inline=False).set_thumbnail(url=self.url)
                await msg1.edit(embed=embed2)
                ans2 = await self.bot.wait_for('message', check=check)

                if all(i.isprintable() for i in ans2.content):

                    embed3 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Suggestions Editor", description=f"**__Bots Name:__**\n{ans1.content}\n**__Suggestion:__**\n{ans2.content}\nIf you are satisfied with your entries, then type `!save`. If not, then type `!exit`.", inline=False).set_thumbnail(url=self.url)
                    await msg1.edit(embed=embed3)
                    ans3 = await self.bot.wait_for('message', check=check)

                    if ans3.content == "!save":

                        await ctx.message.delete()
                        await msg1.delete()
                        await ans1.delete()
                        await ans2.delete()
                        await ans3.delete()

                        final_embed = discord.Embed(color=self.color, timestamp=self.time, title=f"**__INCOMING SUGGESTION FROM {ctx.author.name}", description=f"**__Bots' Name:__**\n{ans1.content}\n**__Suggestion:__**{ans2.content}", inline=False).set_thumbnail(url=ctx.author.avatar_url)
                        channel = self.bot.get_channel(suggestions)
                        await channel.send(embed=final_embed)

                    elif ans3.content == "!exit":

                        await ctx.message.delete()
                        await msg1.delete()
                        await ans1.delete()
                        await ans2.delete()
                        await ans3.delete()

                        a = await ctx.send("You will need to restart the command")
                        await asyncio.sleep(10)
                        await a.delete()

                    else:

                        a = await ctx.send("Take a screenshot of the steps you've gone through, and then post that screenshot in a support channel")
                        await asyncio.sleep(60)
                        await a.delete()
                else:

                    channel = self.bot.get_channel(errors)
                    a = await channel.send("Error on line 113 in suggestions.py")
                    await a.pin()

            else:

                channel = self.bot.get_channel(errors)
                a = await channel.send("Error on line 117 in suggestions.py")
                await a.pin()

        elif ans1.content.lower() == "c":

            bug1 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Suggestion Editor", description="Please Enter The Name Of The Bot:").set_thumbnail(url=self.url)
            msg1 = await ctx.send(embed=bug1)
            ans1 = await self.bot.wait_for('message', check=check)

            if all(i.isprintable() for i in ans1.content):

                bug2 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Suggestion Editor", description="Please Enter The Word You Would Like Voted On").set_thumbnail(url=self.url)
                await msg1.edit(embed=bug2)
                ans2 = await self.bot.wait_for('message', check=check)

                if all(x.isprintable() for x in ans2.content):

                    bug3 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Suggestions Editor", description="Please Enter The Reason For This Word").set_thumbnail(url=self.url)
                    await msg1.edit(embed=bug3)
                    ans3 = await self.bot.wait_for('message', check=check)

                    if all(i.isprintable() for i in ans3.content):
                        
                        bug4 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot Suggestions Editor", description=f"**__Word Chosen:__**\n{ans2.content}\n**__Reason:__**\n{ans3.content}\nIf you are satisfied with your entries, then type `!save`. If not, then type `!Exit`.", inline=False).set_thumbnail(url=self.url)
                        await msg1.edit(embed=bug4)
                        ans4 = await self.bot.wait_for('message', check=check)

                        if ans4.content == "!save":

                            await ctx.message.delete()
                            await msg1.delete()
                            await ans1.delete()
                            await ans2.delete()
                            await ans3.delete()

                            finale = discord.Embed(color=self.color, timestamp=self.time, title=f"{ans1.content}\n{ans2.content}\n{ans3.content}").set_thumbnail(url=self.url)       

                            channel = self.bot.get_channel(botbugs)
                            await channel.send(embed=finale)

        elif ans1.content.lower() == "d":

            await ctx.message.delete()
        
            embed1 = discord.Embed(color=self.color, timestamp=self.time, title="ButtlerBot BotBug Editor", description="What is the name of the Bot?").set_thumbnail(url=self.url)
            channel = self.bot.get_channel(suggestions)
            await channel.send(embed=bls)

        else:
            channel = self.bot.get_channel(errors)
            a = await channel.send("Error line 32 suggestions.py")
            await a.pin()

def setup(bot):
    bot.add_cog(Suggestions(bot))