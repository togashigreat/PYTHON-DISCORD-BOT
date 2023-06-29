# cogs/hello_cog.py
import discord
from discord.ext import commands
from bot import MyBot
class HelloCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello, world!')
        

async def setup(bot):
    await bot.add_cog(HelloCog(bot))
