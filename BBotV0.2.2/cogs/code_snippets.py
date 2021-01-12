import asyncio
import datetime
import discord
import sqlite3
import json
import random

from discord.ext import commands
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

data = data
commands = data["channels"]["commands"]
needs_approving = data["channels"]["needs_approving"]
kastien = data["users"]["kastien"]

class DataBaseStuff(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Dev')
    async def createDatabase(self, ctx):

        def check(m):
            return ctx.author == ctx.message.author
        
        color = random.randint(0, 0xFFFFFF)
        time = datetime.datetime.utcnow()
        bot = self.bot.user.avatar_url
        role = discord.utils.get(ctx.guild.roles, name='Head Dev')
        member = ctx.author
        error = discord.Embed(color=discord.Colour.red(), timestamp=time, title=":red_circle:**__DO NOT PRESS ANOTHER KEY, OR ENTER ANYTHING ELSE INTO THIS CHANNEL!__**:red_circle:", description=f"""If you've received this error, 
                                                                                                                                                                                                        please take a screen shot of the 
                                                                                                                                                                                                        image, upload it to [imgur](), then 
                                                                                                                                                                                                        go to the support category, and find 
                                                                                                                                                                                                        the channel with your name on it. Copy 
                                                                                                                                                                                                        and paste your imgur image link into 
                                                                                                                                                                                                        the text field, and press enter so that 
                                                                                                                                                                                                        it's pinned to the top of the support 
                                                                                                                                                                                                        window, and a developer will be with you 
                                                                                                                                                                                                        shortly!""", inline=False)
        file = discord.File("/home/shellbyy/Desktop/repofolder/ButtlerBot/BBotV0.2.2/bot_images/error.png", filename="error.png")
        error.set_thumbnail(url="attachment://error.png")

        if ctx.message.channel.name == commands:

            category = discord.utils.get(ctx.guild.categories, name='Devs Only')
            channel = await ctx.guild.create_text_channel(ctx.author.display_name, category=category)
            await channel.edit(sync_permissions=True)

            embed1 = discord.Embed(color=color, timestamp=time, title="Welcome To The ButtlerBot Database Builder!", description="Please Enter The Name Of Your Database:", inline=False).set_footer(text="KasMek, LLC. database editor").set_thumbnail(url=bot)
            msg1 = await channel.send(embed=embed1)
            ans1 = await self.bot.wait_for('message', check=check)

            if all(i.isprintable() for i in ans1.content):
                
                await ans1.delete()
                embed2 = discord.Embed(color=color, timestamp=time, title="ButtlerBot Database Editor:", description=f"**__Database Name:__** {ans1.content}\n\nEnter Your First Tables Name:", inline=False).set_footer(text="KasMek, LLC. database editor").set_thumbnail(url=bot)
                await msg1.edit(embed=embed2)
                ans2 = await self.bot.wait_for('message', check=check)

                if all(i.isprintable() for i in ans2.content):

                    await ans2.delete()
                    embed3 = discord.Embed(color=color, timestamp=time, title="ButtlerBot Database Editor:", description=f"**__Database Name:__** {ans1.content}\n**__First Table Name:__** {ans2.content}\n\nDo You Have Any Other Tables To Include? Yes Or No?", inline=False).set_footer(text="KasMek, LLC. database editor").set_thumbnail(url=bot)
                    await msg1.edit(embed=embed3)
                    ans3 = await self.bot.wait_for('message', check=check)

                    if ans3.content.lower() == "yes":

                        await ans3.delete()
                        embed4 = discord.Embed(color=color, timestamp=time, title="ButtlerBot Database Editor:", description=f"**__Databse Name:__** {ans1.content}\n**__First Table Name:__** {ans2.content}\n\nEnter Your Second Tables Name:", inline=False).set_footer(text="KasMek, LLC. database editor").set_thumbnail(url=bot)
                        await msg1.edit(embed=embed4)
                        ans4 = await self.bot.wait_for('message', check=check)

                        if all(i.isprintable() for i in ans4.content):

                            await ans4.delete()
                            embed5 = discord.Embed(color=color, timestamp=time, title="ButtlerBot Database Editor:", description=f"**__Databse Name:__** {ans1.content}\n**__First Table Name:__** {ans2.content}\n**__Second Table Name:__** {ans4.content}\n\nDo You Have Any Other Tables To Include? Yes Or No?", inline=False).set_footer(text="KasMek, LLC. database editor").set_thumbnail(url=bot)
                            await msg1.edit(embed=embed5)
                            ans5 = await self.bot.wait_for('message', check=check)

                            if ans5.content.lower() == "yes":
                                pass
                                # some code to repeat allowing the ctx.author to create as many tables as their new database needs without having to create 1000000 embeds on repeat for millions of lines of code, but don't break the code either.
                            else:
                                await ans5.delete()
                                final_embed1 = discord.Embed(color=color, timestamp=time, title=f"__Your New DataBase Has Been Sent To {role.mention} for approval!__", description=f"**__Database Name:__**\n{ans1.content}\n**__First Table Name:__**\n{ans2.content}\n**__Second Table Name:__**\n{ans4.content}\n**__Database Creator:__**\n{ctx.author.display_name}", inline=False).set_footer(text="Buttler Database Editor").set_thumbnail(url=ctx.author.avatar_url)
                                await channel.send(embed=final_embed1)
                                await channel.send(":red_circle:**__This Channel Will Delete In 10 Seconds__**:red_circle:")
                                channel1 = self.bot.get_channel(needs_approving)
                                a = await channel1.sent(embed=final_embed1)
                                await a.pin()
                                await channel1.purge(limit=1)
                                await asyncio.sleep(10)
                                await channel.delete()

                                a = await channel1.send("To Approve This Database, enter yes. To Deny This Database, enter no and then a reason why you denied it so that the user can understand why, and improve if need be.")

                                def check(m):
                                    return kastien == ctx.message.author

                                ans6 = await self.bot.wait_for('message', check=check, timeout=None)

                                if ans6.content.lower() == "yes":

                                    await member.send(embed=final_embed1)
                                    await member.send(":star:**___YOUR EMBED WAS APPROVED!!!! WOOOOHOOOOO__**")

                                    database_name = ans1.content.upper()
                                    table_name_one = ans2.content.upper()
                                    table_name_two = ans4.content.upper()
                                    # a loop that goes along with the loop for them to enter multiple tables in one editor

                                    conn = sqlite3.connet('some.db')
                                    c = conn.cursor()
                                    c.execute("""CREATE TABLE str(ans1.content) (
                                                # go up to line 88 and create the next if/else statement to setup for a loop of adding rows to the tables inside their new database
                                                """)
                                else:
                                    reason = await self.bot.wait_for('message', check=check, timeout=None)
                                    await member.send(f"Sorry, {member.display_name} but your DataBase was not approved for creation, and here's the reason why {reason.content}")
                        else:
                            await channel.send(embed=error)
                    else:
                        
                        await ans3.delete()
                        final_embed2 = discord.Embed(color=color, timestamp=time, title=f"__Your New Database Has Been Sent To {role.mention} for approval!__", description=f"**__Database Name:__** {ans1.content}\n**__First Table Name:__** {ans2.content}\n**__Database Creator:__**\n{ctx.author.display_name}", inline=False).set_footer(text="Buttler Database Editor").set_footer(text="KasMek, LLC. database editor").set_thumbnail(url=ctx.author.avatar_url)
                        await channel.send(embed=final_embed2)
                        await channel.send(":red_circle:**__This Channel Will Delete In 10 Seconds__**:red_circle:")
                        await asyncio.sleep(10)
                        await channel.delete()
                        channel2 = await self.bot.get_channel(needs_approving)
                        b = await channel2.send(embed=final_embed2)
                        await b.pin()
                        await channel2.purge(limit=1)
                else:
                    await channel.send(embed=error)
            else:
                await channel.send(embed=error)
        else:
            await ctx.send("I know you had better be going to the dev section with this mess instead of trying to give all of our business out to the street!")
            await asyncio.sleep(10)

def setup(bot):
    bot.add_cog(DataBaseStuff(bot))