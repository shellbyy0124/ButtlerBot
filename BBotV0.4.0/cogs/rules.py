import discord
import json
import datetime
import random

from discord.ext import commands
from discord.ext.commands import Cog 

with open('./rules.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

ruleone = data["rules"]["one"]
ruletwo = data["rules"]["two"]
rulethree = data["rules"]["three"]
rulefour = data["rules"]["four"]
rulefive = data["rules"]["five"]
rulesix = data["rules"]["six"]
ruleseven = data["rules"]["seven"]
ruleeight = data["rules"]["eight"]
rulenine = data["rules"]["nine"]
ruleten = data["rules"]["ten"]

with open('./master.json', 'r', encoding='utf-8-sig') as g:
    data = json.load(g)

LT = data["guild"]["LT"]
errors = data["channels"]["errors"]

class Rules(commands.Cog):

    def __init__(self, bot):

        self.bot=bot
        self.color=random.randint(0, 0xFFFFFF)
        self.time=datetime.datetime.utcnow()
        self.url=self.bot.user.avatar_url
    
    @commands.command()
    async def rule(self, ctx):
        
        def check(m):
            return ctx.author == m.author

        embed1 = discord.Embed(color=self.color, timestamp=self.time, title=f"{LT.name}'s Rules Table Of Contents:", description="""Please Select From The Following:
                                                                                                                                    One: Respect
                                                                                                                                    Two: Inferior/Superior
                                                                                                                                    Three: Insults
                                                                                                                                    Four: Attitudes
                                                                                                                                    Five: Spamming
                                                                                                                                    Six: Restrictions
                                                                                                                                    Seven: Chat Topics
                                                                                                                                    Eight: Intimidation
                                                                                                                                    Nine: Markups
                                                                                                                                    Ten: Invites
                                                                                                                                    Eleven: Staff Restrictions
                                                                                                                                    Please Enter Your Answer As One, Two, Three, Etc.""", inline=False).set_thumbnail(url=self.url)
        msg1 = await ctx.send(embed=embed1)
        ans1 = await self.bot.wait_for('message', check=check)

        if ans1.content.lower() == "one":
            
            embed2 = discord.Embed(color=self.color, timestamp=self.time, title="Rule Number 1:", description="Respect of your peers is a must at all times. You can't just be rude. It's not cool >.>").set_thumbnail(url=self.url)
            await msg1.edit(embed=embed2)

        elif ans1.content.lower() == "two":
            
            embed3 = discord.Embed(color=self.color, timestamp=self.time, title="Rule Number 2:", description="Making someone feel inferior, or acting superior to others, is not allowed. Don't let your ego cash a check your account can't cash ^.^").set_thumbnail(url=self.url)
            await msg1.edit(embed=embed3)

        elif ans1.content.lower() == "three":
            
            embed4 = discord.Embed(color=self.color, timestamp=self.time, title="Rule Number 3:", description="Telling someone that their question is stupid, even in a joking manner, is not allowed. The only stupid question that exists is a question that isn't asked!", inline=False).set_thumbnail(url=self.url)
            await msg1.edit(embed=embed4)

        elif ans1.content.lower() == "four":
            
            embed5 = discord.Embed(color=self.color, timestamp=self.time, title="Rule Number 4:", description="Being rude or indecent because you assume that everyone should have a pre-existing level of knowledge of python before requesting help is not allowed. We learn together in this community!", inline=False).set_thumbnail(url=self.url)
            await msg1.edit(embed=embed5)

        elif ans1.content.lower() == "five":

            embed6 = discord.Embed(color=self.color, timestamp=self.time, title="Rule Number 5:", description="No Spamming! This includes but is not limited to: Over posting, asking the same question repetatively, and abusing the `@` ability when not necessary is not allowed. If you need assistance, please create a support channel!", inline=False).set_thumbnail(url=self.url)
            await msg1.edit(embed=embed6)

        elif ans1.content.lower() == "six":

            embed7 = discord.Embed(color=self.color, timestamp=self.time, title="Rule Number 6:", description="We have members of all ages that are welcome into this discord. No Cursing, NSFW, etc. It is not allowed, and may result in a perma-ban", inline=False).set_thumbnail(url=self.url)
            await msg1.edit(embed=embed7)

        elif ans1.content.lower() == "seven":

            embed8 = discord.Embed(color=self.color, timestamp=self.time, title="Rule Number 7:", description="Keep the chats in accordance with the channel topics. If you're not sure, read the top of the channel window, or ask", inline=False).set_thumbnail(url=self.url)
            await msg1.edit(embed=embed8)

        elif ans1.content.lower() == "eight":
            
            embed9 = discord.Embed(color=self.color, timestamp=self.time, title="Rule Number 8:", description="No Intimidation! We grow and learn together as a team from day one, and on! If you need further clearance, please refer to rule number 3 and 4", inline=False).set_thumbnail(url=self.url)
            await msg1.edit(embed=embed9)

        elif ans1.content.lower() == "nine":

            embed10 = discord.Embed(color=self.color, timestamp=self.time, title="Rule Number 9:", description="Use the proper markups when submitting code. Discord supports many languages!", inline=False).set_thumbnail(url=self.url)
            await msg1.edit(embed=embed10)

        elif ans1.content.lower() == "ten":

            embed11 = discord.Embed(color=self.color, timestamp=self.time, title="Rule Number 10", description="Do not create your own invite to this discord. An invite link has already been created for you to use. Type '>binvite' for the link!", inline=False).set_thumbnail(url=self.url)
            await msg1.edit(embed=embed11)

        elif ans1.content.lower() == "eleven":
            
            roles = []

            for r in ctx.guild.roles:
                if not r.managed:
                    roles.append(r)
            embed12 = discord.Embed(color=self.color, timestamp=self.time, title="Staff Restrictions:", description=f"Staff Members include {roles.name}, and are allowed to exercise the rules, and warning tiers as they see fit. In the event that you feel any staff member is abusing their power, please create a support channel, and an admin will be with you shortly.", inline=False).set_thumbnail(url=self.url)
            await msg1.edit(embed=embed12)

        else:
            role = discord.utils.get(ctx.guild.roles, name="Dev")
            role1 = discord.utils.get(ctx.guild.roles, name="Head Dev")
            error = discord.Embed(color=discord.Colour.red(), timestamp=self.time, title="Error!", description=f"{role1.mention} and {role.mention} an error has thrown for the rules.py>first command")
            channel = self.bot.get_channel(errors)
            a = await channel.send(error)
            await a.pin()

def setup(bot):
    bot.add_cog(Rules(bot))