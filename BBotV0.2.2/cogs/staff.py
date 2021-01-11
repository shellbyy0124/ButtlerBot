import warnings
import DiscordUtils as DiscordUtils
import discord
import json
import asyncio
import os
import datetime
import random
import sqlite3

from os import error
from discord import member
from discord.ext import commands
from discord.ext.commands import cog
from discord.utils import get
from isort import logo

# switch me to database
with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
warnings = data["channels"]["warnings"]
bot_updates = data["channels"]["bot_updates"]
community_updates = data["channels"]["community_updates"]
staff_commands = data["channels"]["staff_commands"]
tempmutes = data["channels"]["tempmutes"]
appeals = data["channels"]["appeals"]

class Administration(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["bstats"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admins', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def serverinfo(self, ctx):

        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
        staff_roles = ["Owner", "Head Dev", "Dev", "Head Admin", "Admins", "Moderators", "Community Helpers", "Members"]
            
        embed2 = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
        embed2.add_field(name='Name', value=f"{ctx.guild.name}", inline=False)
        embed2.add_field(name='Owner', value=f"Mekasu, Kastien", inline=False)
        embed2.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
        embed2.add_field(name='Highest role', value=ctx.guild.roles[-2], inline=False)
        embed2.add_field(name='Contributers:', value="None")

        for r in staff_roles:
            role = discord.utils.get(ctx.guild.roles, name=r)
            if role:
                members = '\n'.join([member.name for member in role.members]) or "None"
                embed2.add_field(name=role.name, value=members)

        embed2.add_field(name='Number of roles', value=str(role_count), inline=False)
        embed2.add_field(name='Number Of Members', value=ctx.guild.member_count, inline=False)
        embed2.add_field(name='Bots:', value=(', '.join(list_of_bots)))
        embed2.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed2.set_thumbnail(url=ctx.guild.icon_url)
        embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed2.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        channel = self.bot.get_channel(staff_commands)
        await channel.send(embed=embed2)


    @commands.command(aliases=["bcnick"])
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Head Admin', 'Admins', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def changemembernickname(self, ctx, member:discord.Member, nick, reason):
        existing_nick = member.display_name
        new_nick = await member.edit(nick=nick)
        nickembed = discord.Embed(color=ctx.author.color, title="**Inappropriate Nick Name!").add_field(name="\u200b", value=f"{member.name}, you have chosen an inappropriate nickname. The offending name is: '{existing_nick}, and it has been changed to; {new_nick}, because {reason}")
        await member.send(embed=nickembed)


    @commands.command(aliases=["bpurge"])
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Head Admin', 'Admins')
    async def clear(self, ctx, amount:int):
        await ctx.channel.purge(limit=amount, check=lambda m: not m.pinned)


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
        embed1.add_field(name='Highest Role', value=user.top_role.name, inline=True)
        embed1.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        embed1.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        embed1.set_thumbnail(url=user.avatar_url)
        embed1.set_author(name=user.name, icon_url=user.avatar_url)
        embed1.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        channel = self.bot.get_channel(staff_commands)
        await channel.send(embed=embed1)


    @commands.command(aliases=["block"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admins', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def lock(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel
        role = discord.utils.get(ctx.guild.roles, name='Members')
        role1 = discord.utils.get(ctx.guild.roles, name='Community Helpers')
        role2 = discord.utils.get(ctx.guild.roles, name='Moderators')
        roles = [role, role1, role2]

        for role in roles:
            overwrite = channel.overwrites_for(role)
            overwrite.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(f'{self.bot.user.name} has locked this channel.')


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

        warn = discord.Embed(color= discord.Colour.orange(), timestamp=datetime.datetime.utcnow(), title=f":red_circle:**__WARNING__**:red_circle:", description=f"Staff Member: {ctx.author.display_name}\nStaff member Role: {ctx.author.top_role}\nMember: {member.display_name}\nReason: {reason}")

        await member.send(embed=warn)
        channel = self.bot.get_channel(warnings)
        await channel.send(embed=warn)

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def btempmute(self, ctx):

        def check(m):
            return m.author == ctx.author

        await ctx.message.delete()
        color = random.randint(0, 0xFFFFFF)
        time = datetime.datetime.utcnow()
        number = random.randint(100000, 199999)
        channel2020 = staff_commands
        
        embed1 = discord.Embed(color=color, timestamp=time, title="ButtlerBot Warning Editor:", description="Please Enter The Name Of The User Being Temaporarily Banned:")
        
        if ctx.channel.id == channel2020:

            msg1 = await ctx.send(embed=embed1)
            ans1 = await self.bot.wait_for('message', check=check)
            
            for user in ctx.guild.members:
                
                if not user.bot:

                    if ans1.content == user:

                        await ans1.delete()
                        member = ans1.content

                        embed2 = discord.Embed(color=color, timestamp=time, title=f"ButtlerBot Warning Editor:", description=f"Staff Member: {ctx.author.display_name}\nStaff Member Role: {ctx.author.top_role}\nMember: {ans1.content}\n\nEnter The Length Of Time:")
                        await msg1.edit(embed=embed2)
                        ans2 = await self.bot.wait_for('message', check=check)

                        if all(i.isint() for i in ans2.content):

                            await ans2.delete()

                            time = int(ans2.content)

                            embed3 = discord.Embed(color=color, timestamp=time, title="ButtlerBot Warning Editor:", description=f"Staff Member: {ctx.author.display_name}\nStaff Member Role: {ctx.author.top_role}\nMember: {ans1.content}\nLength Of Time:\n{ans2.content}s\n\nPlease Enter The Reason For The Temporary Mute:")
                            await msg1.edit(embed=embed3)
                            ans3 = await self.bot.wait_for('message', check=check)

                            if all(i.isprintable() for i in ans3.content):

                                await ans3.delete()

                                embed4 = discord.Embed(color=color, timestamp=time, title="Buttler Warning Editor:", description=f"Staff Member: {ctx.author.display_name}\nStaff Member Role: {ctx.author.top_role}\nMember: {ans2.content}\nLength Of Time:\n{ans2.content}s\nReason: {ans3.content}")
                                await msg1.delete()
                                channel = self.bot.get_channel(tempmutes)
                                a = await channel.send(embed=embed4)
                                await member.send(embed=embed4)
                                await a.pin()
                                await channel.purge(limit=1)

                                current_role = member.roles
                                new_role = discord.utils.get(ctx.guild.roles, name="muted")

                                await member.remove_roles(current_role)
                                await member.add_roles(new_role)
                                await asyncio.sleep(time)
                                await member.remove_roles(new_role)
                                await member.add_roles(current_role)

                                with open('./tempmutelogs.json', 'r', encoding='utf-8-sig') as file1:
                                    data = json.load(file1)

                                current_data = data
                                new_data = {"user" : ctx.author.id, "number" : number}

                                with open('./tempmutelogs.json', 'w', encoding='utf-8-sig') as file2:
                                    data = json.dump(current_data, new_data, indent=4)

                                if time > 1800:

                                    appealembed1 = discord.Embed(color=color, timestamp=time, title="Your tempmute time is greater than 30 minutes. If you would like to submit an appeal, please type `appeal`.")
                                    await member.send(embed=appealembed1)
                                    appeal1 = await self.bot.wait_for('message', check=check)

                                    if appeal1.content.lower() == "appeal":

                                        appealembed2 = discord.Embed(color=color, timestamp=time, title=f"Appeal {number}", description=f"Name: {member.display_name}\nAppeal Number: {number}\n\nPlease enter why you are appealing your temporary mute. Please use atleast 3-5 supporting facts as to why your tempmute should be lifted.")
                                        await appeal1.edit(embed=appealembed2)
                                        appeal2 = await self.bot.wait_for('message')

                                        if all(x.isalpha() or x.isspace() for x in appeal2.content):

                                            appealembed3 = discord.Embed(color=color, timestamp=time, title=f"Appeal {number}", description=f"Name: {member.display_name}\nAppeal Number: {number}\nReason: {appeal2}")
                                            
                                            channel1 = self.bot.get_channel(appeals)
                                            b = await channel1.send(embed=appealembed3)
                                            await member.send(embed=embed4)
                                            await b.pin()
                                    else:
                                        await ctx.send("error line 236")
                                else:
                                    await ctx.send("error line 238")
                            else:
                                await ctx.send("error line 240")
                        else:
                            await ctx.send("error line 242")
                    else:
                        await ctx.send("error line 244")
                else:
                    await ctx.send("error line 246")
        else:
            msg = await ctx.send(":red_circle:**__YOU ARE NOT IN THE APPROPRIATE CHANNEL. PLEASE GO TO #staff_commands TO USE THIS COMMAND!")
            await asyncio.sleep(10)
            await msg.delete()
    
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


    @commands.command()
    @commands.has_any_role("Owner", "Head Dev", "Dev", "Head Admin")
    async def bpromotion(self, ctx, member:discord.Member):

        color = random.randint(0, 0xFFFFFF)
        timestamp = datetime.datetime.utcnow()
        image = member.avatar_url
        image2 = self.bot.user.avatar_url
        roles = ["Community Helpers", "Moderators", "Admins", "Head Admin", "Dev"]
        old_role = member.roles
        new_role = roles[roles.index(old_role)+1]
        await member.remove_roles(old_role)
        await member.add_roles(new_role)

        final_embed = discord.Embed(color=color, timestamp=timestamp, icon_url=image, title="**__INCOMING PROMOTION!__**", description=f"{member.mention} has been promoted to {new_role.name}! We are very excited to welcome you to the staff team! <3")
        channel1 = self.bot.get_channel(community_updates)
        msg1 = await channel1.send(embed=final_embed)
        await msg1.pin()

        with open('./commands.json', 'r') as x:
            data = json.load(x)
            
        stuff = data["commands"][str(member.top_role)]

        embed1 = discord.Embed(color=color, timestamp=timestamp, icon_url=image2, title="Commands Available To You:", description=f"{stuff}")
        await member.send(embed=embed1)

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Head Admin', 'Admins', 'Moderators')
    async def close(self, ctx, channel):
            
        await ctx.send("This channel will be closing in 30 seconds.")
        await asyncio.sleep(30)
        await ctx.message.channel.delete()

def setup(bot):
    bot.add_cog(Administration(bot))