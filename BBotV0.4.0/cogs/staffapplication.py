import discord
import json
import random
import asyncio
import datetime

from discord.ext import commands
from discord.ext.commands import Cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

BOTOUTPUT = data["channels"]["staff_applications"]
staff_applications = data["channels"]["staff_applications"]
LT = data["guild"]["LT"]

class StaffApplication(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.color = random.randint(0, 0xFFFFFF)
        self.time = datetime.datetime.utcnow()

    @commands.command(aliases=['bsapp'])
    async def staffapplication1(self, ctx):

        await ctx.message.delete()

        number = random.randint(100000, 999999)
        member = ctx.author.display_name
        url = ctx.author.avatar_url

        def check(m):
            return m.author.id == ctx.author.id

        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True)
        }
        category = discord.utils.get(ctx.guild.categories, name='Applications')

        channel_name = await ctx.guild.create_text_channel(name=member, overwrites=overwrites, category=category)

        initial_message = discord.Embed(color=self.color, timestamp=self.time, title="Staff Application Hub:", description="If you are applying for Buttler Staff, press A. If you are applying to be a Dev, press B.").set_thumbnail(url=url)
        msg1 = await channel_name.send(embed=initial_message)        
        ans1 = await self.bot.wait_for('message', check=check, timeout=60)

        if ans1.content.lower() == "a":

            first_message = discord.Embed(color=self.color, timestamp=self.time, title=f"Welcome To Your Staff Application, {member}", description="All applicants will start as a Community Helper. Those given the role Community Helper, and each tier up in the staff roles, will be sent a direct message of a list of commands that become available to you, and a list of expectations of your role.""", inline=False)
            first_message.add_field(name="\u200b", value="You will have to work your way up. The purpose of this application is for us to get to know our applicants better as they transition into staff members. If it takes you longer than 1 minute to respond to a question, the application will time out! Type `Ready` when you're ready.", inline=False)
            first_message.set_thumbnail(url=ctx.author.avatar_url)
            msg1 = await channel_name.send(embed=first_message)

            answer1 = await self.bot.wait_for('message', check=check, timeout=60)

            if answer1.content.lower() == "ready":

                second_message = discord.Embed(color=self.color, timestamp=self.time, title=f"Application:", description=f"Name: {member}\n\nWhat is your age?", inline=False)
                second_message.set_thumbnail(url=ctx.author.avatar_url)
                await msg1.edit(embed=second_message)

                answer2 = await self.bot.wait_for('message', check=check, timeout=60)
                age1 = 16

                if int(answer2.content) >= 16:

                    third_message = discord.Embed(color=self.color, timestamp=self.time, title=f'Application:').add_field(name="\u200b", value=f'Name: {member}\nAge: {int(answer2.content)}\n\n\nWhy do you believe you would make a great asset to the ButtlerBot staff team?', inline=False)
                    third_message.set_thumbnail(url=ctx.author.avatar_url)
                    await msg1.edit(embed=third_message)

                    answer3 = await self.bot.wait_for('message', check=check, timeout=60)

                    if all(i.isprintable() for i in answer3.content):

                        fourth_message = discord.Embed(color=self.color, timestamp=self.time, title=f'Finished!', description=f'Congratulations, {member}! Your application has been submitted to the staff, and your Application Reference Number is {number}\n\n\nIf satisfied with your application, please type Exit', inline=False).set_thumbnail(url=url)
                        await msg1.edit(embed=fourth_message)
                                            
                        answer4 = await self.bot.wait_for('message', check=check, timeout=60)

                        if answer4.content.lower() == "exit":
                                                        
                            await answer1.delete()
                            await answer2.delete()
                            await answer3.delete()
                            await answer4.delete()
                            roles = self.bot.get_guild(LT).get_member(int(ctx.author.id)).roles
                            list_names = [role.name for role in roles]
                            final_message = discord.Embed(color=self.color, timestamp=self.time, title="Application: Status Complete", description=f"""Buttler Staff Application For: {member}\nApplication Number: {number}\nApplying For: Buttler Team Staff\nDiscord Name: {ctx.author}\nDiscord ID: {ctx.author.id}\nAge: {answer2.content}\nCurrent Roles: {', '.join(list_names[1:])}\nDiscord Member Since: {self.bot.get_guild(LT).get_member(int(ctx.author.id)).created_at.strftime("%d/%m/%y %H:%M")}\nMember Since: {self.bot.get_guild(LT).get_member(int(ctx.author.id)).joined_at.strftime("%d/%m/%y %H:%M")}""", inline=False).add_field(name="\u200b", value=f"{answer3.content}", inline=False).set_thumbnail(url=ctx.author.avatar_url)
                            await channel_name.send("This channel will automatically close in 15 seconds!")
                            channel1 = self.bot.get_channel(staff_applications)
                            await channel1.send(embed=final_message)
                            await asyncio.sleep(15)
                            await channel_name.delete()
                else:
                    await channel_name("You must be 16 years or older to apply for Buttler Staff")

            elif ans1.content.lower() == "b":

                fifth_message = discord.Embed(color=self.color, timestamp=self.time, title=f"Welcome To Your Dev Application, {member}", description=f"All applicants will start as a TempDev. Those given the role, and each tier up in the Dev role, and will be sent a direct message of a list of commands now available to you, plus a list of expectations of your role.", inline=False).set_thumbnail(url=url)
                fifth_message.add_field(name="\u200b", value="You will have to work your way up. The purpose of this application is for us to get to know our applicants better as they transition into full dev members. If you do not answer the question within 60 second, your application will timeout, and you will have to redo the application. Type `Ready` when you're ready.", inline=False)
                msg2 = await channel_name.send(embed=fifth_message)
                answer5 = await self.bot.wait_for('message', check=check, timeout=60)

                if answer5.content.lower() == "ready":

                    sixth_message = discord.Embed(color=self.color, timestamp=self.time, title=f"Application:", description=f"Name: {member}\n\nWhat is your age?")
                    sixth_message.set_thumbnail(url=ctx.author.avatar_url)
                    await msg2.edit(embed=sixth_message)
                    answer6 = await self.bot.wait_for('message', check=check, timeout=60)

                    if int(answer6.content) >= 16:

                        seventh_message = discord.Embed(color=self.color, timestamp=self.time, title=f'Application:').add_field(name="\u200b", value=f'Name: {member}\nAge: {int(answer6.content)}\n\n\nWhat do you feel is your current experience level of programming is, and why?')
                        seventh_message.set_thumbnail(url=ctx.author.avatar_url)
                        await msg2.edit(embed=seventh_message)
                        answer7 = await self.bot.wait_for('message', check=check, timeout=60)

                        if all(x.isprintable() for x in answer7.content):

                            eighth_message = discord.Embed(color=self.color, timestamp=self.time, title=f'Application:').add_field(name="\u200b", value=f'Name: {member}\nAge: {int(answer6.content)}\n\n\nDo you have a github, or some type of repo you can share, if so, please share a link, or answer N/A. This is optional.')
                            eighth_message.set_thumbnail(url=ctx.author.avatar_url)
                            await msg2.edit(embed=eighth_message)
                            answer8 = await self.bot.wait_for('message', check=check, timeout=60)

                            if all(x.isprintable() for x in answer8.content):

                                ninth_message = discord.Embed(color=self.color, timestamp=self.time, title=f'Finished!', description=f'Congratulations, {member}! Your application has been submitted to the staff, and your Application Reference Number is `{number}`. If you are satisfied with your application, please type exit!')
                                ninth_message.set_thumbnail(url=ctx.author.avatar_url)
                                await msg2.edit(embed=ninth_message)
                                answer9 = await self.bot.wait_for('message', check=check, timeout=60)

                                if answer9.content.lower() == "exit":

                                    await answer5.delete()
                                    await answer6.delete()
                                    await answer7.delete()
                                    await answer8.delete()
                                    await answer9.delete()
                                    roles = self.bot.get_guild(LT).get_member(int(ctx.author.id)).roles
                                    list_names = [role.name for role in roles]
                                    final_message = discord.Embed(color=self.color, timestamp=self.time, title="Application: Status Complete", description=f"""Buttler Staff Application For: {ctx.author.name}\nApplication Number: {number}\nApplying For: Buttler Dev Team\nDiscord Name: {ctx.author}\nDiscord ID: {ctx.author.id}\nAge: {answer6.content}\nCurrent Roles: {', '.join(list_names[1:])}\nDiscord Member Since: {self.bot.get_guild(LT).get_member(int(ctx.author.id)).created_at.strftime("%d/%m/%y %H:%M")}\n{self.bot.get_guild(LT).name} Member Since: {self.bot.get_guild(LT).get_member(int(ctx.author.id)).joined_at.strftime("%d/%m/%y %H:%M")}""").add_field(name="\u200b", value=f"{answer7.content}", inline=False).set_thumbnail(url=ctx.author.avatar_url)
                                    channel2 = self.bot.get_channel(staff_applications)
                                    await channel2.send(embed=final_message)
                                    await channel_name.send(":red_circle: **__THIS CHANNEL WILL AUTOMATICALLY DELETE IN 15 SECONDS__**:red_circle:")
                                    await asyncio.sleep(15)
                                    await channel_name.delete()
                    else:
                        await channel_name.send("You must be 16 years or older to apply for Buttler Staff")                                                                           
def setup(bot):
    bot.add_cog(StaffApplication(bot))