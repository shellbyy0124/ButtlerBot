import discord
import json
import random
import datetime

from os import error
from discord.ext import commands
from discord.ext.commands import cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

LT = data["guild"]["LT"]

with open('./users.json', 'r', encoding='utf-8-sig') as g:
    data = json.load(g)

shellbyy = data["users"]["Shellbyy"]

class HelpCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.time = datetime.datetime.utcnow()
        self.url = self.bot.user.avatar_url

    @commands.command()
    async def bhelp(self, ctx):
        
        embed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Buttler Prefix", description="If you can't ever remember the prefix to use the ButtlerBot commands, simple type `buttlerprefix`", inline=False).set_image(url=self.url)
        embed1.add_field(name="Coin Flip", value="To play the coinflip game, type `>bflip <side> <amount>` where side is heads or tails, and amount is how much you're wanting to bet. If you haven't created a profile, use `>bcprofile` to create one, and receive a free $1000 to start your gambling habits ;)", inline=False)
        embed1.add_field(name="Team Code Submission", value="If you're applying to a team within the discord, head over to the _Teams_ category to get started.", inline=False)
        embed1.add_field(name="Discord Suggestion", value="Have a thought about the discord, and how it could be better? Then type `>bdsubmit <message>` to submit your thoughts, and suggestions", inline=False)
        embed1.add_field(name="Buttler Bot Suggestion", value="Thinking about something that could be added to, or made better, with a bot in the discord? Then use `>bbsubmit <message>` to share your thoughts with us!", inline=False)
        embed1.add_field(name="Pasting Code", value="No one likes looking at a huge wall of code that uses every available character space that you're allowed to send in one message. Instead, we have a `>bpaste` command that has links in it for you to use :)", inline=False)
        embed1.add_field(name=f"{ctx.guild.name} Bot List", value=f"Curious about the bots we use here within {ctx.guild.name}? Type `>bblist` to get that info!", inline=False)
        embed1.add_field(name="Inviting People To The Discord", value=":red_circle:**__DO NOT CREATE YOUR OWN INVITE LINK TO ANY PART OF THIS DISCORD__**:red_circle:\nWe have generate a link for you. Type `>binvite` to get the link", inline=False)
        embed1.add_field(name="Bad Word List", value="Too many negative, hurtful, or down-right unecessary words being used and not being caught by the filter? Use `>bbadlist <words_to_add>` to submit those to us!", inline=False)
        embed1.add_field(name="Broken Bots", value="Experiencing issues with any of our bots? Please use `>bbug` to submit a bug report.", inline=False)
        embed1.add_field(name="Negative Attitudes", value="Negative attitudes, being rude to others, etc will not be tolerated within this community. We are here to learn and grow together regardless to our experience levels! If someone is being negative, then type `>think` to see the acronym for thinking before you speak!", inline=False)
        embed1.add_field(name="Getting Support", value="In need of help of some sort? Then head over to the _Support_ category for futher help :)", inline=False)
        embed1.add_field(name="Profiles", value="Can't play a game? Can't use the `>bprofile` command? Then you probably need to create a profile! Head on over to the _Profiles_ category of the discord for futher assistance with getting started :)", inline=False)
        embed1.add_field(name="Rules", value="Everyone was sent a list of the rules when they joined the discord. If the rules are needing to be referenced again, then use `>rules` to get the rules of the discord", inline=False)
        embed1.add_field(name="Staff/Dev Team Applications", value=f"We are always accepting applications from members for our Dev Team and Staff Team within {ctx.guild.name}", inline=False)
        embed1.add_field(name="Buttler's Teams", value="Thinking about becoming a Team Captain and starting a small programming team together? Then head over to the _Teams_ category to get started!")

        await ctx.send(embed=embed1)

    @commands.command()
    @commands.has_any_role('Owner', 'Head Admin', 'Admin', 'Moderator', 'Community Helper')
    async def bstaff(self, ctx):
        
        adminembed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Community Updates Command", description="To create an announcement for the community, `>bbotcommunity` to start the announcement editor", inline=False).set_image(url=self.url)
        adminembed1.add_field(name="Statistics Command", value="`>bstats` will show you various information pertinent to the discord", inline=False)
        adminembed1.add_field(name="Nickname Command", value="NickNames have to be maintained as we are a 13+ age group or higher community", inline=False)
        adminembed1.add_field(name="Who Is Command", value="`>bwhois <@member_name>` will show you a few stats on a user", inline=False) 
        adminembed1.add_field(name="Warning Command", value="`>bwarn` if someone is being rude, or isn't following the rules, then this is your first go to. This command will privately DM the member a warning, along with putting a copy fo the warning in the logs category.", inline=False)
        adminembed1.add_field(name="Tempmute Command", value="`>btempmute <user_name>` If warning a member just isn't getting the point across, then temporarily mute them. I do not want anyone banning anyone for any reason unless discussed with me, Mekasu!", inline=False)
        adminembed1.add_field(name="Promoting Command", value="`>bpromote <user_name>` Is it time to bring in a new staff member, or dev team partner? Then promote them! (with prior authorization of course lol)", inline=False)
        adminembed1.add_field(name="Teams Command", value="`>bteam` This command is available for anyone to use, but it is not on the public help list. This is for members who want to become a Team Captain. Please do not just allow users to freely use this command. If a staff member has not posted that they approved the team within the teams channel, the channel will be deleted!", inline=False)
        adminembed1.add_field(name="Latency Command", value="If the bot is lagging, then use `>bping` to see it's ping.", inline=False)
        
        await ctx.send(embed=adminembed1)

    @commands.command(aliases=['dev'])
    @commands.has_any_role('Owner', 'Head Dev', 'Dev')
    async def bdev(self, ctx):
        
        embed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title="Updating The Challenges List", description="`>buplist` No Dev is to execute this command unless they have approval from the Head Developer", inline=False).set_thumbnail(url=self.url)
        embed1.add_field(name="Announcements For Adding Bots", value="`>baddingbots` This announcement is for when we are adding new bots that have been approved by the Head Developer to be added to the discord! This command is only to be used by Mekasu, KataReborn, or a member of the developer team that has permissions", inline=False)
        embed1.add_field(name="Purging Message", value="`>bpurge X` this command will remove X amount of messages excluding pinned messages.", inline=False)
        embed1.add_field(name="Information Commands", value="`>blistall`, `>blistmem`, `>blistroles` are all use to obtain the list of roles, members, and the list of members in their perspective roles within the discord", inline=False)
        embed1.add_field(name="Updating Bots Announcement", value="`>bbotupdates <message>` is for the Head Dev to announce any, and all updates, made to any of the bots within the discord.", inline=False)
        embed1.add_field(name="Locking/Unlocking Channels", value="This command is for when one, or multiple, of our bots have gone haywire, or we're being hacked. Do Not make light of this command", inline=False)

        await ctx.send(embed=embed1)

def setup(bot):
    bot.add_cog(HelpCommands(bot))