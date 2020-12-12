import discord
import json

from discord.ext import commands
from discord.ext.commands import Cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

staff_commands = data["staff_commands"]

class DevCommands(commands.Cog):

    def __init__(self, bot):
        
        self.bot=bot
    
    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Team Leader')
    async def blistall(self, ctx):

        text = []
        channel = self.bot.get_channel(staff_commands)
        for role in ctx.guild.roles[1:]:
            if not role.managed:
                if role.name != "Bots":
                    if role.name != "muted":
                        list_of_names = [user.name for user in role.members] 
                        text.append(f'{role.name}: {", ".join(list_of_names)}')
        await channel.send("\n".join(text))

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
    print('Development cog has loaded...')
    bot.add_cog(DevCommands(bot))