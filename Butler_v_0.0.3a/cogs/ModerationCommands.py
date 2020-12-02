#*THESE COMMANDS ARE FOR FUTURE UPDATES. THERE ARE NO COGS, AND THUS IGNORE THIS COG FOLDER WHEN BRINGING BOT ONLINE.



# @bot.command( aliases=['shutdown'])
# @commands.has_any_role('Owner', 'Team Leader', 'Head Dev', 'Dev', 'Head Admin', 'Head Team Member')
# async def shutdown_channel(ctx, channel:discord.TextChannel):
#     staff = ['Owner', 'Head Dev', 'Head Admin', 'Admins', 'Moderators', 'Team Leader', 'Head Team Member']
#     nonstaff = ['Community Helpers', 'KasMek Programming Team', 'Team Captain', 'Members', 'Bot Tester', 'Verified', 'everyone']
#     for roles in staff:
#         if role.name in roles == staff:
#             pass
#         else:
#             for nonstaffroles in nonstaff:
#                 await ctx.channel.set_permissions(nonstaff, send_messages=False)


# building a filter

# @bot.event
# async def on_message(ctx, *, message):
#     if message.author.bot:
#         return
#     else:
#         allowed_links = ['https://paste.pythondiscord.com/', 'https://pastebin.com/', 'https://rickandmortyapi.com/api/character', 'https://discord.gg/QyMuAaD9gs']
#         blocked_links = ['https://www.pornhub.com']
        
#         for awl in allowed_links:
#              if awl in message.content:
#                  return
#         for bwl in blocked_links:
#              if bwl in message.content:
#                  await ctx.send(f'{message.author}, you cannot use that link in {ctx.guild.name}! You are only allowed to use https://paste.pythondiscord.com/, and https://pastebin.com/ to post your code!')
#                  await message.delete()
#     await bot.process_commands(message)