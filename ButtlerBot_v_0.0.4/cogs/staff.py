import DiscordUtils as DiscordUtils
import discord
import json
import asyncio
import os
import datetime

from os import error
from discord import member
from discord.ext import commands
from discord.ext.commands import cog
from discord.utils import get
from isort import logo

with open('/home/shellbyy/Desktop/repofolder/Mekasu/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
BOTOUTPUT = data["BOTOUTPUT"]
mekasu = data["mekasu"]
kastien = data["kastien"]

class Administration(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

#* fix commented out lines. it's supposed to print the bots we use in the discord
    @commands.command(aliases=["buttlerstats"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def serverinfo(self, ctx):
        role_count = len(ctx.guild.roles)
        # bots = discord.utils.get(ctx.guild.roles([member.mention for member in role.members if member.bot]))  
        emoji_count = len(ctx.guild.emojis)
        channel_count = len([x for x in ctx.guild.channels if isinstance(x, discord.channel.TextChannel)])
        embed2 = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
        embed2.add_field(name='Name (ID)', value=f"{ctx.guild.name} ({ctx.guild.id})", inline=False)
        embed2.add_field(name='Owner', value=ctx.guild.owner.display_name, inline=False)
        embed2.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
        embed2.add_field(name='Highest role', value=ctx.guild.roles[-1], inline=False)
        embed2.add_field(name='Role Members', value=f'{self.bot.get_user(mekasu).display_name} {self.bot.get_user(kastien).display_name}', inline=False)
        embed2.add_field(name='Number of roles', value=str(role_count), inline=False)
        embed2.add_field(name='Members', value=ctx.guild.member_count, inline=False)
        # embed2.add_field(name='Bots', value=(bots))
        embed2.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed2.set_thumbnail(url=ctx.guild.icon_url)
        embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed2.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed2)

#* add in reason

    @commands.command(aliases=["buttlerchangenick"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def changemembernickname(self, ctx, member:discord.Member, nick):
        existing_nick = member.display_name
        new_nick = await member.edit(nick=nick)
        nickembed = discord.Embed(color=ctx.author.color, title="**Inappropriate Nick Name!").add_field(name="\u200b", value=f"{member.name}, you have chosen an inappropriate nickname. The offending name is: '{existing_nick}, and it has been changed to; {nick}")
        await member.send(embed=nickembed)

    @commands.command(aliases=["buttlerpurge"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount:int):
        await ctx.channel.purge(limit=amount)
        msg = await ctx.send(f"{self.bot.user.name} has purged {amount} messages from this channel!")
        await asyncio.sleep(10)
        await msg.delete()

    @commands.command(aliases=["buttlerwhois"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def whois(self, ctx, user: discord.Member):
        user = user or ctx.author
        if user is None:
            user = ctx.message.author
        if user.activity is not None:
            game = user.activity.name
        else:
            game = None
        voice_state = None if not user.voice else user.voice.channel
        embed1 = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
        embed1.add_field(name='User ID', value=user.id, inline=True)
        embed1.add_field(name='Nick', value=user.nick, inline=True)
        embed1.add_field(name='Status', value=user.status, inline=True)
        embed1.add_field(name='On Mobile', value=user.is_on_mobile(), inline=True)
        embed1.add_field(name='In Voice', value=voice_state, inline=True)
        embed1.add_field(name='Game', value=game, inline=True)
        embed1.add_field(name='Highest Role', value=user.top_role.name, inline=True)
        embed1.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        embed1.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        embed1.set_thumbnail(url=user.avatar_url)
        embed1.set_author(name=user.name, icon_url=user.avatar_url)
        embed1.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed1)

    @commands.command(aliases=["buttlerlock"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def lock(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(f'{self.bot.user.name} has locked this channel.')

    @commands.command(aliases=["buttlerunlock"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def unlock(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(f'{self.bot.user.name} has unlocked this channel.')

#* fix me - TypeError: sequence item 0: expected str instance, list found

    @commands.command(aliases=["buttlerlistmembers"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def listmembers(self, ctx):
        
        members = []
        for m in ctx.guild.members:
            if not m.bot:
                members.append(m.name)

        stuff1 = discord.Embed(color=discord.Colour.purple(), title=f"Members:", description=f"""{(", ".join([members]))}""")
        stuff1.timestamp = datetime.datetime.utcnow()

        channel = self.bot.get_channel(BOTOUTPUT)
        # await channel.send(", ".join(members))
        await channel.send(embed=stuff1)


def setup(bot):
    bot.add_cog(Administration(bot))