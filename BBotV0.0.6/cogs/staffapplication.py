from os import error
import discord
import json
import random

from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands.core import check

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

BOTOUTPUT = data["BOTOUTPUT"]
kastien = data["kastien"]
mekasu = data["mekasu"]
TheOnlyCarl = data["TheOnlyCarl"]
KPT = data["KPT"]

class StaffApplication(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command(aliases=['bsapp'])
    async def staffapplication1(self, ctx):

        number = random.randint(100000, 999999)

        member = self.bot.get_guild(KPT).get_member(ctx.author.id)

        first_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Welcome To Your Staff Application, {member.name}", description="All applicants will start as a Community Helper").add_field(name="\u200b", value="You will have to work your way up. The purpose of this application is for us to get to know our applicants better as they transition into staff members. Type `Ready` when you're ready.")

        msg1 = await member.send(embed=first_message)
        answer1 = await self.bot.wait_for('message')

        if answer1.content.lower() == "ready":
            pass
        else:
            return await member.send("Please Enter 'Ready'")
            # some code to restart function from here



        second_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Application:", description=f"Name: {ctx.author.name}\n\nWhat is your age?")

        await msg1.edit(embed=second_message)
        def check(m):
            return m.author.id == member.id

        answer2 = await self.bot.wait_for('message', check=check)

        age1 = 16

        if int(answer2.content) < age1:
            
            return await member.send(f"Apologies {ctx.author.name}, but you must be at least 16 year's old to apply for staff within this community")
            # some code to restart the function from here

        third_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f'Application:').add_field(name="\u200b", value=f'Name: {ctx.author.name}\nAge: {int(answer2.content)}\n\n\nWhy do you believe you would make a great asset to the ButtlerBot staff team?')
        await msg1.edit(embed=third_message)
        def check(m):
            return m.author.id == member.id

        answer3 = await self.bot.wait_for('message')

        if all(x.isalpha() or x.isspace() for x in answer3.content):
            pass
        else:
            return await member.send("That is not a valid entry, Try Again!")
            # some code to restart function from here

        fourth_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f'Finished!', description=f'Congratulations, {ctx.author.name}! Your application has been submitted to the staff, and your Application Reference Number is {number}')
        await msg1.edit(embed=fourth_message)

        roles = self.bot.get_guild(KPT).get_member(member.id).roles
        list_names = [role.name for role in roles]

        final_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Application: Status Complete", description=f"""Buttler Staff Application For: {ctx.author.name}
                                                                                                        Application Number: {number}
                                                                                                        Discord Name: {ctx.author}
                                                                                                        Discord ID: {ctx.author.id}
                                                                                                        Age: {answer2.content}
                                                                                                        Current Roles: {', '.join(list_names[1:])}
                                                                                                        Discord Member Since: {self.bot.get_guild(KPT).get_member(member.id).created_at.strftime("%d/%m/%y %H:%M")}
                                                                                                        {self.bot.get_guild(KPT).name} Member Since: {self.bot.get_guild(KPT).get_member(member.id).joined_at.strftime("%d/%m/%y %H:%M")}""").add_field(name="\u200b", value=f"{answer3.content}")
        channel = self.bot.get_channel(BOTOUTPUT)
        await channel.send(embed=final_message)


                                                                                                            
def setup(bot):
    bot.add_cog(StaffApplication(bot))