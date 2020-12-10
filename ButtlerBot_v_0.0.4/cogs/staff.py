import DiscordUtils as DiscordUtils
import discord
import json
import asyncio
import os
import datetime
import random

from os import error
from discord import member
from discord.ext import commands
from discord.ext.commands import cog
from discord.utils import get
from isort import logo

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
BOTOUTPUT = data["BOTOUTPUT"]
mekasu = data["mekasu"]
kastien = data["kastien"]

class Administration(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["bstats"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admins', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def serverinfo(self, ctx):

        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
                
        
        embed2 = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
        embed2.add_field(name='Name', value=f"{ctx.guild.name}", inline=False)
        embed2.add_field(name='Owner', value=f"{self.bot.get_user(mekasu).display_name}, {self.bot.get_user(kastien).display_name}", inline=False)
        embed2.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
        embed2.add_field(name='Highest role', value=ctx.guild.roles[-1], inline=False)
        embed2.add_field(name='Role Members', value=f'{self.bot.get_user(mekasu).display_name} {self.bot.get_user(kastien).display_name}', inline=False)
        embed2.add_field(name='Number of roles', value=str(role_count), inline=False)
        embed2.add_field(name='Number Of Members', value=ctx.guild.member_count, inline=False)
        embed2.add_field(name='Bots:', value=(', '.join(list_of_bots)))
        embed2.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed2.set_thumbnail(url=ctx.guild.icon_url)
        embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed2.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed2)

    @commands.command(aliases=["bcnick"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admins', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def changemembernickname(self, ctx, member:discord.Member, nick, reason):
        existing_nick = member.display_name
        new_nick = await member.edit(nick=nick)
        nickembed = discord.Embed(color=ctx.author.color, title="**Inappropriate Nick Name!").add_field(name="\u200b", value=f"{member.name}, you have chosen an inappropriate nickname. The offending name is: '{existing_nick}, and it has been changed to; {nick}, because {reason}")
        await member.send(embed=nickembed)

    @commands.command(aliases=["bpurge"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount:int):
        await ctx.channel.purge(limit=amount)
        msg = await ctx.send(f"{self.bot.user.name} has purged {amount} messages from this channel!")
        await asyncio.sleep(10)
        await msg.delete()

    @commands.command(aliases=["bwhois"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admins', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
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

    @commands.command(aliases=["block"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admins', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def lock(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(f'{self.bot.user.name} has locked this channel.')

        await member.send(f"We have been spammed/hacked within the discord community. {ctx.author} has locked down {channel}")

    @commands.command(aliases=["bunlock"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admins', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def unlock(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(f'{self.bot.user.name} has unlocked this channel.')


    @commands.command(aliases=['bwarn'])
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Head Admin', 'Admins', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def warn(self, ctx, member:discord.Member, reason):

        warn = discord.Embed(color = discord.Colour.orange(), title=f'{ctx.author} has sent you a warning!').add_field(name="\u200b", value=f'{reason}', inline=False)
        warn1 = discord.Embed(color = discord.Colour.orange(), title=f'{ctx.author} has sent a warning to {member} for {reason}', inline=False)

        await member.send(embed=warn)
        channel = self.bot.get_channel(BOTOUTPUT)
        await channel.send(embed=warn1)

#* needs fixing

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def btempmute(self, ctx, member:discord.Member, time:int, *, reason=None):

        tempmute1 = discord.Embed(colour = discord.Colour.red(), title="Tempmute",description=f"{member.name} was muted by {ctx.author.name}").add_field(name="\u200b", value=f'{reason} for {time}seconds')
        tempmute1.timestamp = datetime.datetime.utcnow()

        channel = self.bot.get_channel(BOTOUTPUT)
        await channel.send(embed = tempmute1)

        muted_role = discord.utils.get(ctx.guild.roles,name="muted")
        roles = self.server.get_member(member.id).roles
        user_roles = [role.name for role in roles]

        tempmute2 = discord.Embed(colour = discord.Colour.red(), title =f"You Have been Muted!", description=f"you have been muted for {time}, because {reason}")
        tempmute2.timestamp = datetime.datetime.utcnow()

        msg1 = await member.send(emed=tempmute2)
        await member.remove_roles(user_roles, reason=reason)
        await member.add_roles(muted_role,reason=reason)

        await asyncio.sleep(time)

        await member.remove_roles(muted_role)
        await member.add_roles(user_roles)

        tempmute3 = discord.Embed(color=discord.Colour.green(), title="You Have Been Unmuted. Please Continue With Your Activities :)")
        
        await msg1.edit(embed=tempmute3)

        number1 = random.randint(100000, 999999)

        if time > 1800:

            appealembed1 = discord.Embed(color=discord.Colour.blue(), title="Your tempmute time is greater than 30 minutes. If you would like to submit an appeal, please type `appeal`.")
            appealembed1.timestamp = datetime.datetime.utcnow()
            await member.send(embed=appealembed1)

            appeal1 = await self.bot.wait_for('message')

            if appeal1.content == "appeal":
                pass
            else:
                return await member.send("Please Enter `appeal`!")
                #some code to restart function from here

            appealembed2 = discord.Embed(color=discord.Colour.blue(), title=f"Appeal {number1}", description=f"Name: {member.name}\nAppeal Number: {number1}")
            appealembed2.timestamp = datetime.datetime.utcnow()

            await appeal1.edit(embed=appealembed2)

            appeal2 = await self.bot.wait_for('message')

            if all(x.isalpha() or x.isspace() for x in appeal2.content):
                pass
            else:
                return await member.send("That is not a valid entry, Please Try Again!")
                #some code to restart function from here
        
        
    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def bannounce(self, ctx):

        ann1 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Buttler Announcement Editor:", description="What channel is your announcement for?\n\nEnter A for Bot Updates\nEnter B for Community Updatess")
        
        ques1 = await ctx.send(embed=ann1)
        ans1 = await self.bot.wait_for('message')

        A = "a"
        B = "b"

        if ans1.content.lower() == A:

            ques2 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Please enter the name of the announcement.")
            await ques1.edit(embed=ques2)
            ans2 = await self.bot.wait_for('message')

            ques3 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Please enter your announcement")
            await ques1.edit(embed=ques3)
            ans3 = await self.bot.wait_for('message')

            if all(x.isalpha() or x.isspace() for x in ans2.content):
                pass
            else:
                return await member.send("That is not a valid entry, Try Again!")
                # some code to restart function from here

        
            finale = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"**___ANNOUNCEMENT___**:")
            finale.add_field(name=f"{ans2.content}", value=f"{ans3.content}")

            await ans1.delete()
            await ques1.delete()
            await ans2.delete()
            await ans3.delete()
            
            channel = self.bot.get_channel(BOTOUTPUT)
            await channel.send(embed=finale)

        elif ans1.content.lower() == B:
            
            ques4 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Please enter the name of the announcement.")
            await ques1.edit(embed=ques4)
            ans4 = await self.bot.wait_for('message')

            if all(y.isalpha() or y.isspace() for y in ans4.content):
                pass
            else:
                return await ctx.send("Sorry that is not a valid announcement. Please run the command again.")
                # some code to restart function from here

            ques5 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Please enter the announcement")
            await ques1.edit(embed=ques5)
            ans5 = await self.bot.wait_for('message')

            finale2 = discord.Embed(color=random.randint(0, 0xFFFFFF), title="**___ANNOUNCEMENT___**:")
            finale2.add_field(name=f"{ans4.content}", value=f"{ans5.content}")

            await ans1.delete()
            await ques1.delete()
            await ans4.delete()
            await ans5.delete()

            channel = self.bot.get_channel(BOTOUTPUT)
            await channel.send(embed=finale2)

        else:
            raise error









def setup(bot):
    bot.add_cog(Administration(bot))