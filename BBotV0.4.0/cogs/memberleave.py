import discord
import json

from discord.ext import commands
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

members_leave = data["channels"]["members_leave"]

class MemberLeave(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):

        channel = self.bot.get_channel(members_leave)
        await channel.send(f"{member.mention} has left the server. It's going to be a sad time while you're gone :'(")

def setup(bot):
    bot.add_cog(MemberLeave(bot))