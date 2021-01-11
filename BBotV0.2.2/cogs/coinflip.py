import discord
import random
import datetime
import json

from discord.ext import commands
from discord.ext.commands import cog

class CP(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command(aliases=['bflip'])
    async def cpgame(self, ctx, side, amount):

        color = random.randint(0, 0xFFFFFF)
        time = datetime.datetime.utcnow()
        num = random.randint(0, 1)
        amount = int(amount)
        errormsg = "You are trying to bet more than you are worth! Use (command for balance inquiry) to see what your current balance is!"
        errormsg1 = "Sorry that is not a valid entry. Please Try again! `>bflip <side> <amount>"

        A = "heads"
        B = "tails"

        with open('./master.json', 'r', encoding='utf-8-sig') as user:
            data = json.load(user)

        balance = data["users"][str(ctx.author.name)]["bank"]

        if int(amount) <= int(balance):
            
            if num == 0 and side.lower() == A:

                heads = discord.Embed(color=color, timestamp=time, title="You Flipped Heads, and Won!", value=f"You have won {amount}! Your new balance has been updated!")

                file = discord.File("/home/shellbyy/Desktop/repofolder/ButtlerBot/BBotV0.2.2/bot_images/quarterheads.jpg", filename="quarterheads.jpg")
                heads.set_thumbnail(url="attachment://quarterheads.jpg")
                await ctx.send(embed=heads, file=file)

                with open('./master.json', 'r', encoding='utf-8-sig') as p:
                    data= json.load(p)

                data["users"][str(ctx.author.name)] = {"name":ctx.author.name,"bank":1000}

                data["users"][str(ctx.author.name)]["bank"] += amount

                info = data["users"][str(ctx.author.name)]["bank"]

                message = f"Your updated balance is ${info}"

                await ctx.send(f"{message}")

                with open('./master.json', 'w', encoding='utf-8-sig') as file:
                    data = json.dump(data, file, indent=4)
                            
            elif num == 1 and side.lower() == A:

                heads1 = discord.Embed(color=color, timestamp=time, title="You Flipped Heads, and Lost!", value=f"You have lost {amount}! Your new balance has been updated!")
                
                file = discord.File("/home/shellbyy/Desktop/repofolder/ButtlerBot/BBotV0.2.2/bot_images/quarterheads.jpg", filename="quarterheads.jpg")
                heads1.set_thumbnail(url="attachment://quarterheads.jpg")
                await ctx.send(embed=heads1, file=file)

                with open('./master.json', 'r', encoding='utf-8-sig') as p:
                    data= json.load(p)

                data["users"][str(ctx.author.name)] = {"name":ctx.author.name,"bank":1000}

                data["users"][str(ctx.author.name)]["bank"] -= amount

                info = data["users"][str(ctx.author.name)]["bank"]

                message = f"Your updated balance is ${info}"

                await ctx.send(f"{message}")

                with open('./master.json', 'w', encoding='utf-8-sig') as file:
                    data = json.dump(data, file, indent=4)
                
            elif num == 0 and side.lower() == B:

                tails = discord.Embed(color=color, timestamp=time, title="You Flipped Tails, and Won!", value=f"You have won {amount}! Your new balance has been updated!")
                
                file = discord.File("/home/shellbyy/Desktop/repofolder/ButtlerBot/BBotV0.2.2/bot_images/quartertails.png", filename="quartertails.png")
                tails.set_thumbnail(url="attachment://quartertails.png")
                await ctx.send(embed=tails, file=file)

                with open('./master.json', 'r', encoding='utf-8-sig') as p:
                    data= json.load(p)

                data["users"][str(ctx.author.name)] = {"name":ctx.author.name,"bank":1000}

                data["users"][str(ctx.author.name)]["bank"] += amount

                info = data["users"][str(ctx.author.name)]["bank"]

                message = f"Your updated balance is ${info}"

                await ctx.send(f"{message}")

                with open('./master.json', 'w', encoding='utf-8-sig') as file:
                    data = json.dump(data, file, indent=4)

            elif num == 1 and side.lower() == B:

                tails1 = discord.Embed(color=color, timestamp=time, title="You Flipped Tails, and Lost!", value=f"You have lost {amount}! Your new balance has been updated!")
                
                file = discord.File("/home/shellbyy/Desktop/repofolder/ButtlerBot/BBotV0.2.2/bot_images/quartertails.png", filename="quartertails.png")
                tails1.set_thumbnail(url="attachment://quartertails.png")
                await ctx.send(embed=tails1, file=file)

                with open('./master.json', 'r', encoding='utf-8-sig') as p:
                    data= json.load(p)

                data["users"][str(ctx.author.name)] = {"name":ctx.author.name,"bank":1000}

                data["users"][str(ctx.author.name)]["bank"] -= amount

                info = data["users"][str(ctx.author.name)]["bank"]

                message = f"Your updated balance is ${info}"

                await ctx.send(f"{message}")

                with open('./master.json', 'w', encoding='utf-8-sig') as file:
                    data = json.dump(data, file, indent=4)

            else:
                return ctx.send(errormsg)
        else:
            return ctx.send(errormsg1)
                


def setup(bot):
    bot.add_cog(CP(bot))