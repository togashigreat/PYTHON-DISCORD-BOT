import discord
from discord.ext import commands
from discord import app_commands
import openai
from asyncio import sleep

from bot import MyBot
class ChatGpt(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot
    openai.api_key = "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"

    @app_commands.command(name="chatgptt", description="Ask ChatGPT3")
    async def gpt(self, interaction: discord.Interaction, question: str):
        await interaction.response.defer()
        response = openai.Completion.create(
                model="text-davinci-003",
                prompt=question,
                temperature=0.3,
                max_tokens=4000,
                top_p=1,
                frequency_penalty=1,
                presence_penalty=1,
                stop=[" Human:", " AI:"]
               )
        text = response['choices'][0]['text']
        await sleep(4)
        await interaction.followup.send(f" {text}")
        
async def setup(bot):
        await bot.add_cog(ChatGpt(bot))
