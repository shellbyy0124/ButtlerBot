import discord
import DiscordUtils as DU

from discord.ext import commands
from discord.ext.commands import Cog 

class Information(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev')
    async def binfo(self, ctx):

        note1 = "This message will self-destruct after 300 seconds"
        
        buttler = discord.Embed(color=self.color, timestamp=self.time, title="Hi! Welcome To The ButtlerBot Introduction!", description="Table Of Contents:\n1) Introduction\n2) What I Can Do\n3) General Commands\n 4) Staff Commands\n5) Dev Commands", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)

        buttler1 = discord.Embed(color=self.color, timestamp=self.time, title="Introduction", description="ButtlerBot was created just before Christmas of 2020.", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)

        buttler2 = discord.Embed(color=self.color, timestamp=self.time, title="What I Can Do", description="As of now, ButtlerBot can run several moderation commands, as well as, he can send a list of your discords rules to new members who join, play mini-games, send automated messages, and so much more!", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)

        buttler3 = discord.Embed(color=self.color, timestamp=self.time, title="General Commands", description="bprefix - bflip - btsubmit - bdsubmit - bbsubmit - bpaste\nbblist - binvite - bbadlist - bbug - think - bsupport\nbhelp - bcprofile - brules - bsapp", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)

        buttler4 = discord.Embed(color=self.color, timestamp=self.time, title="Staff Commands", description="bbotcommynity - bstats - bcnick - bwhois - bwarn - btempmute\nbpromotion - bteam - bping", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)

        buttler5 = discord.Embed(color=self.color, timestamp=self.time, title="Dev Commands", description="buplist - addingbots - bpurge - blistall - blistmem\nblistroles - bbotupdates - block - bunlock", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)

        buttler6 = discord.Embed(color=self.color, timestamp=self.time, title="", description="", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)

        buttler7 = discord.Embed(color=self.color, timestamp=self.time, title="The Creators", description="", inline=False).set_thumbnail(url=self.bot).set_footer(text=note1)

        paginator = DU.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        embeds21 = [buttler, buttler1, buttler2, buttler3, buttler4, buttler5, buttler6, buttler7]
        await paginator.run(embeds21)

def setup(bot):
    bot.add_cog(Information(bot))