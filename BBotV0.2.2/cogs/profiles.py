import discord
import json
import DiscordUtils as DU 
import random
import datetime
import asyncio

from discord.ext import commands
from discord.ext.commands import cog 

# switch me to database
with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

profiles = data["channels"]["profiles"]

class Profiles(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.time = datetime.datetime.utcnow()
        self.color = random.randint(0, 0xFFFFFF)

    @commands.command(aliases=['bcprofile'])
    async def createprofile(self, ctx):

        await ctx.message.delete()

        a = await ctx.send(":red_circle:**__A NEW TEXT CHANNEL UNDER THE PROFILES CATEGORY HAS BEEN OPENED IN YOUR NAME TO CONTINUE YOUR PROFILE!__**:red_circle:")
        member = ctx.author
        preferred_languages= []
        languages = []
        certifications = []
        awards = []
        degrees = []
        tries = 0
        starting_balance = 1000
        member = ctx.author

        category = discord.utils.get(ctx.guild.categories, name = 'Profile Information')
        channel = await ctx.guild.create_text_channel(ctx.author.display_name, overwrites=None, category=category)

        msg = discord.Embed(color=self.color, timestamp=self.time, title="Welcome to the profile setup! :)", description="""During this setup, I am going to be asking you a series of questions. 
                                                                                                                            This won't take but just a few moments of your time. Please be sure to 
                                                                                                                            read each question, and it's instructions carefully! **__Type ready when 
                                                                                                                            you're ready__**\n**___NOTE___**\n**__You only get 3 tries on an incorrect 
                                                                                                                            input. After 3 incorrect tries, it will delete the channel, and you will need 
                                                                                                                            to go back to #profiles to start over!__**""") 
        snd = await channel.send(embed=msg)
        ans = await self.bot.wait_for('message')

        if ans.content == "ready":
            await a.delete()

            msg1 = discord.Embed(color=self.color, timestamp=self.time, title="How long have you been programming for?")
            await ans.delete()
            await snd.edit(embed=msg1)
            
            while True:
                ans1 = await self.bot.wait_for("message")
                if all(x.isprintable() for x in ans1.content):
                    break
                tries += 1
                if tries == 1:
                    errormsg = "That is not a valid entry. Please try again!"
                    return await channel.send(errormsg)
                if tries == 2:
                    errormsg = "That is not a valid entry. Please try again!"
                    return await channel.send(errormsg)
                if tries == 3:
                    await channel.send("Please go back to the profiles channel to type the command, and try again")
                    await asyncio.sleep(20)
                    await channel.delete()
                    return

            msg2 = discord.Embed(color=self.color, timestamp=self.time, title="What is your preferred programming language(s)?")
            await ans1.delete()
            await snd.edit(embed=msg2)
            
            while True:
                ans2 = await self.bot.wait_for("message")
                if all(x.isprintable() for x in ans2.content):
                    break
                tries += 1
                if tries == 1:
                    errormsg = "That is not a valid entry. Please try again!"
                    return await channel.send(errormsg)
                if tries == 2:
                    errormsg = "That is not a valid entry. Please try again!"
                    return await channel.send(errormsg)
                if tries == 3:
                    await channel.send("Please go back to the profiles channel to type the command, and try again")
                    await asyncio.sleep(20)
                    await channel.delete()
                    return

            msg3 = discord.Embed(color=self.color, timestamp=self.time, title="What is your favorite programming language?")
            await ans2.delete()
            await snd.edit(embed=msg3)
            
            while True:
                ans3 = await self.bot.wait_for("message")
                preferred_languages.append(ans3.content)
                if all(x.isprintable() for x in ans3.content):
                    break
                tries += 1
                if tries == 1:
                    errormsg = "That is not a valid entry. Please try again!"
                    return await channel.send(errormsg)
                if tries == 2:
                    errormsg = "That is not a valid entry. Please try again!"
                    return await channel.send(errormsg)
                if tries == 3:
                    errormsg = "That is not a valid entry. Please try again!"
                    await channel.send("Please go back to the profiles channel to type the command, and try again")
                    await asyncio.sleep(20)
                    await channel.delete()
                    return

            msg4 = discord.Embed(color=self.color, timestamp=self.time, title="Would you like to list any languages that you know and use?", description="If so, then please enter them now. If you do not want to list any, please enter N/A.")
            await ans3.delete()
            await snd.edit(embed=msg4)
            
            while True:
                ans4 = await self.bot.wait_for("message")
                languages.append(ans4.content)
                if all(x.isprintable() for x in ans4.content):
                    break
                tries += 1
                if tries == 1:
                    errormsg = "That is not a valid entry. Please try again!"
                    return await channel.send(errormsg)
                if tries == 2:
                    errormsg = "That is not a valid entry. Please try again!"
                    return await channel.send(errormsg)
                if tries == 3:
                    await channel.send("Please go back to the profiles channel to type the command, and try again")
                    await asyncio.sleep(20)
                    await channel.delete()
                    return

            msg5 = discord.Embed(color=self.color, timestamp=self.time, title="Would you like to list any certifications?", description="If so, then please enter them now. If you do not want to list any, please enter N/A.")
            await ans4.delete()
            await snd.edit(embed=msg5)
            
            while True:
                ans5 = await self.bot.wait_for("message")
                certifications.append(ans5.content)
                if all(x.isprintable() for x in ans5.content):
                    break
                tries += 1
                if tries == 1:
                    errormsg = "That is not a valid entry. Please try again!"
                    return await channel.send(errormsg)
                if tries == 2:
                    errormsg = "That is not a valid entry. Please try again!"
                    return await channel.send(errormsg)
                if tries == 3:
                    await channel.send("Please go back to the profiles channel to type the command, and try again")
                    await asyncio.sleep(20)
                    await channel.delete()
                    return

            msg6 = discord.Embed(color=self.color, timestamp=self.time, title="Would you like to list any awards?", description="If so, then please enter them now. If you do not want to list any, please enter N/A.")
            await ans5.delete()
            await snd.edit(embed=msg6)
            
            while True:
                ans6 = await self.bot.wait_for("message")
                awards.append(ans6.content)
                if all(x.isprintable() for x in ans6.content):
                    break
                tries += 1
                if tries == 1:
                    errormsg = "That is not a valid entry. Please try again!"
                    return await channel.send(errormsg)
                if tries == 2:
                    errormsg = "That is not a valid entry. Please try again!"
                    return await channel.send(errormsg)
                if tries == 3:
                    await channel.send("Please go back to the profiles channel to type the command, and try again")
                    await asyncio.sleep(20)
                    await channel.delete()
                    return

            msg7 = discord.Embed(color=self.color, timestamp=self.time, title="Would you like to list any degrees?", description="If so, then please enter them now. If you do not want to list any, please enter N/A.")
            await ans6.delete()
            await snd.edit(embed=msg7)
            
            while True:
                ans7 = await self.bot.wait_for("message")
                degrees.append(ans7.content)
                if all(x.isprintable() for x in ans7.content):
                    break
                tries += 1
                if tries == 1:
                    errormsg = "That is not a valid entry. Please try again!"
                    return await channel.send(errormsg)
                if tries == 2:
                    errormsg = "That is not a valid entry. Please try again!"
                    return await channel.send(errormsg)
                if tries == 3:
                    await channel.send("Please go back to the profiles channel to type the command, and try again")
                    await asyncio.sleep(20)
                    await channel.delete()
                    return

            final_message = discord.Embed(color=self.color, timestamp=self.time, title=f"Profile For: {member.display_name}", description=f"Programming For: {ans1.content}\nPreferred Language: {ans2.content}\nFavorite Language: {ans3.content}\nKnown Languages: {', '.join(languages)}\nCertifications: {', '.join(certifications)}\nAwards: {', '.join(awards)}\nDegrees: {', '.join(degrees)}\nAccount Balance: {starting_balance}")
            final_message.set_thumbnail(url=ctx.author.avatar_url)

            final_message2 = discord.Embed(color=self.color, timestamp=self.time, title=":red_circle:**___ATTENTION___**:red_circle:", description="This window will automatically close in 10 seconds. You can find your profile in the #profiles channel!")
            final_message2.set_thumbnail(url=ctx.author.avatar_url)

            await ans7.delete()
            await snd.edit(embed=final_message2)

            channel1 = self.bot.get_channel(profiles)
            await channel1.send(embed=final_message)

            with open('./master.json', 'r', encoding='utf-8-sig') as f:
                data= json.load(f)

            info = data["users"][str(member.name)][{"id" : int(member.id), "bank" : 1000, "roles" : str(member.roles)}]

            with open('./master.json', 'w', encoding='utf-8-sig') as fw:
                json.dump(data, info, indent=4)

            await asyncio.sleep(10)
            await channel.delete()

        else:
            errormsg = "That is not a valid entry. Please try again!"
            await channel.send(errormsg)


"""
ADD SECOND COMMAND TO BE ABLE TO PULL UP PROFILE
ADD SECOND COMMAND AFTER EXPERIENCE BOT IS FINISHED AND A LEVEL DISPLAY HAS BEEN INCORPORATED
"""


def setup(bot):
    bot.add_cog(Profiles(bot))