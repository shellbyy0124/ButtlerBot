import discord
import json
import random
import datetime
import DiscordUtils
import asyncio

from os import error
from discord.ext import commands
from discord.ext.commands import cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

LT = data["guild"]["LT"]

with open('./users.json', 'r', encoding='utf-8-sig') as g:
    data = json.load(g)

kastien = data["users"]["Kastien"]
shellbyy = data["users"]["Shellbyy"]

class HelpCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.color = random.randint(0,0xFFFFFF)
        self.time = datetime.datetime.utcnow()
        self.url = self.bot.user.avatar_url

    @commands.command()
    async def bhelp(self, ctx):
        
        embed1 = discord.Embed(color=self.color, timestamp=self.time, title="Buttler Prefix", description="If you can't ever remember the prefix to use the ButtlerBot commands, simple type `buttlerprefix`", inline=False).set_image(url=self.bot).set_footer(text='Page 1/16')
        embed2 = discord.Embed(color=self.color, timestamp=self.time, title="Coin Flip", description="To play the coinflip game, type `>bflip <side> <amount>` where side is heads or tails, and amount is how much you're wanting to bet. If you haven't created a profile, use `>bcprofile` to create one, and receive a free $1000 to start your gambling habits ;)", inline=False).set_image(url=self.bot).set_footer(text='Page 2/16')
        embed3 = discord.Embed(color=self.color, timestamp=self.time, title="Team Code Submission", description="If you're applying to a team within the discord, head over to the _Teams_ category to get started.", inline=False).set_image(url=self.bot).set_footer(text='Page 3/16')
        embed4 = discord.Embed(color=self.color, timestamp=self.time, title="Discord Suggestion", description="Have a thought about the discord, and how it could be better? Then type `>bdsubmit <message>` to submit your thoughts, and suggestions", inline=False).set_image(url=self.bot).set_footer(text='Page 4/16')
        embed5 = discord.Embed(color=self.color, timestamp=self.time, title="Buttler Bot Suggestion", description="Thinking about something that could be added to, or made better, with a bot in the discord? Then use `>bbsubmit <message>` to share your thoughts with us!", inline=False).set_image(url=self.bot).set_footer(text="Page 5/16")
        embed6 = discord.Embed(color=self.color, timestamp=self.time, title="Pasting Code", description="No one likes looking at a huge wall of code that uses every available character space that you're allowed to send in one message. Instead, we have a `>bpaste` command that has links in it for you to use :)", inline=False).set_image(url=self.bot).set_footer(text='Page 6/16')
        embed7 = discord.Embed(color=self.color, timestamp=self.time, title=f"{self.bot.get(LT).name} Bot List", description=f"Curious about the bots we use here within {self.bot.get(LT).name}? Type `>bblist` to get that info!", inline=False).set_image(url=self.bot).set_footer(text='Page 7/16')
        embed8 = discord.Embed(color=self.color, timestamp=self.time, title="Inviting People To The Discord", description=":red_circle:**__DO NOT CREATE YOUR OWN INVITE LINK TO ANY PART OF THIS DISCORD__**:red_circle:\nWe have generate a link for you. Type `>binvite` to get the link", inline=False).set_image(url=self.bot).set_footer(text='Page 8/16')
        embed9 = discord.Embed(color=self.color, timestamp=self.time, title="Bad Word List", description="Too many negative, hurtful, or down-right unecessary words being used and not being caught by the filter? Use `>bbadlist <words_to_add>` to submit those to us!", inline=False).set_image(url=self.bot).set_footer(text='Page 9/16')
        embed10 = discord.Embed(color=self.color, timestamp=self.time, title="Broken Bots", description="Experiencing issues with any of our bots? Please use `>bbug` to submit a bug report.", inline=False).set_image(url=self.bot).set_footer(text='Page 10/16')
        embed11 = discord.Embed(color=self.color, timestamp=self.time, title="Negative Attitudes", description="Negative attitudes, being rude to others, etc will not be tolerated within this community. We are here to learn and grow together regardless to our experience levels! If someone is being negative, then type `>think` to see the acronym for thinking before you speak!", inline=False).set_image(url=self.bot).set_footer(text="Page 11/16")
        embed12 = discord.Embed(color=self.color, timestamp=self.time, title="Getting Support", description="In need of help of some sort? Then head over to the _Support_ category for futher help :)", inline=False).set_image(url=self.bot).set_footer(text="Page 12/16")
        embed13 = discord.Embed(color=self.color, timestamp=self.time, title="Profiles", description="Can't play a game? Can't use the `>bprofile` command? Then you probably need to create a profile! Head on over to the _Profiles_ category of the discord for futher assistance with getting started :)", inline=False).set_image(url=self.bot).set_footer(text="Page 13/16")
        embed14 = discord.Embed(color=self.color, timestamp=self.time, title="Rules", description="Everyone was sent a list of the rules when they joined the discord. If the rules are needing to be referenced again, then use `>brules` to get the rules of the discord", inline=False).set_image(url=self.bot).set_footer(text="Page 14/16")
        embed15 = discord.Embed(color=self.color, timestamp=self.time, title="Staff/Dev Team Applications", description=f"We are always accepting applications from members for our Dev Team and Staff Team within {self.bot.get(LT).name}", inline=False).set_image(url=self.bot).set_footer(text="Page 15/16")
        embed16 = discord.Embed(color=self.color, timestamp=self.time, title="Buttler's Teams", description="Thinking about becoming a Team Captain and starting a small programming team together? Then head over to the _Teams_ category to get started!")


        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        embeds = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16]
        await paginator.run(embeds)

    @commands.command()
    @commands.has_any_role('Owner', 'Head Admin', 'Admin', 'Moderator', 'Community Helper')
    async def bstaff(self, ctx):
        
        adminembed1 = discord.Embed(color=self.color, timestamp=self.time, title="Community Updates Command", description="To create an announcement for the community, `>bbotcommunity` to start the announcement editor", inline=False).set_image(url=self.bot).set_footer(text='Page 1/9')
        adminembed2 = discord.Embed(color=self.color, timestamp=self.time, title="Statistics Command", description="`>bstats` will show you various information pertinent to the discord", inline=False).set_thumbnail(url=self.bot).set_footer(text='Page 2/9')
        adminembed3 = discord.Embed(color=self.color, timestamp=self.time, title="Nickname Command", description="NickNames have to be maintained as we are a 13+ age group or higher community", inline=False).set_thumbnail(url=self.bot).set_footer(text='Page 3/9')
        adminembed4 = discord.Embed(color=self.color, timestamp=self.time, title="Who Is Command", description="`>bwhois <@member_name>` will show you a few stats on a user", inline=False).set_thumbnail(url=self.bot).set_footer(text='Page 4/9') 
        adminembed5 = discord.Embed(color=self.color, timestamp=self.time, title="Warning Command", description="`>bwarn` if someone is being rude, or isn't following the rules, then this is your first go to. This command will privately DM the member a warning, along with putting a copy fo the warning in the logs category.", inline=False).set_thumbnail(url=self.bot).set_footer(text='Page 5/9')
        adminembed6 = discord.Embed(color=self.color, timestamp=self.time, title="Tempmute Command", description="`>btempmute <user_name>` If warning a member just isn't getting the point across, then temporarily mute them. I do not want anyone banning anyone for any reason unless discussed with me, Mekasu!", inline=False).set_thumbnail(url=self.bot).set_footer(text="Page 6/9")
        adminembed7 = discord.Embed(color=self.color, timestamp=self.time, title="Promoting Command", description="`>bpromote <user_name>` Is it time to bring in a new staff member, or dev team partner? Then promote them! (with prior authorization of course lol)", inline=False).set_thumbnail(url=self.bot).set_footer(text='Page 7/9')
        adminembed8 = discord.Embed(color=self.color, timestamp=self.time, title="Teams Command", description="`>bteam` This command is available for anyone to use, but it is not on the public help list. This is for members who want to become a Team Captain. Please do not just allow users to freely use this command. If a staff member has not posted that they approved the team within the teams channel, the channel will be deleted!", inline=False).set_thumbnail(url=self.bot).set_footer(text='Page 8/9')
        adminembed9 = discord.Embed(color=self.color, timestamp=self.time, title="Latency Command", description="", inline=False).set_thumbnail(url=self.bot).set_footer(text="Page 9/9")
        
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        adminembeds = [adminembed1, adminembed2, adminembed3, adminembed4, adminembed5, adminembed6, adminembed7, adminembed8, adminembed9]
        await paginator.run(adminembeds)

    @commands.command(aliases=['dev'])
    @commands.has_any_role('Owner', 'Head Dev', 'Dev')
    async def bdev(self, ctx):
        
        embed1 = discord.Embed(color=self.color, timestamp=self.time, title="Updating The Challenges List", description="`>buplist` No Dev is to execute this command unless they have approval from the Head Developer", inline=False).set_thumbnail(url=self.bot).set_footer(text="Page 1/6")
        embed2 = discord.Embed(color=self.color, timestamp=self.time, title="Announcements For Adding Bots", description="`>baddingbots` This announcement is for when we are adding new bots that have been approved by the Head Developer to be added to the discord! This command is only to be used by Mekasu, KataReborn, or a member of the developer team that has permissions", inline=False).set_thumbnail(url=self.bot).set_footer(text="Page 2/6")
        embed3 = discord.Embed(color=self.color, timestamp=self.time, title="Purging Message", description="`>bpurge X` this command will remove X amount of messages excluding pinned messages.", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 3/6")    
        embed4 = discord.Embed(color=self.color, timestamp=self.time, title="Information Commands", description="`>blistall`, `>blistmem`, `>blistroles` are all use to obtain the list of roles, members, and the list of members in their perspective roles within the discord", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 4/6")
        embed5 = discord.Embed(color=self.color, timestamp=self.time, title="Updating Bots Announcement", description="`>bbotupdates <message>` is for the Head Dev to announce any, and all updates, made to any of the bots within the discord.", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 5/6")
        embed6 = discord.Embed(color=self.color, timestamp=self.time, title="Locking/Unlocking Channels", description="This command is for when one, or multiple, of our bots have gone haywire, or we're being hacked. Do Not make light of this command", inline=False).set_thumbnail(url=self.url).set_footer(text="Page 6/6")

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        embeds = [embed1, embed2, embed3, embed4, embed5, embed6]
        await paginator.run(embeds)

def setup(bot):
    bot.add_cog(HelpCommands(bot))