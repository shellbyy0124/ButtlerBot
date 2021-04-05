import discord
import asyncio
import json
import datetime
import random

from discord.ext import commands
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

members_join = data["channels"]["members_join_and_leave"]
LT = data["guild"]["LT"]
rules_agreement_logs = data["channels"]["rules_agreement_logs"]
errors = data["channels"]["errors"]
profiles = data["channels"]["profiles"]
bot_spam = data["channels"]["bot_spam"]
headdev = data["roles"]["Head Dev"]
dev = data["roles"]["Dev"]

class WelcomingMembers(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.time = datetime.datetime.utcnow()
        self.url = self.bot.user.avatar_url

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):

        starting_balance = 1000

        channel = self.bot.get_channel(bot_spam)

        welcome = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title=f"Hi and Welcome!", description=f"My name is {self.bot.user.name}, and I will be your virtual assistant during your stay here at the Learning Together Discord Community! :smile:", inline=False)
        welcome.add_field(name="To Get Started:", value=f"You must be a member of {self.bot.get_guild(LT)} for at least 5 minutes before being able to chat with the community, so in the meantime I would like to cover some ground rules:", inline=False)
        welcome.add_field(name="First:", value="Respect of your peers is a must at all times. Making someone feel inferior to you is prohibited! Telling someone that their question is stupid is prohibited.", inline=False)
        welcome.add_field(name="Second:", value="No Spamming! This includes: using the @ ability when there are sufficient support channels for your needs", inline=False)
        welcome.add_field(name="Third:", value="We have members of all ages that are welcome into this discord. No Cursing, NSFW, etc! It is prohibited!", inline=False)
        welcome.add_field(name="Fourth", value="Keep the chats in accordance with the channels topic. Not sure? Look Up :smile:", inline=False)
        welcome.add_field(name="Fifth:", value="No Intimidation! We grow and learn together from day one and on", inline=False)
        welcome.add_field(name="Sixth:", value="Use the proper markups when submitting code. Discord supports many languages!", inline=False)
        welcome.add_field(name="Seventh:", value="When posting links in the **_Resources_** category, you may __ONLY__ post links that are pertinent to that channel. Any NSFW gags, hacks, trackers, etc will result in your account getting reported. We have all ages in this group!", inline=False)
        welcome.add_field(name="Eighth:", value=f"Use the {channel.mention} channel for all of your bot commands that are not pertinent with your current conversation, or if you need/want to look something up!", inline=False)
        welcome.add_field(name="Ninth:", value="Do not create your own invite to this discord. An invite link has already been created for you to use. Type `>binvite` for the link", inline=False)
        welcome.add_field(name="And Finally:", value="If you have any more questions, use `>buttlerhelp` to call me, and if you'd like to get a better look at the rules, `>buttlerrules`", inline=False)
        welcome.add_field(name="Note:", value="Please type `!continue` to create your profile for the community :) If you choose not to create a profile, then please type `!noprofile`, but keep in mind that without a profile, majority of the commands, including the minigames commands, will not work for you, and there is nothing that the staff can do to fix it. You will need to leave the discord, and rejoin in order to create a profile. If the command doesn't work, then please get in touch with a staff member by going to the #new_member_support channel for assistance.", inline=False)

        await member.send(embed=welcome)
        msg = await self.bot.wait_for('message')

        if msg.content == "!continue":

            embed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Welcome To The ButtlerBot Profile Creator", description="During this setup, I am going to be asking you a series of questions. This shouldn't take you longer than 5 minutes max to answer all questions. Please be sure to read each question, and it's instructions carefully. Type Ready When you're ready to begin", inline=False).set_thumbnail(url=self.url).set_footer(text="You have 60 seconds to respond, or this command will time out, and you will need to get with a staff member in the #new_member_support channel")
            msg1 = await member.send(embed=embed1)
            ans1 = await self.bot.wait_for('message', timeout=60)

            if ans1.content.lower() == "ready":

                embed2 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="ButtlerBot Profile Creator", description="How long have you been programming for? Example: 1 year 6 months", inline=False).set_thumbnail(url=self.url).set_footer(text="You have 60 seconds to respond, or this command will time out, and you will need to get with a staff member in the #new_member_support channel")
                await msg1.edit(embed=embed2)
                ans2 = await self.bot.wait_for('message', timeout=60)

                if all(i.isprintable() for i in ans2.content):

                    embed3 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="ButtlerBot Profile Creator", description="What is your favorite programming language? If you have multiple, please separate them using commas `,`\nIf not, then enter N/A. No blank answers will be accepted", inline=False).set_thumbnail(url=self.url).set_footer(text="You have 60 seconds to respond, or this command will time out, and you will need to get with a staff member in the #new_member_support channel")
                    await msg1.edit(embed=embed3)
                    ans3 = await self.bot.wait_for('message', timeout=60)

                    if all(i.isprintable() for i in ans3.content):

                        embed4 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="ButtlerBot Profile Creator", description="What is your preferred programming language? If you have multiple, please separate them using a comma `,`\nIf not, then enter N/A. No blank answers will be accepted", inline=False).set_thumbnail(url=self.url).set_footer(text="You have 60 seconds to respond, or this command will timeout, and you will need to get with a staff member in the #new_member_support channel")
                        await msg1.edit(embed=embed4)
                        ans4 = await self.bot.wait_for('message', timeout=60)

                        if all(i.isprintable() for i in ans4.content):
                            
                            embed5 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="ButtlerBot Profile Creator", description="What other languages do you know? If you have multiple, please separate them using a comma `,`\nIf not, then enter N/A. No blank answers will be accepted", inline=False).set_thumbnail(url=self.url).set_footer(text="You have 60 seconds to respond, or this command will timeout, and you will need to get with a staff member in the #new_member_support channel")
                            await msg1.edit(embed=embed5)
                            ans5 = await self.bot.wait_for('message', timeout=60)

                            if all(i.isprintable() for i in ans5.content):
                                
                                embed6 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="ButtlerBot Profile Creator", description="Do you have any certifications that you would like to list? If yes, separate them by commas `,`\nIf not, then enter N/A. No blank answers will be accepted", inline=False).set_thumbnail(url=self.url).set_footer(text="You have 60 seconds to respond, or this command will timeout, and you will need to get with a staff member in the #new_member_support channel")
                                await msg1.edit(embed=embed6)
                                ans6 = await self.bot.wait_for('message', timeout=60)

                                if all(i.isprintable() for i in ans6.content):

                                    embed7 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="ButtlerBot Profile Creator", description="Do you have any awards that you would like to list? if yes, separate them by commas `,`\nIf not, then enter N/A. No blank answers will be accepted", inline=False).set_thumbnail(url=self.url).set_footer(text="You have 60 seconds to respond, or this command will timeout, and you will need to get with a staff member in the #new_member_support channel")
                                    await msg1.edit(embed=embed7)
                                    ans7 = await self.bot.wait_for('message', timeout=60)

                                    if all(i.isprintable() for i in ans7.content):

                                        embed8 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="ButtlerBot Profile Creator", description="Do you have any degrees that you would like to list? if yes, separate them by commas `,`\nIf not, then enter N/A. No blank answers will be acceptaed", inline=False).set_thumbnail(url=self.url).set_footer(text="You have 60 seconds to respond, or this command will timeout, and you will need to get with a staff member in the #new_member_support channel")
                                        await msg1.edit(embed=embed8)
                                        ans8 = await self.bot.wait_for('message', timeout=60)

                                        if all(i.isprintable() for i in ans8.content):

                                            embed9 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title=f"Profile For: {member.display_name}", description=f"""Programming For: {ans2.content}
                                                                                                                                                                                        Favorite Language: {ans3.content}
                                                                                                                                                                                        Preferred Language(s): {ans4.content}
                                                                                                                                                                                        Languages Known: {ans5.content}
                                                                                                                                                                                        Certifications: {ans6.content}
                                                                                                                                                                                        Awards: {ans7.content}
                                                                                                                                                                                        Degrees: {ans8.content}
                                                                                                                                                                                        Account Balance: {starting_balance}""").set_thumbnail(url=member.avatar_url).set_footer(text="If you are satisfied with your profile, please type `!save`, otherwise, you will need to go to the #new_member_support channel")
                                            await msg1.edit(embed=embed9)
                                            ans9 = await self.bot.wait_for('message', timeout=60)

                                            if ans9.content.lower() == "!save":

                                                final_embed = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title=f"Profile For: {member.display_name}", description=f"""Programming For: {ans2.content}
                                                                                                                                                                            Favorite Language: {ans3.content}
                                                                                                                                                                            Preferred Language(s): {ans4.content}
                                                                                                                                                                            Languages Known: {ans5.content}
                                                                                                                                                                            Certifications: {ans6.content}
                                                                                                                                                                            Awards: {ans7.content}
                                                                                                                                                                            Degrees: {ans8.content}
                                                                                                                                                                            Account Balance: {starting_balance}""").set_thumbnail(url=member.avatar_url)

                                                channel = self.bot.get_channel(rules_agreement_logs)
                                                channel1 = self.bot.get_channel(profiles)
                                                await channel.send(f"User, {member.name}, has agreed to the rules on {self.time.__format__('%A, %d. %B %Y @ %H:%M:%S')}")
                                                await channel1.send(embed=final_embed)

                                                with open('./users.json', 'r', encoding='utf-8-sig') as f:
                                                    data = json.load(f)

                                                answers = [ans2, ans3, ans4, ans5, ans6, ans7, ans8]

                                                data["users"][str(member.name)] = {"id" : int(member.id), "bank" : 1000, "points" : 0, "warnings" : 0}

                                                with open('./users.json', 'w', encoding='utf-8-sig') as g:
                                                    data = json.dump(data, g, indent=4)

                                                role = discord.utils.get(member.guild.roles, name="Members")
                                                await member.add_roles(role)
                                                    
        elif msg.content.lower() == "!noprofile":

            embed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Hello, and Welcome!", description=f"Welcome to {LT.name}!").set_thumbnail(url=self.url)
            msg1 = await member.send(embed=embed1)

            role = discord.utils.get(self.ctx.guild.roles, name="Members")
            await member.add_roles(role)

def setup(bot):
    bot.add_cog(WelcomingMembers(bot))