from os import error
import discord
import json
import random

from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands.core import check

with open('/home/shellbyy/Desktop/repofolder/Mekasu/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

BOTOUTPUT = data["BOTOUTPUT"]
kastien = data["kastien"]
mekasu = data["mekasu"]
TheOnlyCarl = data["TheOnlyCarl"]

class StaffApplication(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command(aliases=['buttlerstaffapp1'])
    async def staffapplication1(self, ctx):

        member = ctx.author

        first_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Welcome To Your Staff Application, {member}", description="All applicants will start as a Community Helper, and you will have to work your way up. The purpose of this application is for us to get to know our applicants better as they transition into staff members. Type `Ready` when you're ready.")
        errormsg = "Sorry, but you have entered an invalid entry. please try again by starting your application over"

        msg1 = await member.send(embed=first_message)
        answer1 = await self.bot.wait_for('message')

        if answer1.content.lower() == "ready":


            second_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Applicant: {ctx.author.name}\nQuestion 1:", description=f"What is your age?")

            await msg1.edit(embed=second_message)
            answer2 = await self.bot.wait_for('message')

            age1 = 16

            if int(answer2.content) < age1:
                
                return await member.send(f"Apologies {ctx.author.name}, but you must be at least 16 year's old to apply for staff within this community")

            third_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f'Applicant: {ctx.author.name}\nAge: {answer2}\nQuestion 3:', description=f'Why do you believe you would make a great asset to the ButtlerBot staff team?')
            await msg1.edit(embed=third_message)
            answer3 = await self.bot.wait_for('message')

            fourth_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f'Finished!', description=f'Congratulations, {ctx.author.name}! Your application has been submitted to the staff. Your confirmation number is {confirmation_number}')

        
        # final_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"""Buttler Staff Application For: {ctx.author}",
        #                                                                         value=f"Name: {ctx.author.display_name}
        #                                                                         Discord Name: {ctx.author}
        #                                                                         Discord ID: {ctx.author.id}
        #                                                                         Current Roles: {self.bot.get_roles(ctx.author)}
        #                                                                         Discord Member Since: {ctx.author.created_at}
        #                                                                         {ctx.guild.name} Member Since: {ctx.author.joined_at}""")
        # channel = self.bot.get_channel(BOTOUTPUT)
        # await channel.send(embed=final_message)





    

def setup(bot):
    bot.add_cog(StaffApplication(bot))