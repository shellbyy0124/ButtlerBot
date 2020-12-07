import discord
import json
import sqlite3

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
    @commands.has_any_role('Owner', 'Head Dev', 'Team Leader', 'Dev')
    async def listmembers(self, ctx):
        
        members = []

        for m in ctx.guild.members:
            if not m.bot:
                members.append(m.name)
        await ctx.send(', '.join(members))


    @commands.command(aliases=['buttlerlistroles'])
    @commands.has_any_role('Owner', 'Team Leader', 'Head Dev', 'Dev')
    async def listroles(self, ctx):
        roles = []
        for r in ctx.guild.roles:
            if not r.managed:

                roles.append(r)
        channel = self.bot.get_channel(BOTOUTPUT)
        await channel.send(", ".join(role.name for role in ctx.guild.roles[1:] if not role.managed and role.name != "Bots"))

#* prints too many times
    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Team Leader', 'Dev')
    async def listall(self, ctx):
        for role in ctx.guild.roles[3:]:
            if not role.managed:

                list3 = discord.Embed(title="Here is a list of all Roles, and Members within each role.")
                list3 = discord.Embed(name=f"{role.name}", description=f"""{(",".join([m.display_name for m in role.members if not m.bot]))}""")

                channel = self.bot.get_channel(BOTOUTPUT)
                await channel.send(embed=list3)

def setup(bot):
    bot.add_cog(DevCommands(bot))