import discord
import json
import asyncio
import datetime
import random
import DiscordUtils

from discord.ext import commands
from discord.ext.commands import cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

warnings = data["channels"]["warnings"]
bot_updates = data["channels"]["bot_updates"]
community_updates = data["channels"]["community_updates"]
staff_commands = data["channels"]["staff_commands"]
tempmutes = data["channels"]["tempmutes"]
appeals = data["channels"]["appeals"]
muted = data["roles"]["muted"]

class Administration(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.time = datetime.datetime.utcnow()
        self.url = self.bot.user.avatar_url

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admins', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def bstats(self, ctx):

        await ctx.message.delete()

        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
        staff_roles = ["Owner", "Head Dev", "Dev", "Head Admin", "Admins", "Moderators", "Community Helpers", "Members"]
            
        embed2 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=ctx.message.created_at)
        embed2.add_field(name='Name', value=f"{ctx.guild.name}", inline=False)
        embed2.add_field(name='Owner', value=f"Mekasu, Kastien", inline=False)
        embed2.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
        embed2.add_field(name='Highest role', value=ctx.guild.roles[-1], inline=False)
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


    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Head Admin', 'Admins', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def bcnick(self, ctx, member:discord.Member, nick, reason):
        await ctx.message.delete()
        existing_nick = member.display_name
        new_nick = await member.edit(nick=nick)
        nickembed = discord.Embed(color=random.randint(0, 0xFFFFFF), title="**Inappropriate Nick Name!").add_field(name="\u200b", value=f"{member.name}, you have chosen an inappropriate nickname. The offending name is: '{existing_nick}, and it has been changed to; {new_nick}, because {reason}")
        await member.send(embed=nickembed)


    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev')
    async def bpurge(self, ctx, amount:int):

        await ctx.channel.purge(limit=amount, check=lambda m: not m.pinned)
        await ctx.send(f"I have purged {amount} messages")

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Head Admin', 'Admins', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def warn(self, ctx, member:discord.Member):

        def check(m):
            return m.author.id == ctx.author.id

        await ctx.message.delete()
        a = await ctx.send("Please enter the reason for the warning")
        reason = await self.bot.wait_for('message', check=check)

        if all(i.isprintable() for i in reason.content):

            warn = discord.Embed(color= discord.Colour.red(), timestamp=datetime.datetime.utcnow(), title=f":red_circle:**__WARNING__**:red_circle:", description=f"Staff Member: {ctx.author.display_name}\nStaff member Role: {ctx.author.top_role}\nMember: {member.display_name}\nReason: {reason.content}").set_thumbnail(url=ctx.author.avatar_url)

            await member.send(embed=warn)
            channel = self.bot.get_channel(warnings)
            await channel.send(embed=warn)

            await a.delete()
            await reason.delete()

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Head Administrator', 'Admins', 'Moderators', 'Team Captain', 'Community Helpers')
    async def tempmute(self, ctx, member:discord.Member, reason, timer:int):

        await ctx.message.delete()

        def check(m):
            return ctx.message.author == m.author

        channel1 = self.bot.get_channel(staff_commands)

        if ctx.message.channel == channel1:

            embed1 = discord.Embed(color=discord.Colour.red(), timestamp=self.time, title="**__A Tempmute Has Been Issued!__**", description=f"Offending Members Name: {member.top_role.name} {member.name}\nStaff Member Responsible: {ctx.author.top_role.name} {ctx.author.display_name}\nReason: {reason}\nTime Length: {timer}s", inline=False).set_thumbnail(url=self.url)
            await member.send(embed=embed1)
            channel = self.bot.get_channel(tempmutes)
            msg1 = await channel.send(embed=embed1)
            await msg1.pin()
            await channel.purge(limit=1)

            existing_role = member.top_role
            await member.remove_roles(existing_role)

            role = discord.utils.get(ctx.guild.roles, name="muted")
            await member.add_roles(role)

            await asyncio.sleep(timer)

            await member.remove_roles(role)
            await member.add_roles(existing_role)

            embed2 = discord.Embed(color=discord.Colour.green(), timestamp=self.time, title="**__YOU HAVE BEEN UNMUTED!__**", description=f"Yeet, {member.mention}! You have served your sentence! Your access has been regained within the discord :)", inline=False).set_thumbnail(url=self.url)
            await member.send(embed=embed2)
            await channel.send(embed=embed2)

        else:
            a = await ctx.send("**__You must be in the #staff_commands channel to use this command")
            await asyncio.sleep(10)
            await a.delete()
    
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
    @commands.has_any_role("Owner", "Head Dev", "Head Admin")
    async def promote(self, ctx, member:discord.Member):

        current_role = member.top_role
        hr_position = member.top_role.position

        i = 1

        while True:

            role = ctx.guild.roles[member.top_role.position - len(ctx.guild.roles)]

            if role.id == ctx.guild.id:

                await ctx.send("you are the highest :mhm:")
                break

            if role.managed:
                i += 1
                continue

            await member.add_roles(role)
            await member.remove_roles(current_role)
            break
        
        promotion = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title=":rotating_light:**___INCOMING PROMOTION___**:rotating_light:", description=f"Please give some <3 for {member.mention} for their promotion from {current_role} to {role}!:clap::clap::clap::clap::clap::clap::clap:", inline=False).set_thumbnail(url=member.avatar_url)
        channel = self.bot.get_channel(community_updates)
        await channel.send(embed=promotion)
        
        adminembed = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Commands Now Available To You!", description="You can access this help menu any time within the dicsord using `>bstaff`", inline=False)
        adminembed.add_field(name="Community Updates Command", value="To create an announcement for the community, `>bbotcommunity` to start the announcement editor", inline=False)
        adminembed.add_field(name="Statistics Command", value="`>bstats` will show you various information pertinent to the discord", inline=False)
        adminembed.add_field(name="Nickname Command", value="NickNames have to be maintained as we are a 13+ age group or higher community", inline=False)
        adminembed.add_field(name="Who Is Command", value="`>bwhois <@member_name>` will show you a few stats on a user", inline=False)
        adminembed.set_thumbnail(url=self.url)

        adminembed2 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Continued")
        adminembed2.add_field(name="Warning Command", value="`>bwarn` if someone is being rude, or isn't following the rules, then this is your first go to. This command will privately DM the member a warning, along with putting a copy fo the warning in the logs category.", inline=False)
        adminembed2.add_field(name="Tempmute Command", value="`>btempmute <user_name>` If warning a member just isn't getting the point across, then temporarily mute them. I do not want anyone banning anyone for any reason unless discussed with me, Mekasu!", inline=False)
        adminembed2.add_field(name="Promoting Command", value="`>bpromote <user_name>` Is it time to bring in a new staff member, or dev team partner? Then promote them! (with prior authorization of course lol)", inline=False)
        adminembed2.add_field(name="Teams Command", value="`>bteam` This command is available for anyone to use, but it is not on the public help list. This is for members who want to become a Team Captain. Please do not just allow users to freely use this command. If a staff member has not posted that they approved the team within the teams channel, the channel will be deleted!", inline=False)
        adminembed2.add_field(name="Latency Command", value=">bping", inline=False)
        adminembed2.set_thumbnail(url=self.url)

        await member.send(embed=adminembed)        
        await member.send(embed=adminembed2)

def setup(bot):
    bot.add_cog(Administration(bot))