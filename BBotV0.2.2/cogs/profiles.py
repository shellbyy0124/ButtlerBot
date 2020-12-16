import discord
import json
import DiscordUtils as DU 
import random
import datetime
import asyncio

from discord.ext import commands
from discord.ext.commands import cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

profiles = data["profiles"]

class Profiles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['bcprofile'])
    async def createprofile(self, ctx):

        timestamp = datetime.datetime.utcnow()
        color = random.randint(0, 0xFFFFFF)
        member = ctx.author
        category = discord.utils.get(ctx.guild.categories, name='Profile Setup')
        channel = await ctx.guild.create_text_channel(ctx.author.name, overwrites=None, category=category)
        certifications = []
        awards = []
        degrees = []
        languages = []
        errormsg = "That is not a valid entry. Please try again!"
        tries = 0
        
        msg = discord.Embed(color=color, title="Welcome to the profile setup! :)", description="During this setup, I am going to be asking you a series of questions. This won't take but just a few moments of your time. Please be sure to read each question, and it's instructions carefully! Type ready when you're ready\n**___NOTE___**\n**__You only get 3 tries on an incorrect input. After 3 incorrect tries, it will delete the channel, and you will need to go back to #profiles to start over!__**") 
        snd = await channel.send(embed=msg)
        ans = await self.bot.wait_for('message')

        if ans.content == "ready":

            msg1 = discord.Embed(color=color, title="How long have you been programming for?")
            await ans.delete()
            await snd.edit(embed=msg1)
            
            while True:
                ans1 = await self.bot.wait_for("message")
                if all(x.isprintable() for x in ans1.content):
                    break
                tries += 1
                if tries == 1:
                    return await channel.send(errormsg)
                if tries == 2:
                    return await channel.send(errormsg)
                if tries == 3:
                    await channel.send("Please go back to the profiles channel to type the command, and try again")
                    await asyncio.sleep(20)
                    await channel.delete()
                    return

            msg2 = discord.Embed(color=color, title="What is your preferred programming language?")
            await ans1.delete()
            await snd.edit(embed=msg2)
            
            while True:
                ans2 = await self.bot.wait_for("message")
                if all(x.isprintable() for x in ans2.content):
                    break
                tries += 1
                if tries == 1:
                    return await channel.send(errormsg)
                if tries == 2:
                    return await channel.send(errormsg)
                if tries == 3:
                    await channel.send("Please go back to the profiles channel to type the command, and try again")
                    await asyncio.sleep(20)
                    await channel.delete()
                    return

            msg3 = discord.Embed(color=color, title="What is your favorite programming language?")
            await ans2.delete()
            await snd.edit(embed=msg3)
            
            while True:
                ans3 = await self.bot.wait_for("message")
                if all(x.isprintable() for x in ans3.content):
                    break
                tries += 1
                if tries == 1:
                    return await channel.send(errormsg)
                if tries == 2:
                    return await channel.send(errormsg)
                if tries == 3:
                    await channel.send("Please go back to the profiles channel to type the command, and try again")
                    await asyncio.sleep(20)
                    await channel.delete()
                    return

            msg4 = discord.Embed(color=color, title="Would you like to list any, or all, languages that you know and use?", description="If so, then please enter them now. Do not use commas, periods, etc. to separate as teh bot is already setup to do that for you. Please enter them like so, `lang_one lang_two lang_three`! If you do not want to list any, please enter N/A.")
            await ans3.delete()
            await snd.edit(embed=msg4)
            
            while True:
                ans4 = await self.bot.wait_for("message")
                languages.append(ans4.content)
                if all(x.isprintable() for x in ans4.content):
                    break
                tries += 1
                if tries == 1:
                    return await channel.send(errormsg)
                if tries == 2:
                    return await channel.send(errormsg)
                if tries == 3:
                    await channel.send("Please go back to the profiles channel to type the command, and try again")
                    await asyncio.sleep(20)
                    await channel.delete()
                    return

            msg5 = discord.Embed(color=color, title="Would you like to list any certifications?", description="If so, then please enter them now. Do not use commas, periods, etc. to separate as teh bot is already setup to do that for you. Please enter them like so, `Certification_one certification_two certificaiton_three`! If you do not want to list any, please enter N/A.")
            await ans4.delete()
            await snd.edit(embed=msg5)
            
            while True:
                ans5 = await self.bot.wait_for("message")
                certifications.append(ans5.content)
                if all(x.isprintable() for x in ans5.content):
                    break
                tries += 1
                if tries == 1:
                    return await channel.send(errormsg)
                if tries == 2:
                    return await channel.send(errormsg)
                if tries == 3:
                    await channel.send("Please go back to the profiles channel to type the command, and try again")
                    await asyncio.sleep(20)
                    await channel.delete()
                    return

            msg6 = discord.Embed(color=color, title="Would you like to list any awards?", description="If so, then please enter them now. Do not use commas, periods, etc. to separate as the bot is already setup to do that for you. Please enter them like so, `Awards_one awards_two awards_three`! If you do not want to list any, please enter N/A.")
            await ans5.delete()
            await snd.edit(embed=msg6)
            
            while True:
                ans6 = await self.bot.wait_for("message")
                awards.append(ans6.content)
                if all(x.isprintable() for x in ans6.content):
                    break
                tries += 1
                if tries == 1:
                    return await channel.send(errormsg)
                if tries == 2:
                    return await channel.send(errormsg)
                if tries == 3:
                    await channel.send("Please go back to the profiles channel to type the command, and try again")
                    await asyncio.sleep(20)
                    await channel.delete()
                    return

            msg7 = discord.Embed(color=color, title="Would you like to list any degrees?", description="If so, then please enter them now. DO not use commas, periods, etc. to separate. The bot is already setup to do that for you. Please enter them like so, `degree_one degree_two degree_three`! If you do not want to list any, please enter N/A.")
            await ans6.delete()
            await snd.edit(embed=msg7)
            
            while True:
                ans7 = await self.bot.wait_for("message")
                degrees.append(ans7.content)
                if all(x.isprintable() for x in ans7.content):
                    break
                tries += 1
                if tries == 1:
                    return await channel.send(errormsg)
                if tries == 2:
                    return await channel.send(errormsg)
                if tries == 3:
                    await channel.send("Please go back to the profiles channel to type the command, and try again")
                    await asyncio.sleep(20)
                    await channel.delete()
                    return

            final_message = discord.Embed(color=color, timestamp=timestamp, title=f"Profile For: {member.name}", description=f"Programming For: {ans1.content}\nPreferred Language: {ans2.content}\nFavorite Language: {ans3.content}\nKnown Languages: {', '.join(languages)}\nCertifications: {', '.join(certifications)}\nAwards: {', '.join(awards)}\nDegrees: {', '.join(degrees)}")
            final_message.set_thumbnail(url=ctx.author.avatar_url)

            final_message2 = discord.Embed(color=color, timestamp=timestamp, title=":red_circle:**___ATTENTION___**:red_circle:", description="This window will automatically close in 10 seconds. You can find your profile in the #profiles channel!")
            final_message2.set_thumbnail(url=ctx.author.avatar_url)

            await ans7.delete()
            await snd.edit(embed=final_message2)

            channel1 = self.bot.get_channel(profiles)
            await channel1.send(embed=final_message)

            await asyncio.sleep(10)
            await channel.delete()

        else:
            return await channel.send(errormsg)


def setup(bot):
    bot.add_cog(Profiles(bot))