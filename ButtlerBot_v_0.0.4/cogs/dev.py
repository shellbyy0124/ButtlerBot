import discord
import json

from discord.ext import commands
from discord.ext.commands import Cog

with open('/home/shellbyy/Desktop/repofolder/Mekasu/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

BOTOUTPUT = data["BOTOUTPUT"]

class DevCommands(commands.Cog):

    def __init__(self, bot):
        
        self.bot=bot
    
    @commands.command(aliases=["buttlerlisteveryone"])
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Team Leader')
    async def listall(self, ctx):
        
        members = []

        for m in ctx.guild.members:
            if not m.bot:
                members.append(m.name)
        await ctx.send(', '.join(members))

        roles = []

        for r in ctx.guild.roles:
            if r == "Bots":
                pass
            else:
                roles.append(r.name)

        await ctx.send(', '.join(roles[1:] + members))


    @commands.command(aliases=["buttlerlistmembers"])
    @commands.has_any_role('Owner', 'Head Dev', 'Team Leader')
    async def listmembers(self, ctx):
        
        members = []

        for m in ctx.guild.members:
            if not m.bot:
                members.append(m.name)
        await ctx.send(', '.join(members))

def setup(bot):
    bot.add_cog(DevCommands(bot))