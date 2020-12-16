import discord
import json
import asyncio
import datetime
import random

from discord.ext import commands
from discord.ext.commands import Cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)


class Teams(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['bteam'])
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Head Admin', 'Admins', 'Team Captain')
    async def createteams(self, ctx):

        category = discord.utils.get(ctx.guild.categories, name='Teams')

        for channel in category.text_channels:

            if str(channel.topic) == str(ctx.author.id):

                msg1 = discord.Embed(color=discord.Colour.red(), title=":red_circle:**__ATTENTION__**:red_circle:", description="Sorry, but you already have a channel created. If you feel this is an error, then please get in touch with a staff member, and they will help you appropriately.")
                msg1.set_footer(text="This message will self-destruct in 10 seconds")
                await asyncio.sleep(10)
                await msg1.delete()

            else:

                channel = await ctx.guild.create_text_channel(ctx.author.name, overwrites=None, topic=str(ctx.author.id), category=category)

                team = discord.Embed(color=random.randint(0, 0xFFFFFF), title="__Teams Channel Setup__", description="Welcome to your new teams channel. A few quick things to note.", inline=False)
                team.add_field(name="__Team Captains:__", value="You are the staff member of your channel. If you need further assistance with your channel, then ping an admin.", inline=False)
                team.add_field(name="__Rules:__", value="The rules for the discord also apply within this channel. No NSFW, No Cursing, etc. Buttler is watching at all times, and after enough warnings, you will be removed from the team. Anyone may pin whatever messages they want to, however, **__no one is to unpin/delete this message, or the message that shows the list of members names!__**", inline=False)
                team.add_field(name=":red_circle:__Reminder!!!!__:red_circle:", value="Be sure to save any and all relative things from your team to your computers that you want/need for when the team is done with the channel. After the channel has been closed, there is no getting it back!", inline=False)
                team.timestamp = datetime.datetime.utcnow()
                msg = await channel.send(embed=team)
                await msg.pin()
                await asyncio.sleep(3)
                await channel.purge(limit=1)
                
                team1 = discord.Embed(color=discord.Color.blue(), title="Please Choose A Team Name:")
                msg2 = await channel.send(embed=team1)
                ans = await self.bot.wait_for('message')
                name1 = await channel.edit(name=f'{ans.content}')

                team2 = discord.Embed(color=discord.Color.green(), title=f"Team Name: {ans.content}", description=f'What language(S) are you using?')
                await msg2.edit(embed=team2)
                ans2 = await self.bot.wait_for('message')

                team3 = discord.Embed(color=discord.Colour.red(), title=f'Team Name: {ans.content}', description=f'Languages: {ans2.content}\nWhat is your teams current project?')
                await msg2.edit(embed=team3)
                ans3 = await self.bot.wait_for('message')

                team4 = discord.Embed(color=discord.Colour.blurple(), title=f'Team Name: {ans.content}', description=f'Languages: {ans2.content}\nCurrent Project: {ans3.content}\n\nIf you are satisfied with your answers\nA) save and continue\nB) delete and start over')
                await msg2.edit(embed=team4)
                ans4 = await self.bot.wait_for('message')

                A = 'a'
                B = 'b'

                if ans4.content == A:

                    final_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Welcome To Your Channel!", description="You have succesfully created your teams text channel. Please enter all of the names of your team members. **THIS IS NOT OPTIONAL** Once you have entered in your teammates names, everything that is unimportant will delete itself so please do not attempt to delete the messages.", inline=False)
                    await msg2.edit(embed=final_message)
                    ans5 = await self.bot.wait_for('message')      
                    await ans5.pin()
                    await asyncio.sleep(3)
                    await channel.purge(limit=1)

                    await msg2.delete()
                    await ans.delete()
                    await ans2.delete()
                    await ans3.delete()
                    await ans4.delete()
                
                elif ans4.content == B:

                    await name1.send("This channel will close in 10 seconds.")
                    await asyncio.sleep(10)
                    await name1.delete()

    @commands.command()
    async def btclose(ctx):
        if ctx.channel.category.name == 'Teams':
            await ctx.channel.delete()


def setup(bot):
    bot.add_cog(Teams(bot))