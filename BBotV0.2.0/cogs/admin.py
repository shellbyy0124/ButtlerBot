import discord
import json
import datetime
import DiscordUtils
import asyncio

from discord.ext import commands
from discord.ext.commands import Cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data=json.load(f)


    
class Administration(commands.Cog):

    def __init__(self, bot):

        self.bot = bot    
    
    
    @commands.command(aliases=["buttlerstaffhelp"])
    @commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
    async def staffhelpmenu(self, ctx):

        adminembed1 = discord.Embed(color=ctx.author.color).add_field(name=f"Hi! I'm {self.bot.user.name} Staff Menu, and I'm here to help!",
                                                                value="In the pages to follow are things that I am able to currently help you with, and below that is a list of things that I am currently developing to better help you in the future! :smile: To get my help menu, type `/buttlerstaffhelp`")
        adminembed1.set_image(url=self.bot.user.avatar_url)
        adminembed1.set_footer(text='Page 1/20')
        adminembed1.timestamp = datetime.datetime.now()
        adminembed2 = discord.Embed(color=ctx.author.color).add_field(name="Server Statistics:",
                                                                value="Want to help us keep up with the server stats? Type /buttlerstats to get the pertinent info!")
        adminembed2.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed2.set_footer(text='Page 2/20')
        adminembed2.timestamp = datetime.datetime.now()
        adminembed3 = discord.Embed(color=ctx.author.color).add_field(name=f"User Inappropriate Nickname?",
                                                                value="Do you see a user with an inappropriate username? then type /buttlerchangenick <username_as_currently_shown> <actual_name> and the user will automatically be dm'd a message of their nickname being changed. Adding a reason for why will be coming in a future update!")
        adminembed3.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed3.set_footer(text='Page 3/20')
        adminembed3.timestamp = datetime.datetime.now()
        adminembed4 = discord.Embed(color=ctx.author.color).add_field(name=f"Purging Channels: `>buttlerpurge`",
                                                                value="Do Not Abuse This Ability! If you are deleting less than 20-ish messages, then right click and delete them individually. This command is only for if someone has hacked us, or spammed us! It will delete pinned messages if you delete it with the bot! Try not to use this command if you are not an admin or higher. If unsure of when to use it, please ask an admin or higher in the staff chat channel")
        adminembed4.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed4.set_footer(text='Page 4/20')
        adminembed4.timestamp = datetime.datetime.now()
        adminembed5 = discord.Embed(color=ctx.author.color).add_field(name=f"Who Is Who but a Who!",
                                                                value="Some have an incomprehensible nickname, and you want to know who they are, or need to change their nickname, then type /buttlerwhois <username> and get that information!")
        adminembed5.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed5.set_footer(text='Page 5/20')
        adminembed5.timestamp = datetime.datetime.now()
        adminembed6 = discord.Embed(color=ctx.author.color).add_field(name=f"A member being obnixious is the voice, or text channel?",
                                                                value="Type `/tempmute <member_name> <time_in_seconds> <reason>` to mute them").add_field(name="\u200b", value="**THIS COMMAND IS UNDER CONSTRUCTION AND WILL NOT WORK**")
        adminembed6.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed6.set_footer(text='Page 6/20')
        adminembed6.timestamp = datetime.datetime.now()
        adminembed7 = discord.Embed(color=ctx.author.color).add_field(name=f"Locking Channels:", value="It is only ok to lock a channel with `>buttlerlock` when we are being spammed, or a virus of some sort is in the server. Other than that, you can simply use the `>buttlerwarn` or `>butlertempmute` commands to take care of the problem.")
        adminembed7.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed7.set_footer(text='Page 7/20')
        adminembed7.timestamp = datetime.datetime.now()
        adminembed8 = discord.Embed(color=ctx.author.color).add_field(name="Unlocking Channels:", value="As stated previously with the locking channels, and the appropriatness of that command, unlocking channels (`>buttlerunlock`) are only to be done by the head admins or higher. We are the only ones with access to the files. We will let you know when it is safe!")
        adminembed8.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed8.set_footer(text="Page 8/20")
        adminembed8.timestamp = datetime.datetime.now()
        adminembed9 = discord.Embed(color=ctx.author.color).add_field(name="Need To Know Who's Here?", value="Use `>buttlerlistmembers` to get a list of members within the discord :smile:")
        adminembed9.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed9.set_footer(text="Page 9/20")
        adminembed9.timestamp = datetime.datetime.now()
        adminembed10 = discord.Embed(color=ctx.author.color).add_field(name="Need to make an announcement?", value="Use `>bannounce` and follow the prompts on the screens to follow to get your announcement amde :D")
        adminembed10.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed10.set_footer(text="Page 10/20")
        adminembed10.timestamp = datetime.datetime.utcnow()
        adminembed11 = discord.Embed(color=ctx.author.color).add_field(name="Making An Announcement?", value="Use `>bannouce` to make your announcement. When making your announcement, be sure to read the screen carefully!!! **DO NOT USE OPTION C IF YOU ARE NOT THE HEAD DEV OR THE OWNER!!!!**")
        adminembed11.set_thumbnail(url=self.bot.user.avatar_url)
        adminembed11.set_footer(text="11/21")
        adminembed11.timestamp = datetime.datetime.utcnow()
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction('⏮️', "first")
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('⏭️', "last")
        adminembeds = [adminembed1, adminembed2, adminembed3, adminembed4, adminembed5, adminembed6, adminembed7, adminembed8, adminembed9, adminembed10]
        await paginator.run(adminembeds)
        await asyncio.sleep(90)
        await adminembeds.delete()


