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