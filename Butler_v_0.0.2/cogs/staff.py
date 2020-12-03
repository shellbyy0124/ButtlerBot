import DiscordUtils as DiscordUtils
import discord
import json
import aiohttp
import random
import os

from os import error
from discord import member
from discord.ext import commands
from discord.ext.commands import cog
from discord.utils import get
from isort import logo

with open('/home/shellbyy/Desktop/repofolder/Mekasu/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

TOKEN = data["TOKEN"]
STDOUT = data["STDOUT"]
command_prefix = data["command_prefix"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=command_prefix, intents=intents, nickname_command=None)

class Administration(cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="buttleradminhelp")
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def adminhelpmenu(self, ctx, bot):

        adminembed1 = discord.Embed(color=ctx.author.color).add_field(name=f"Hi! I'm {bot.user.name} Staff Menu, and I'm here to help!",
                                                                value="In the pages to follow are things that I am able to currently help you with, and below that is a list of things that I am currently developing to better help you in the future! :smile:")
        adminembed1.set_image(url=bot.user.avatar_url)
        adminembed1.set_footer(text='Page 1/20')
        adminembed2 = discord.Embed(color=ctx.author.color).add_field(name="Server Statistics:",
                                                                value="Want to help us keep up with the server stats? Type /stats to get the pertinent info!")
        adminembed2.set_image(url=bot.user.avatar_url)
        adminembed2.set_footer(text='Page 2/20')
        adminembed3 = discord.Embed(color=ctx.author.color).add_field(name=f"User Inappropriate Nickname?",
                                                                value="Do you see a user with an inappropriate username? then type /changenick <username_as_currently_shown> <actual_name> and the user will automatically be dm'd a message of their nickname being changed. Adding a reason for why will be coming in a future update!")
        adminembed3.set_image(url=bot.user.avatar_url)
        adminembed3.set_footer(text='Page 3/20')
        adminembed4 = discord.Embed(color=ctx.author.color).add_field(name=f"Purging Channels:",
                                                                value="Do Not Abuse This Ability! If you are deleting less than 23 messages, then right click and delete them individually. This command is only for if someone has hacked us, or spammed us! Try not to use this command if you are not an admin or higher. If unsure of when to use it, please ask an admin or higher in the staff chat channel")
        adminembed4.set_image(url=bot.user.avatar_url)
        adminembed4.set_footer(text='Page 4/20')
        adminembed5 = discord.Embed(color=ctx.author.color).add_field(name=f"Who Is Who but a Who!",
                                                                value="Some have an incomprehensible nickname, and you want to know who they are, or need to change their nickname, then type /whois <username> and get that information!")
        adminembed5.set_image(url=bot.user.avatar_url)
        adminembed5.set_footer(text='Page 5/20')
        adminembed6 = discord.Embed(color=ctx.author.color).add_field(name=f"A member being obnixious is the voice, or text channel?",
                                                                value="Type `/tempmute <member_name> <time_in_seconds> <reason>` to mute them")
        adminembed6.set_image(url=bot.user.avatar_url)
        adminembed6.set_footer(text='Page 6/20')

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction('⏮️', "first")
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('⏭️', "last")
        adminembeds = [adminembed1, adminembed2, adminembed3, adminembed4, adminembed5, adminembed6]
        await paginator.run(adminembeds)

    @commands.command(name='buttlerstats')
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def serverinfo(self, ctx):
        role_count = len(ctx.guild.roles)
        emoji_count = len(ctx.guild.emojis)
        channel_count = len([x for x in ctx.guild.channels if isinstance(x, discord.channel.TextChannel)])
        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.add_field(name='Name (ID)', value=f"{ctx.guild.name} ({ctx.guild.id})", inline=False)
        embed.add_field(name='Owner', value=ctx.guild.owner, inline=False)
        embed.add_field(name='Members', value=ctx.guild.member_count, inline=False)
        embed.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
        embed.add_field(name='Highest role', value=ctx.guild.roles[-1], inline=False)
        embed.add_field(name='Number of roles', value=str(role_count), inline=False)
        embed.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name="buttlerchangenick")
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def changemembernickname(self, ctx, member:discord.Member, nick):
        existing_nick = member.display_name
        new_nick = await member.edit(nick=nick)
        nickembed = discord.Embed(colour=0xFB2605, title="**Inappropriate Nick Name!").add_field(name="\u200b", value=f"{member.name}, you have chosen an inappropriate nickname. The offending name is: '{existing_nick}, and it has been changed to; {new_nick}")
        await member.send(embed=nickembed)

    @commands.command(name="buttlerpurge")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount:int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{bot.user.name} has purged {amount} messages from this channel!")

    @commands.command(name='buttlerwhois')
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
        embed = discord.Embed(timestamp=ctx.message.created_at)
        embed.add_field(name='User ID', value=user.id, inline=True)
        embed.add_field(name='Nick', value=user.nick, inline=True)
        embed.add_field(name='Status', value=user.status, inline=True)
        embed.add_field(name='On Mobile', value=user.is_on_mobile(), inline=True)
        embed.add_field(name='In Voice', value=voice_state, inline=True)
        embed.add_field(name='Game', value=game, inline=True)
        embed.add_field(name='Highest Role', value=user.top_role.name, inline=True)
        embed.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        embed.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_author(name=user.name, icon_url=user.avatar_url)
        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name='buttlerlock')
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def lock(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(f'{bot.user.name} has locked this channel.')

    @commands.command(name='buttlerunlock')
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def unlock(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(f'{bot.user.name} has unlocked this channel.')

    @commands.command(name='buttlerlistmembers')
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def listmembers(self, ctx, datetime):
        now = datetime.datetime.now()+datetime.timedelta(minutes=5)
        members = []
        for m in ctx.guild.members:
            if not m.bot:
                members.append(m.name)

                #stuff1 = discord.Embed(timestamp=now, color=discord.Colour.purple(), title=f"Members:", description=f"""{(", ".join([members]))}""")

        channel = bot.get_channel(Stdout)
        await channel.send(", ".join(members))


def setup(bot):
    bot.add_cog(Administration(bot))