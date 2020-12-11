import discord
import json
import sqlite3

from discord.ext import commands
from discord.ext.commands import Cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
BOTOUTPUT = data["BOTOUTPUT"]
staff_commands = data["staff_commands"]

class DevCommands(commands.Cog):

    def __init__(self, bot):
        
        self.bot=bot

#* fix me. prints on every loop
    
    # @commands.command()
    # @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Team Leader')
    # async def blistall(self, ctx):

    #     names = []

    #     for role.name in ctx.guild.roles:
    #         if not role.managed:
    #             list_of_names = [user.name for user in role.members]
    #             names.append(list_of_names)

    #     channel = self.bot.get_channel(staff_commands)
    #     await channel.send(f'{role.name}: {names}')

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Team Leader', 'Dev')
    async def blistmem(self, ctx):
        
        members = []

        for m in ctx.guild.members:
            if not m.bot:
                members.append(m.name)

        channel = self.bot.get_channel(staff_commands)
        await channel.send(', '.join(members))


    @commands.command()
    @commands.has_any_role('Owner', 'Team Leader', 'Head Dev', 'Dev')
    async def blistroles(self, ctx):
        roles = []
        for r in ctx.guild.roles:
            if not r.managed:

                roles.append(r)
        channel = self.bot.get_channel(staff_commands)
        await channel.send(", ".join(role.name for role in ctx.guild.roles[1:] if not role.managed and role.name != "Bots"))


def setup(bot):
    bot.add_cog(DevCommands(bot))