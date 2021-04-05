import discord
import json
import random
import os

from discord.ext import commands
from discord.ext.commands import Cog
from os import error

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data=json.load(f)

bot_updates = data["bot_updates"]
community_updates = data["community_updates"]




class Announcements(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def bannounce(self, ctx):

        ann1 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Buttler Announcement Editor:", description="What channel is your announcement for?\n\nEnter A for Bot Updates\nEnter B for Community Updatess")
        
        ques1 = await ctx.send(embed=ann1)
        ans1 = await self.bot.wait_for('message')

        A = "a"
        B = "b"

        if ans1.content.lower() == A:

            ques2 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Please enter the name of the announcement.")
            await ques1.edit(embed=ques2)
            ans2 = await self.bot.wait_for('message')

            ques3 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Please enter your announcement")
            await ques1.edit(embed=ques3)
            ans3 = await self.bot.wait_for('message')

            if all(x.isalpha() or x.isspace() for x in ans2.content):
                pass
            else:
                return await ctx.send("That is not a valid entry, Try Again!")
                # some code to restart function from here

        
            finale = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"**___ANNOUNCEMENT___**:")
            finale.add_field(name=f"{ans2.content}", value=f"{ans3.content}")

            await ans1.delete()
            await ques1.delete()
            await ans2.delete()
            await ans3.delete()
            
            channel = self.bot.get_channel(bot_updates)
            await channel.send(embed=finale)

        elif ans1.content.lower() == B:
            
            ques4 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Please enter the name of the announcement.")
            await ques1.edit(embed=ques4)
            ans4 = await self.bot.wait_for('message')

            if all(y.isalpha() or y.isspace() for y in ans4.content):
                pass
            else:
                return await ctx.send("Sorry that is not a valid announcement. Please run the command again.")
                # some code to restart function from here

            ques5 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Please enter the announcement")
            await ques1.edit(embed=ques5)
            ans5 = await self.bot.wait_for('message')

            finale2 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="**___ANNOUNCEMENT___**:")
            finale2.add_field(name=f"{ans4.content}", value=f"{ans5.content}")

            await ans1.delete()
            await ques1.delete()
            await ans4.delete()
            await ans5.delete()

            channel = self.bot.get_channel(community_updates)
            await channel.send(embed=finale2)

        else:
            raise error

def setup(bot):
    bot.add_cog(Announcements(bot))