import discord
import json
import datetime

from discord.ext import commands
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

members_leave = data["channels"]["members_join_and_leave"]

class MemberLeave(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):

        embed1 = discord.Embed(color=discord.Colour.blue(), timestamp=datetime.datetime.utcnow(), title=f"So Long Friend!", description=f"It's going to be a sad time while you're gone :'(", inline=False).set_image(url=member.avatar_url)
        channel = self.bot.get_channel(members_leave)
        await channel.send(embed=embed1)


def setup(bot):
    bot.add_cog(MemberLeave(bot))