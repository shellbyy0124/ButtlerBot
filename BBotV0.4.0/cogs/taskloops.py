import discord
import asyncio
import json

from discord.ext import commands, tasks
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

ID = data["guild"]["LT"]
class TaskLoops(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.changepresence.start()

    @tasks.loop(seconds=30)
    async def changepresence(self):

        await self.bot.wait_until_ready()
        count = self.bot.get_guild(ID)

        await self.bot.change_presence(activity=discord.Game(name="Staff Applications Are Now Open!")) 
        await asyncio.sleep(30)       
        await self.bot.change_presence(activity=discord.Game(name=f"Total Members: {count.member_count}"))
        await asyncio.sleep(30)
        await self.bot.change_presence(activity=discord.Game(name="prefix = >"))
        await asyncio.sleep(30)
        await self.bot.change_presence(activity=discord.Game(name="If you can't remember, type >bhelp"))
        await asyncio.sleep(30)
        await self.bot.change_presence(activity=discord.Game(name="Released: 12/02/2020 By: Mekasu & Kastien"))
        await asyncio.sleep(30)
        await self.bot.change_presence(activity=discord.Game(name="Team Members: Mekasu, KataReborn, KortaPo"))
        await asyncio.sleep(30)

def setup(bot):
    bot.add_cog(TaskLoops(bot))