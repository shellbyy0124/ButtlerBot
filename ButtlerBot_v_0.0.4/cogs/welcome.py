import discord
import json
import random
import datetime

from discord.ext import commands
from discord.ext.commands import Cog

with open('/home/shellbyy/Desktop/repofolder/Mekasu/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
BOTOUTPUT = data["BOTOUTPUT"]
KPT = data["KasMek_Programming_Team"]



class DMUser(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):

        color = random.randint(0, 0xFFFFFF)

        welcome = discord.Embed(color=color, title=f"Hi and Welcome!", value=f"My name is {self.bot.user.name}, and I will be your virtual assistant during your stay here at the Learning Together Discord Community! :smile:", inline=False)
        welcome.add_field(name="To Get Started:", value=f"You must be a member of {self.bot.get_guild(KPT)} for at least 5 minutes before being able to chat with the community, so in the meantime I would like to cover some ground rules:", inline=False)
        welcome.add_field(name="First:", value="Respect of your peers is a must at all times.", inline=False)
        welcome.add_field(name="Second:", value="Making someone feel inferior to your is prohibited!", inline=False)
        welcome.add_field(name="Third:", value="Telling someone that their question is stupid is prohibited.", inline=False)
        welcome.add_field(name="Fourth", value="No Spamming! This includes: using the @ ability when there are sufficient support channels for your needs", inline=False)
        welcome.add_field(name="Fifth:", value="We have members of all ages that are welcome into this discord. No Cursing: NSFW: etc! It is prohibited!", inline=False)
        welcome.add_field(name="Sixth:", value="Keep the chats in accordance with the channels topic. Not sure? Look Up :smile:", inline=False)
        welcome.add_field(name="Seventh:", value="No Intimidation! We grow and learn together from day one and on", inline=False)
        welcome.add_field(name="Eighth:", value="Use the proper markups when submitting code. Discord supports many languages!", inline=False)
        welcome.add_field(name="And Finally:", value="If you have any more questions, use `>buttlerhelp` to call me, and if you'd like to get a better look at the rules, `>buttlerrules`", inline=False)
        welcome.set_thumbnail(url=self.bot.user.avatar_url)
        welcome.timestamp=datetime.datetime.now()
        await member.send(embed=welcome)

    @commands.Cog.listener()
    async def on_member_leave(self, member:discord.Member):

        channel = self.bot.get_channel(779290533155176465)
        await channel.send(f'{member.mention} has left the server')

    
 
def setup(bot):
    bot.add_cog(DMUser(bot))