#*THESE COMMANDS ARE FOR FUTURE UPDATES. THERE ARE NO COGS, AND THUS IGNORE THIS COG FOLDER WHEN BRINGING BOT ONLINE.
#*DO NOT DELETE THIS FILE! ADD THIS FILE TO THE .GITIGNORE FILE FOR THE REPO

#* fix me - documented on paper

@bot.event
async def on_message(ctx, *, message):
    if message.author.bot:
        return
    else:
        allowed_links = ['https://paste.pythondiscord.com/', 'https://pastebin.com/', 'https://rickandmortyapi.com/api/character', 'https://discord.gg/QyMuAaD9gs']
        blocked_links = ['https://www.pornhub.com']
        
        for awl in allowed_links:
             if awl in message.content:
                 return
        for bwl in blocked_links:
             if bwl in message.content:
                 await ctx.send(f'{message.author}, you cannot use that link in {ctx.guild.name}! You are only allowed to use https://paste.pythondiscord.com/, and https://pastebin.com/ to post your code!')
                 await message.delete()
    await bot.process_commands(message)



#* fix me - documented on paper


@commands.command()
@commands.has_permissions(mute_member=True)
async def warn(self, ctx, bot, member:discord.Member, *, reason):

    warn = discord.Embed(title=f'{ctx.author} has sent you a warning!', value=f'{reason}', inline=False)
    warn1 = discord.Embed(title=f'{ctx.author} has sent a warning to {member} for {reason}', inline=False)

    await member.send(embed=warn)
    channel = bot.get_channel(BotOutput)
    await channel.send(embed=warn1)


#* fix me - documented on paper

@commands.command()
@commands.has_any_role('Owner', 'Head Dev')
async def listroles(self, ctx, bot):
    roles = []
    for r in ctx.guild.roles:
        roles.append(r)
    channel = bot.get_channel(BotOutput)
    await channel.send(", ".join([roles.name for roles in ctx.guild.roles]))


#* fix me - documented on paper

@commands.command()
@commands.is_owner()
async def hello(self, ctx):
    hellos = discord.Embed(title="Coding Challenges Bot", description="Date Created: 11/13/2020", color=0x323e54)
    hellos.add_field(name="Release Date: ", value="To Be Determined!", inline=False)
    hellos.add_field(name="Team:", value="Mekasu, Kastien", inline=False)
    hellos.add_field(name="Help Menu", value="Type `!buttlerhelp` to get the General Commands Help Menu",
                        inline=False)
    hellos.add_field(name="Community Helper Help Menu",
                        value="Type `!buttlerchhelp` to get the Community Helpers Help Menu", inline=False)
    hellos.add_field(name="Moderator Help Menu", value="Type `!buttlerModHelp` to get the Moderator Help Menu",
                        inline=False)
    hellos.add_field(name="Admins Help Menu", value="Type `!buttlerAdminHelp` to get the Admins Help Menu",
                        inline=False)
    hellos.add_field(name="Head Admin Help Menu",
                        value="Type `!buttlerhelpheadadmin` to get the Head Admin Help Menu", inline=False)
    hellos.add_field(name="Dev Help Menu", value="Type `!buttlerhelpdev` to get the Dev Help Menu", inline=False)
    hellos.add_field(name="Head Dev Help Menu", value="Type `!buttlerhelpheaddev` to get the Head Dev Help Menu",
                        inline=False)
    hellos.add_field(name="Butler Bot",
                        value="Hi and Welcome to this brief explanation of what Butler can do :D Butler is an all-around general use bot from making/removing channels in discord, to verifying that users have agreed to your ToS. The commands are set up to only allow users to use certain commands that meet certain role requirements. Any futher questions, or concerns, when it comes to Butler, please DM shellbyy#8025 on discord",
                        inline=False)
    await ctx.send(embed=hellos)
    



#* fix me - documented on paper

@commands.command()
@commands.has_permissions(ban_member=True)
async def listall(self, ctx, bot):
    for role in ctx.guild.roles[3:]:
        if not role.managed:

            list3 = discord.Ember(title="Here is a list of all Roles, and Members within each role.")
            list3 = discord.Embed(name=f"{role.name}", description=f"""{(",".join([m.display_name for m in role.members if not m.bot]))}""")

            channel = bot.get_channel(STDOUT)
            await channel.send(embed=list3)





#* fix me - documented on paper

