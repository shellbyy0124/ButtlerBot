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
bots_added = data["bots_added"]




class Announcements(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def bannounce(self, ctx):

        ann1 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Buttler Announcement Editor:", description="What channel is your announcement for?\n\nEnter A for Bot Updates\nEnter B for Community Updates\nEnter C for Bots being added to the discord. If you are not the Head Dev, or the Owner, **__DO NOT__** choose option C!")
        
        ques1 = await ctx.send(embed=ann1)
        ans1 = await self.bot.wait_for('message')

        A = "a"
        B = "b"
        C = "c"

        if ans1.content.lower() == A:

            await ctx.message.delete()

            ques2 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Please enter the name of the announcement.")
            await ques1.edit(embed=ques2)
            ans2 = await self.bot.wait_for('message')

            if all(i.isprintable() for i in ans2.content):
                pass
            else:
                return await ctx.send(":red_circle: That is not a valid announcement, Try Again!")
                # some code to restart function from here

            ques3 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Please enter your announcement")
            await ques1.edit(embed=ques3)
            ans3 = await self.bot.wait_for('message')

            if all(i.isprintable() for i in ans3.content):
                pass
            else:
                return await ctx.send(":red_circle: That is not a valid entry, Try Again!")
                # some code to restart function from here

            await ques1.delete()
            await ans1.delete()
            await ans2.delete()
            await ans3.delete()
        
            finale = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"**___ANNOUNCEMENT___**:")
            finale.add_field(name=f"{ans2.content}", value=f"{ans3.content}")
            
            channel = self.bot.get_channel(bot_updates)
            await channel.send(embed=finale)

        elif ans1.content.lower() == B:

            await ctx.message.delete()
            
            ques4 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Please enter the name of the announcement.")
            await ques1.edit(embed=ques4)
            ans4 = await self.bot.wait_for('message')

            if all(i.isprintable() for i in ans4.content):
                pass
            else:
                return await ctx.send(":red_circle: Sorry that is not a valid name. Please run the command again.")
                # some code to restart from here

            ques5 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Please enter the announcement")
            await ques1.edit(embed=ques5)
            ans5 = await self.bot.wait_for('message')

            if all(i.isprintable for i in ans5.content):
                pass
            else:
                return await ctx.send(":red_cicle: That is not a valid announcement, Try Again!")
                # some code to restart function from here

            await ques1.delete()
            await ans1.delete()
            await ans4.delete()
            await ans5.delete()

            finale2 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="**___ANNOUNCEMENT___**:")
            finale2.add_field(name=f"{ans4.content}", value=f"{ans5.content}\n**__Announcement By__:** {ctx.message.author.name}")

            channel = self.bot.get_channel(community_updates)
            await channel.send(embed=finale2)

        elif ans1.content.lower() == C:

            await ctx.message.delete()

            ques6 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Enter The Name Of The Bot:")
            await ques1.edit(embed=ques6)
            ans6 = await self.bot.wait_for('message')

            if all(i.isprintable() for i in ans6.content):
                pass
            else:
                return await ctx.send(":red_circle: that is not a valid name. Please run the command again.")
                # some code to restart from here

            ques7 =discord.Embed(color=random.randint(0, 0xFFFFFF), title="Enter A 3-5 sentence description of the bot.")
            await ques1.edit(embed=ques7)
            ans7 = await self.bot.wait_for('message')

            if all(i.isprintable() for i in ans7.content):
                pass
            else:
                return await ctx.send(":red_circle: that is not a valid description. Please run the command again.")

            ques8 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Enter any other details about the bot as needed, otherwise, type N/A")
            await ques1.edit(embed=ques8)
            ans8 = await self.bot.wait_for('message')

            if all(i.isprintable() for i in ans8.content):
                pass
            else:
                return await ctx.send(":red_circle: That is not a valid entry. Type the command again.")

            await ques1.delete()
            await ans1.delete()
            await ans6.delete()
            await ans7.delete()
            await ans8.delete()

            finale3 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="**__NEW BOT INCOMING!!!!__**")
            finale3.add_field(name=f"{ans6.content}", value=f"{ans7.content}", inline=False)
            finale3.add_field(name="\u200b", value=f"{ans8.content}", inline=False)            

            channel = self.bot.get_channel(bots_added)
            await channel.send(embed=finale3)

        else:
            raise error

def setup(bot):
    print('Announcement cog has loaded...')
    bot.add_cog(Announcements(bot))