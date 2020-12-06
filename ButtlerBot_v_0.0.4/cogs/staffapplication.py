import discord
import json

from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands.core import check

with open('/home/shellbyy/Desktop/repofolder/Mekasu/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

BOTOUTPUT = data["BOTOUTPUT"]

class StaffApplication(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command(aliases=['buttlerstaffapp1'])
    async def staffapplication1(self, ctx):

        member = ctx.author

        embed1 = discord.Embed(color=discord.Colour.purple(), title="Welcome To Your Staff Application.", description="Please answer all questions fully, accurately, and honestly. Type `Ready` when you're ready.")
        embed2 = discord.Embed(color=discord.Colour.red(), title="Question 1:", description="Please Enter Your Discord Name: (name#0000)")
        errormsg = "Sorry, but you have entered an invalid name. please try again:"
        embed3 = discord.Embed(color=discord.Colour.blue(), title="Question 2:", description="Please Enter Your Email (email@email.com)")
        embed4 = discord.Embed(color=discord.Colour.green(), title="Question 3:", description="What makes you believe you would be an asset to the staff team?")
        embed5 = discord.Embed(color=discord.Colour.from_rgb(0, 255, 255), title="Question 4:", description=f"How long have you been in {ctx.guild.name}?")

        await member.send(embed=embed1)
        answer1 = await self.bot.wait_for('message')

        if answer1 == 'Ready':
            
            await member.send(embed=embed2)
            answer2 = self.bot.wait_for('message')

            if answer2 == member:

                await member.send(embed=embed3)
                # answer3 = await self.bot.wait_for('message')

                # if answer3 == :

                #     await member.send(embed=embed4)
                #     answer4 = await self.bot.wait_For('message')

                #     if answer4 == :

                #         await member.send(embed=embed5)
                #         answer5 = await self.bot.wait_for('message')

        else:

            await member.send(errormsg)
            await member.send(embed=embed2)


def setup(bot):
    bot.add_cog(StaffApplication(bot))