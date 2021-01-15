import discord
import json
import random
import datetime

from discord.ext import commands
from discord.ext.commands import Cog

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

members_join = data["channels"]["members_join"]
members_leave = data["channels"]["members_leave"]
LT = data["guild"]["LT"]
rules_agreement_logs = data["channels"]["rules_agreement_logs"]

class DMUser(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):

        color = random.randint(0, 0xFFFFFF)
        timestamp = datetime.datetime.utcnow()
        welcome = discord.Embed(color=color, timestamp=timestamp, title=f"Hi and Welcome!", description=f"My name is {self.bot.user.name}, and I will be your virtual assistant during your stay here at the Learning Together Discord Community! :smile:", inline=False)
        welcome.add_field(name="To Get Started:", value=f"You must be a member of {self.bot.get_guild(LT)} for at least 5 minutes before being able to chat with the community, so in the meantime I would like to cover some ground rules:", inline=False)
        welcome.add_field(name="First:", value="Respect of your peers is a must at all times. Making someone feel inferior to you is prohibited! Telling someone that their question is stupid is prohibited.", inline=False)
        welcome.add_field(name="Second:", value="No Spamming! This includes: using the @ ability when there are sufficient support channels for your needs", inline=False)
        welcome.add_field(name="Third:", value="We have members of all ages that are welcome into this discord. No Cursing, NSFW, etc! It is prohibited!", inline=False)
        welcome.add_field(name="Fourth", value="Keep the chats in accordance with the channels topic. Not sure? Look Up :smile:", inline=False)
        welcome.add_field(name="Fifth:", value="No Intimidation! We grow and learn together from day one and on", inline=False)
        welcome.add_field(name="Sixth:", value="Use the proper markups when submitting code. Discord supports many languages!", inline=False)
        welcome.add_field(name="Seventh:", value="When posting links in the **_Resources_** category, you may __ONLY__ post links that are pertinent to that channel. Any NSFW gags, hacks, trackers, etc will result in your account getting reported. We have all ages in this group!", inline=False)
        welcome.add_field(name="Eighth:", value="Use the #bot_spam channel for all of your bot commands that are not pertinent with your current conversation, or if you need/want to look something up!", inline=False)
        welcome.add_field(name="Ninth:", value="Do not create your own invite to this discord. An invite link has already been created for you to use. Type `>binbite` for the link", inline=False)
        welcome.add_field(name="And Finally:", value="If you have any more questions, use `>buttlerhelp` to call me, and if you'd like to get a better look at the rules, `>buttlerrules`", inline=False)
        welcome.add_field(name="Note:", value="In order to gain access to the discord, please type `!agree`. If the command doesn't work, then please get in touch with a staff member!", inline=False)

        faq1 = discord.Embed(color=color, timestamp=timestamp, title="FAQ's")
        faq1.add_field(name="Why are there no active bots in the server except buttler?", value="We are in the very beginning stages of creating this community, and the bots that are used within it. We are building custom bots from scratch for our community, and to match what our community is about. Please bare with us as we are working diligently to get this community started, and rocketed off to the moon!", inline=False)
        faq1.add_field(name="What do I do if I would like to submit an idea for a bot?", value="Please submit your ideas for bots by using `>bbsubmit <idea>` to send your submission to our lovely developers!", inline=False)
        faq1.add_field(name="Where can I find beginner resources for Python?", value="You can venture over to the _**Resources**_ category where you can find different channels containing various links for all types of information. You're also welcome to post your own links for others to use as well, however, please stick to the rules when doing so!", inline=False)
        faq1.add_field(name="How often can I get a coding challenge?", value="Coding Challenges are setup on a 24 hour timer. There is no command to receive a challenge. They will be posted in the **__Coding Challenges__** category as they are sent out.", inline=False)
        faq1.add_field(name="How does the ranking system work?", value="Kastien is currently developing that system, and thus at this time we have no information. It is still a product in progress :penguin:", inline=False)
        faq1.add_field(name="How do I need to post my code in the community?", value="Please use the backticks before and after your code when posting. If you're unsure of what a backtick is, it's the key underneath your ESC key and next to your `1` key on your keyboared.", inline=False)
        
        await member.send(embed=welcome)
        await member.send(embed=faq1)

        channel = self.bot.get_channel(members_join)
        await channel.send(f"Let's welcome {member.name} to {self.bot.get_guild(LT).name}!")

        msg = await self.bot.wait_for("message", check=lambda m: m.author.id == member.id and not m.guild)
        
        if msg.content.lower() == "!agree":

            role = discord.utils.get(member.guild.roles, name="Members")
            await member.add_roles(role)

            channel = self.bot.get_channel(rules_agreement_logs)
            agreement = discord.Embed(color=color, timestamp=timestamp, title=f'{member.name} has agreed to the rules on {timestamp}')
            agreement.set_thumbnail(url=member.avatar_url)
            await channel.send(embed=agreement)

        else:

            await member.send("Please Agree To The Rules To Gain Access To The Discord")

        #some code to check database. if member exists - pass, else - create and add to db
 
def setup(bot):
    bot.add_cog(DMUser(bot))