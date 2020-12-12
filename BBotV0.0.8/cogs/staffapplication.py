import discord
import json
import random
import asyncio

from os import error
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands.core import check

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

kastien = data["kastien"]
mekasu = data["mekasu"]
TheOnlyCarl = data["TheOnlyCarl"]
LT = data["LT"]
staff_applications = data["staff_applications"]
staff_apply_here = data["staff_apply_here"]

class StaffApplication(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command(aliases=['bsapp'])
    async def staffapplication1(self, ctx):

        member = ctx.author

        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True)
        }
        category = discord.utils.get(ctx.guild.categories, name='Application_Channels')

        channel = await ctx.guild.create_text_channel(ctx.author.name, overwrites=overwrites, category=category)
        

        initial_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Staff Application Hub:", description="If you are applying for Buttler Staff, press A. If you are applying to be a Dev, press B.")
        msg1 = await channel.send(embed=initial_message)
        ans1 = await self.bot.wait_for('message')

        A = 'a'
        B = 'b'

        if ans1.content.lower() == A:

            number = random.randint(100000, 999999)

            first_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Welcome To Your Staff Application, {member.name}", description="All applicants will start as a Community Helper. Those given the role Community Helper, and each tier up in the staff roles, will be sent a direct message of a list of commands now available to you, and a list of expectations of your role.").add_field(name="\u200b", value="You will have to work your way up. The purpose of this application is for us to get to know our applicants better as they transition into staff members. Type `Ready` when you're ready.")

            await msg1.edit(embed=first_message)
            answer1 = await self.bot.wait_for('message')

            B = "ready"

            if answer1.content.lower() == B:
                pass
            else:
                await channel.send(":red_circle: That is not a valid entry. Go back to the #bot_spam channel and restart the application process. This window will close in 15 seconds.")
                await asyncio.sleep(15)
                await channel.delete()

            second_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Application:", description=f"Name: {ctx.author.name}\n\nWhat is your age?")
            await msg1.edit(embed=second_message)
            answer2 = await self.bot.wait_for('message')

            age1 = 16

            if int(answer2.content) < age1:
                
                await channel.send(f"Apologies {ctx.author.name}, but you must be at least 16 year's old to apply for staff within this community. This window will close in 15 seconds.")
                await asyncio.sleep(15)
                await channel.delete()
                return
            else:

                third_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f'Application:').add_field(name="\u200b", value=f'Name: {ctx.author.name}\nAge: {int(answer2.content)}\n\n\nWhy do you believe you would make a great asset to the ButtlerBot staff team?')
                await msg1.edit(embed=third_message)

                answer3 = await self.bot.wait_for('message')

                if all(x.isalpha() or x.isspace() for x in answer3.content):
                    pass
                else:
                    await channel.send("That is not a valid entry! Go Back to the #bot_spam channel, and start the application process over. This window will close in 15 seconds")
                    await asyncio.sleep(15)
                    await channel.delete()
                    return

            fourth_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f'Finished!', description=f'Congratulations, {ctx.author.name}! Your application has been submitted to the staff, and your Application Reference Number is {number}\n\n\nIf satisfied with your application, please type Exit')
            await msg1.edit(embed=fourth_message)
            answer4 = await self.bot.wait_for('message')

            A = "exit"

            if answer4.content.lower() == A:

                roles = self.bot.get_guild(LT).get_member(member.id).roles
                list_names = [role.name for role in roles]

                final_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Application: Status Complete", description=f"""Buttler Staff Application For: {ctx.author.display_name}
                                                                                                                Application Number: {number}
                                                                                                                Discord Name: {ctx.author}
                                                                                                                Discord ID: {ctx.author.id}
                                                                                                                Age: {answer2.content}
                                                                                                                Current Roles: {', '.join(list_names[1:])}
                                                                                                                Discord Member Since: {self.bot.get_guild(LT).get_member(member.id).created_at.strftime("%d/%m/%y %H:%M")}
                                                                                                                {self.bot.get_guild(LT).name} Member Since: {self.bot.get_guild(LT).get_member(member.id).joined_at.strftime("%d/%m/%y %H:%M")}""").add_field(name="\u200b", value=f"{answer3.content}")
                submit = self.bot.get_channel(staff_applications)
                await submit.send(embed=final_message)
                await asyncio.sleep(10)
                await channel.delete()

        elif ans1.content.lower() == B:

            number = random.randint(100000, 999999)

            fifth_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Welcome To Your Dev Application, {member.name}", description=f"All applicants will start as a TempDev. Those given the role, and each tier up in the Dev roles, will be sent a direct message of a list of commands now available to you, and a list of expectations of your role.").add_field(name="\u200b", value="You will have to work your way up. The purpose of this application is for us to get to know our applicants better as they transition into full dev members. Type `Ready` when you're ready.")

            await msg1.edit(embed=fifth_message)
            answer6 = await self.bot.wait_for('message')

            C = "ready"

            if answer6.content.lower() == C:
                pass
            else:
                return await channel.send("Please Enter 'Ready'")

            sixth_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Application:", description=f"Name: {ctx.author.name}\n\nWhat is your age?")
            await msg1.edit(embed=sixth_message)
            answer7 = await self.bot.wait_for('message')

            age1 = 16

            if int(answer7.content) < age1:
                
                await channel.send(f"Apologies {ctx.author.name}, but you must be at least 16 year's old to apply for staff within this community. This window will close in 15 seconds.")
                await asyncio.sleep(15)
                await channel.delete()
                return
            else:
                seventh_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Application:", description=f"Name: {ctx.author.name}\nAge: {int(answer7.content)}\n\nHow long have you been programming for?")
                await msg1.edit(embed=seventh_message)
                answer8 = await self.bot.wait_for('message')

                if all(i.isprintable() for i in answer8.content):
                    pass
                else:
                    await channel.send(":red_circle: That is not a valid entry. Go back to the #bot_spam channel, and start the application process over. This window will close in 15 seconds")
                    await asyncio.sleep(15)
                    await channel.delete()

                eighth_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"Application: {member.name}", description=f"Age: {answer7.content}\nProgramming Length Of Time: {answer8.content}\n\nWhat do you feel is your current experience level with programming?")
                await msg1.edit(embed=eighth_message)
                answer9 = await self.bot.wait_for('message')

                if all(i.isprintable() for i in answer9.content):
                    pass
                else:
                    return await channel.send(":red_circle: That is not a valid entry. Type the command again to restart")

            ninth_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"CONGRATULATIONS, {member.name}!", description=f"You have completed the application! We will be in touch with you shortly. Your application number is {number}. After you've written that down, type exit to close this window!")
            await msg1.edit(embed=ninth_message)
            answer10 = await self.bot.wait_for('message')

            A = "exit"

            if answer10.content.lower() == A:

                roles = self.bot.get_guild(LT).get_member(member.id).roles
                list_names = [role.name for role in roles]

                final_message = discord.Embed(color=random.randint(0, 0xFFFFFF), title="Application: Status Complete", description=f"""Buttler Staff Application For: {ctx.author.display_name}
                                                                                                                Application Number: {number}
                                                                                                                Discord Name: {ctx.author}
                                                                                                                Discord ID: {ctx.author.id}
                                                                                                                Age: {answer7.content}
                                                                                                                Current Roles: {', '.join(list_names[1:])}
                                                                                                                Discord Member Since: {self.bot.get_guild(LT).get_member(member.id).created_at.strftime("%d/%m/%y %H:%M")}
                                                                                                                {self.bot.get_guild(LT).name} Member Since: {self.bot.get_guild(LT).get_member(member.id).joined_at.strftime("%d/%m/%y %H:%M")}
                                                                                                                Length Of Time Programming: {answer8.content}
                                                                                                                Experience Level in Programming: {answer9.content}""")
                submit = self.bot.get_channel(staff_applications)
                await submit.send(embed=final_message)
                await asyncio.sleep(10)
                await channel.delete()
            

        


            
            



                                                                                                            
def setup(bot):
    bot.add_cog(StaffApplication(bot))