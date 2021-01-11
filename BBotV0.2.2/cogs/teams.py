import discord
import json
import asyncio
import datetime
import random

from discord.ext import commands
from discord.ext.commands import Cog


class Teams(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['bteam'])
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Head Admin', 'Admins', 'Team Captain')
    async def createteams(self, ctx):

        category = discord.utils.get(ctx.guild.categories, name='Teams')
        color = random.randint(0, 0xFFFFFF)
        time = datetime.datetime.utcnow()

        for channel in category.text_channels:

            while True:

                if str(channel.name) == str(ctx.author.display_name):

                    msg1 = discord.Embed(color=color, timestamp=time, title=":red_circle:**__ATTENTION__**:red_circle:", description="Sorry, but you already have a channel created. If you feel this is an error, then please get in touch with a staff member, and they will help you appropriately.")
                    msg1.set_footer(text="This message will self-destruct in 10 seconds")
                    await asyncio.sleep(10)
                    await msg1.delete()

                else:

                    channel = await ctx.guild.create_text_channel(ctx.author.name, category=category)

                    team = discord.Embed(color=color, timestamp=time, title="__Teams Channel Setup__", description="Welcome to your new teams channel. A few quick things to note.", inline=False)
                    team.add_field(name="__Team Captains:__", value="You are the staff member of your channel. If you need further assistance with your channel, then ping an admin.", inline=False)
                    team.add_field(name="__Rules:__", value="The rules for the discord also apply within this channel. No NSFW, No Cursing, etc. Buttler is watching at all times, and after enough warnings, you will be removed from the team. Anyone may pin whatever messages they want to, however, **__no one is to unpin/delete this message, or the message that shows the list of members names!__**", inline=False)
                    team.add_field(name=":red_circle:__Reminder!!!!__:red_circle:", value="Be sure to save any and all relative things from your team to your computers that you want/need for when the team is done with the channel. After the channel has been closed, there is no getting it back!", inline=False)
                    team.timestamp = datetime.datetime.utcnow()
                    msg = await channel.send(embed=team)
                    await msg.pin()
                    await asyncio.sleep(3)
                    await channel.purge(limit=1)
                    
                    team1 = discord.Embed(color=color, timestamp=time, title="Please Choose A Team Name:")
                    msg2 = await channel.send(embed=team1)
                    ans = await self.bot.wait_for('message')
                    name1 = await channel.edit(name=f'{ans.content}')

                    team2 = discord.Embed(color=color, timestamp=time, title=f"Team Name: {ans.content}", description=f'What language(s) are you using?')
                    await msg2.edit(embed=team2)
                    ans2 = await self.bot.wait_for('message')

                    team3 = discord.Embed(color=color, timestamp=time, title=f'Team Name: {ans.content}', description=f'Languages: {ans2.content}\nWhat is your teams current project?')
                    await msg2.edit(embed=team3)
                    ans3 = await self.bot.wait_for('message')

                    team4 = discord.Embed(color=color, timestamp=time, title=f'Team name: {ans.content}', description=f'Languages: {ans2.content}\nWhat is your teams current project?\n{ans3.content}\nWho are your team members?')
                    await msg2.edit(embed=team4)
                    ans4 = await self.bot.wait_for('message')

                    team5 = discord.Embed(color=color, timestamp=time, title=f'Team Name: {ans.content}', description=f'Languages: {ans2.content}\nCurrent Project: {ans3.content}\nTeam Members:\n{ans4.content}\nIf you are satisfied with your answers\nEnter `a` to save and continue\nEnter `b` to start over.')
                    await msg2.edit(embed=team5)
                    ans5 = await self.bot.wait_for('message')

                    if ans5.content.lower() == "a":

                        final_embed = discord.Embed(color=color, timestamp=time, title=f'Team Name: {ans.content}', description=f'Languages: {ans2.content}\nCurrent Project: {ans3.content}\nTeam Members:\n{ans4.content}')
                        await msg2.edit(embed=final_embed)                    
                        a = await channel.send(":red_circle:**__DO NOT DELETE ANY MESSAGES. THE BOT WILL AUTOMATICALLY PIN AND DELETE ALL INFO THAT IS NEEDED/UNEEDED__**:red_circle:")
                        await asyncio.sleep(1)
                        await msg2.pin()
                        await asyncio.sleep(1)
                        await ans.delete()
                        await asyncio.sleep(1)
                        await ans2.delete()
                        await asyncio.sleep(1)
                        await ans3.delete()
                        await asyncio.sleep(1)
                        await ans4.delete()
                        await asyncio.sleep(1)
                        await ans5.delete()
                        await asyncio.sleep(1)
                        await channel.purge(limit=1)
                        await asyncio.sleep(1)
                        await a.delete()
                    
                    elif ans4.content.lower() == "b":

                        await name1.send("Please Run The Command Again: This channel will close in 10 seconds.")
                        await asyncio.sleep(10)
                        await name1.delete()

def setup(bot):
    bot.add_cog(Teams(bot))