import discord
from discord.ext import commands
from discord import app_commands
from bot import MyBot
class say(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot
        
    @app_commands.command(description="repeats after")    
    async def say(self, interaction, message: str):
    	await interaction.response.send_message(message)
    	
async def setup(bot):
    await bot.add_cog(say(bot))