@tasks.loop(seconds=10)
async def changepresence():
    """Will loop every 60 seconds and change the bots presence"""
    await bot.change_presence(activity=discord.Game(name='if you can't remember, type /help!'))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Game(name=f'Member count: {total_members_count}'))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Game(name='Released: 12/02/2020 By: Shellbyy'))
    await asyncio.sleep(10)
    await bot.change_precense(activity=discord.Game(name='Team Members: Kastien-Dev, KortaPo'))
    await asyncio.sleep(10)

#* fix me - documented on paper
@bot.event
async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```You Do Not Have All The Requirements For That Command!```")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("```You Do Not Have All The Required Permissions For That Command!```")
        else:
            raise error


#* fix me - documented on paper

@bot.event
async def on_member_join(member:discord.Member):
    now = datetime.datetime.now()+datetime.timedelta(minutes=5)
    embed1 = discord.Embed(timestamp=now, color=discord.Colour.orange(), title="These Are The Rules For The Learning Together Community Discord!").add_field(name="\u200b",
                                                                         value="These rules are to be followed at all times!", inline=False)
    embed1.set_image(url=bot.user.avatar_url)
    embed1.set_footer(text="Page 1/12")
    embed2 = discord.Embed(timestamp=now, color=discord.Colour.orange(), title="Below You Will See The Tiers Of Warnings").add_field(name="\u200b", 
                                                          value="""1-3 Warnings: temp mute from text/voice chat channels < 10 minutes
                                                                     4th Warning: 12 hour silence from text/voice chat channels
                                                                     5th Warning: 1-3 Day Tempban or Perma Ban""", inline=False)
    embed2.set_image(url=bot.user.avatar_url)
    embed2.set_footer(text="Pase 2/12")
    embed3 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 1:", value="Respect of your peers is a must at all times!", inline=False)
    embed3.set_image(url=bot.user.avatar_url)
    embed3.set_footer(text="Pase 3/12")
    embed4 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 2:", value="Making someone feel inferior to your is prohibited!", inline=False)
    embed4.set_image(url=bot.user.avatar_url)
    embed4.set_footer(text="Page 4/12")
    embed5 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 3:", value="Telling someone that their question is stupid is prohibited. If you feel the person is not wanting to learn on purpose get with a staff member", inline=False)
    embed5.set_image(url=bot.user.avatar_url)
    embed5.set_footer(text="Page 5/12")
    embed6 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 4:", value="Being rude or indencent because you assume that everyone should have a pre-exisiting level of knowledge of python before requesting help is prohibited! We learn together!", inline=False)
    embed6.set_image(url=bot.user.avatar_url)
    embed6.set_footer(text="Page 6/12")
    embed7 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 5:", value="No Spamming! This includes but is not limited to: Over posting asking the same question over and over without showing progress or understanding using the @ ability when there are sufficient support channels for your needs", inline=False)
    embed7.set_image(url=bot.user.avatar_url)
    embed7.set_footer(text="page 7/12")
    embed8 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 6:", value="We have members of all ages that are welcome into this discord. No Cursing: NSFW: etc! It is prohibited!", inline=False)
    embed8.set_image(url=bot.user.avatar_url)
    embed8.set_footer(text="Page 8/12")
    embed9 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 7:", value="Keep the chats in accordance with the channels topic. If you're not sure read the top of the channel window or ask", inline=False)
    embed9.set_image(url=bot.user.avatar_url)
    embed9.set_footer(text="Page 9/12")
    embed10 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 8:", value="No Intimidation! We grow and learn together from day one and on!", inline=False)
    embed10.set_image(url=bot.user.avatar_url)
    embed10.set_footer(text="Page 10/12")
    embed11 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="Number 9:", value="Use the proper markups when submitting code. Discord supports many languages!", inline=False)
    embed11.set_image(url=bot.user.avatar_url)
    embed11.set_footer(text="Page 11/12")
    embed12 = discord.Embed(timestamp=now, color=discord.Colour.orange()).add_field(name="**Disclaimer**:", value="These rules are subject to change at any time and will be posted to the announcements channel. This pyramid is at the staff discression as to the punishment they seem fit. You always have the right to appeal!", inline=False)
    embed12.set_image(url=bot.user.avatar_url)
    embed12.set_footer(text="Page 12/12")
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=False)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    embeds = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12]
    await member.send(embeds)


#* fix me - documented on paper

@bot.event
async def on_leave(member:discord.Member):
    channel = bot.get_channel(BotOutput)
    await channel.send(f"{bot.user.name} is :frowning: at the fact that {member.name} has left {ctx.guild.name}")



#* fix me - documented on paper

@bot.command(aliases = ["tempmute"])
@commands.has_any_role('Owner', 'Head Dev', 'Head Admin', 'Admin', 'Moderator', 'Community Helper', 'Team Leader', 'Head Team Member')
async def tempmute_user(ctx,member:discord.Member,time:int,*,reason=None):
    now = datetime.datetime.now()+datetime.timedelta(minutes=5)
    embed = discord.Embed(timestamp = now, colour = discord.Colour.red(), title="Tempmute",description=f"{member.name} was muted by {ctx.author.name}").add_field(name="\u200b",
                                                        value=f'{reason} for {time}seconds')
    user_role = discord.utils.get(ctx.guild.roles,name="muted")
    await member.add_roles(user_role,reason=reason)
    await ctx.send(embed=embed)
    if user_role not in ctx.guild.roles:
        mutedRole = await ctx.guild.create_role(name="muted")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, send_messages=False,speak =False,read_message_history = False)
            await member.add_roles(mutedRole, reason=reason)
            await ctx.send(f"{member.name} has been muted ")
    await asyncio.sleep(time)
    emed = discord.Embed(timestamp = now, colour = discord.Colour.red(), title =f'{bot.user.name} believes {member.name} has learned their lesson!').add_field(name="\u200b",
                                                                        value=f"{member.name} has been unmuted after {time}.")
    await member.remove_roles(user_role)
    await ctx.send(embed = emed)