import asyncio
import discord
import datetime
import json
import random

from discord.ext import commands
from discord.ext.commands import Cog 

class CP(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.time = datetime.datetime.utcnow()
        
    @commands.command()
    async def cflip(self, ctx, side, amount:int):

        async with ctx.typing():

            num = random.choice(0, 11)

            await asyncio.sleep(num)

        num = random.randint(0, 1)

        with open('./users.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)

        balance = data["users"][str(ctx.author.name)]["bank"]

        if amount < balance:

            if num == 0 and side.lower() == "heads":

                with open('./users.json', 'r', encoding='utf-8-sig') as p:
                    data = json.load(p)

                data["users"][str(ctx.author.name)]["bank"] += amount

                new_bal = data["users"][str(ctx.author.name)]["bank"]

                with open('./users.json', 'w', encoding='utf-8-sig') as file:
                    data = json.dump(data, file, indent=4)

                embed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title=f"You Flipped {side.lower()}, and Won!", description=f"__Name:__ {ctx.author.name}\n__Bet:__ {amount}\n__Won/Lost:__ Won\n__Previous Balance:__ {balance}\n__New Balance:__ {new_bal}", inline=False)

                file = discord.File('/root/discord_bots/ButtlerBot/BBotV0.4.0/bot_images/quarterheads.jpg', filename='quarterheads.jpg')
                embed1.set_thumbnail(url='attachment://quarterheads.jpg')
                a = await ctx.send(embed=embed1, file=file)
                await asyncio.sleep(20)
                await a.delete()                

            elif num == 1 and side.lower() == "heads":

                with open('./users.json', 'r', encoding='utf-8-sig') as p:
                    data = json.load(p)
                
                data["users"][str(ctx.author.name)]["bank"] -= amount

                new_bal = data["users"][str(ctx.author.name)]["bank"]

                with open('./users.json', 'w', encoding='utf-8-sig') as file:
                    data = json.dump(data, file, indent=4)

                embed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title=f"You Flipped {side.lower()}, and Lost!", description=f"__Name:__ {ctx.author.name}\n__Bet:__ {amount}\n__Won/Lost:__ Lost\n__Previous Balance:__ {balance}\n__New Balance:__ {new_bal}", inline=False)

                file = discord.File('/root/discord_bots/ButtlerBot/BBotV0.4.0/bot_images/quarterheads.jpg', filename='quarterheads.jpg')
                embed1.set_thumbnail(url='attachment://quarterheads.jpg')
                a = await ctx.send(embed=embed1, file=file)
                await asyncio.sleep(20)
                await a.delete()

            elif num == 0 and side.lower() == "tails":
                
                with open('./users.json', 'r', encoding='utf-8-sig') as p:
                    data = json.load(p)
                
                data["users"][str(ctx.author.name)]["bank"] += amount

                new_bal = data["users"][str(ctx.author.name)]["bank"]

                with open('./users.json', 'w', encoding='utf-8-sig') as file:
                    data = json.dump(data, file, indent=4)

                embed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title=f"You Flipped {side.lower()}, and Won!", description=f"__Name:__ {ctx.author.name}\n__Bet:__ {amount}\n__Won/Lost:__ Lost\n__Previous Balance:__ {balance}\n__New Balance:__ {new_bal}", inline=False)

                file = discord.File('/root/discord_bots/ButtlerBot/BBotV0.4.0/bot_images/quartertails.png', filename='quartertails.png')
                embed1.set_thumbnail(url='attachment://quartertails.png')
                a = await ctx.send(embed=embed1, file=file)
                await asyncio.sleep(20)
                await a.delete()

            elif num == 1 and side.lower() == "tails":

                with open('./users.json', 'r', encoding='utf-8-sig') as p:
                    data = json.load(p)
                
                data["users"][str(ctx.author.name)]["bank"] -= amount

                new_bal = data["users"][str(ctx.author.name)]["bank"]

                with open('./users.json', 'w', encoding='utf-8-sig') as file:
                    data = json.dump(data, file, indent=4)

                embed1 = discord.Embed(color=random.randint(0, 0xFFFFFF), timestamp=self.time, title=f"You Flipped {side.lower()}, and Lost!", description=f"__Name:__ {ctx.author.name}\n__Bet:__ {amount}\n__Won/Lost:__ Lost\n__Previous Balance:__ {balance}\n__New Balance:__ {new_bal}", inline=False)

                file = discord.File('/root/discord_bots/ButtlerBot/BBotV0.4.0/bot_images/quartertails.png', filename='quartertails.png')
                embed1.set_thumbnail(url='attachment://quartertails.png')
                a = await ctx.send(embed=embed1, file=file)
                await asyncio.sleep(20)
                await a.delete()

            else:

                a = await ctx.send(f"{ctx.author.name}, that is not a valid option. Please Try Again!")
                await asyncio.sleep(10)
                await a.delete()

        else:
            
            a = await ctx.send(f"{ctx.author.name}, you do not have enough money in the bank to cover that transaction. Your balance is {balance}")
            await asyncio.sleep(10)
            await a.delete()

def setup(bot):
    bot.add_cog(CP(bot))