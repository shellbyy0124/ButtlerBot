import discord
import random
import datetime
import asyncio
import json

from discord.ext import commands
from discord.ext.commands import Cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

challenge_updates = data["channels"]["challenge_updates"]

class Challenges(commands.Cog):

    def __init__(self, bot):

        self.bot=bot

    @commands.command(aliases=['buplist'])
    @commands.has_any_role("Owner", "Head Dev", "Dev")
    async def updatechallengelist(self, ctx):

        def check(m):
            return m.author.id == ctx.author.id

        def error():
            tries = 0
            tries += 1
            if tries < 4:
                return error
            if tries == 4:
                return error1

        error = "Invalid Entry: Try Again!"
        error1 = "You have entered an invalid entry too many times. Please createa a support channel for further assistance!"
        color = random.randint(0, 0xFFFFFF)
        time = datetime.datetime.utcnow()
        bot = self.bot.user.avatar_url

        embed = discord.Embed(color=color, timestamp=time, title="Type ready when you are ready").set_thumbnail(url=bot)
        msg1 =await ctx.send(embed=embed)
        ans1 = await self.bot.wait_for('message', check=check)

        if ans1.content.lower() == "ready":
            embed1 = discord.Embed(color=color, timestamp=time, title="Please Enter The Coding Challenge Name:").set_thumbnail(url=bot)
            await msg1.edit(embed=embed1)
            ans2 = await self.bot.wait_for('message', check=check)
            if all(i.isprintable() for i in ans1.content):
                embed2 = discord.Embed(color=color, timestamp=time, title="Please Enter The Language For This Challenge:").set_thumbnail(url=bot)
                await msg1.edit(embed=embed2)
                await ctx.message.delete()
                await ans1.delete()
                await ans2.delete()
                ans3 = await self.bot.wait_for('message', check=check)
                if all(i.isprintable() for i in ans2.content):
                    embed3 = discord.Embed(color=color, timestamp=time, title="Please Enter The Challenge Details:").set_thumbnail(url=bot)
                    await msg1.edit(embed=embed3)
                    await ans3.delete()
                    ans4 = await self.bot.wait_for('message', check=check)
                    if all(i.isprintable() for i in ans3.content):

                        final_embed = discord.Embed(color=color, timestamp=time, title="**__New Challenge__**", description=f"""Challenge Name: {ans2.content}
                                                                                                                                Challenge Language: {ans3.content}
                                                                                                                                Challenge Details: {ans4.content}""")
                        final_embed.set_thumbnail(url=bot)
                        final_embed.set_footer(text=f"This challenge has been brought to you by, {ctx.author.display_name}")
                        channel = self.bot.get_channel(challenge_updates)
                        await channel.send(embed=final_embed)

                        await msg1.delete()
                        await ans4.delete()
                        for i in self.data.keys():
                            if ans3.content.lower() == i.lower():

                                with open('./challenges.json', 'r', encoding='utf-8-sig') as g:
                                    data = json.load(g)

                                current_data = data
                                new_data = data["challenges"][str(ans3.content)] = {"challenge_name" : str(ans2.content), "challenge_details" : str(ans4.content)}

                                with open('./challenges.json', 'w', encoding='utf-8-sig') as x:
                                    data = json.dump(current_data, new_data, indent=4)
                        
                            else:
                                error()

                    else:
                        error()
                else:
                    error()
            else:
                error()
        else:
            error()

    @updatechallengelist.error
    async def commanderror(self, ctx, error):
        if isinstance(error,commands.MissingAnyRole):
            await ctx.send("You don't have the roles")

def setup(bot):
    bot.add_cog(Challenges(bot))