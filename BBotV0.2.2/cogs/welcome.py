import discord
import json
import random
import datetime
import asyncio

from discord.ext import commands
from discord.ext.commands import Cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

members_join_and_leave = data["members_join_and_leave"]
LT = data["LT"]

class DMUser(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):

        color = random.randint(0, 0xFFFFFF)
        timestamp = datetime.datetime.utcnow()

        welcome = discord.Embed(color=color, timestamp=timestamp, title=f"Hi and Welcome!", value=f"My name is {self.bot.user.name}, and I will be your virtual assistant during your stay here at the Learning Together Discord Community! :smile:", inline=False)
        welcome.add_field(name="To Get Started:", value=f"You must be a member of {self.bot.get_guild(LT)} for at least 5 minutes before being able to chat with the community, so in the meantime I would like to cover some ground rules:", inline=False)
        welcome.add_field(name="First:", value="Respect of your peers is a must at all times.", inline=False)
        welcome.add_field(name="Second:", value="Making someone feel inferior to your is prohibited!", inline=False)
        welcome.add_field(name="Third:", value="Telling someone that their question is stupid is prohibited.", inline=False)
        welcome.add_field(name="Fourth", value="No Spamming! This includes: using the @ ability when there are sufficient support channels for your needs", inline=False)
        welcome.add_field(name="Fifth:", value="We have members of all ages that are welcome into this discord. No Cursing: NSFW: etc! It is prohibited!", inline=False)
        welcome.add_field(name="Sixth:", value="Keep the chats in accordance with the channels topic. Not sure? Look Up :smile:", inline=False)
        welcome.add_field(name="Seventh:", value="No Intimidation! We grow and learn together from day one and on", inline=False)
        welcome.add_field(name="Eighth:", value="Use the proper markups when submitting code. Discord supports many languages!", inline=False)
        welcome.add_field(name="And Finally:", value="If you have any more questions, use `>buttlerhelp` to call me, and if you'd like to get a better look at the rules, `>buttlerrules`", inline=False)
        welcome.add_field(name="Note:", value="This message will delete after 5 minutes. Once this message deletes, you will have access to the discord. If not, then please get in touch with a staff member!", inline=False)
        msg = await member.send(embed=welcome)
        channel = self.bot.get_channel(members_join_and_leave)
        await channel.send(f"Let's welcome {member.name} to {self.bot.get_guild(LT).name}!")
        await asyncio.sleep(300)
        await msg.delete()

        with open("test.json") as fp:
            data = json.load(fp)
        if str(member.id) not in data:
            data[str(member.id)] = {"name": member.name, "discrim":member.discriminator}
            with open("test.json","w") as fw:
                json.dump(data,fw)
 
def setup(bot):
    bot.add_cog(DMUser(bot))