import discord
from discord import app_commands
from discord.embeds import Embed
from bot import MyBot
import requests
from discord import colour
from discord.ext import commands

class action(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="kicking", description="break bones")
    @app_commands.describe(member="mention the bastard")
    async def kicking(self, interaction: discord.Interaction, member: discord.Member):
        kick_gif = "https://apiservice1.kisara.app/satou//api/endpoint/kick"
        response = requests.get(kick_gif)
        if response.status_code == 200:
            data = response.json()
            urls = data["url"]
        else:
            print("Error:", response.status_code)

        embed = discord.Embed(
            colour=(discord.Colour.random()),
            description=f"{member.mention}, here take this you bobo! \n***{interaction.user.name} kicks {member.name}***"
        )
        embed.set_image(url=urls)
        await interaction.response.send_message(embed=embed)

    # slap command
    @app_commands.command(name="slap", description="slap a person")
    @app_commands.describe(member="the person to slap")
    async def slap(self, interaction: discord.Interaction, member: discord.Member):
        slap_gif = "https://apiservice1.kisara.app/satou//api/endpoint/slap"
        response = requests.get(slap_gif)
        if response.status_code == 200:
            data = response.json()
            urls = data["url"]
        else:
            print("Error:", response.status_code)
        embed = discord.Embed(
            colour=(discord.Colour.random()),
            description=f"{member.mention}, You dirty human take this!\n***{interaction.user.name} slaps {member.name}***"
        )
        embed.set_image(url=urls)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="pat", description="pat someone")
    @app_commands.describe(member="the person you want to pat")
    async def pat(self, interaction: discord.Interaction, member: discord.Member):
        pat_gif = "https://apiservice1.kisara.app/satou//api/endpoint/pat"
        response = requests.get(pat_gif)
        if response.status_code == 200:
            data = response.json()
            urls = data["url"]
        else:
            print("Error:", response.status_code)
        embed = discord.Embed(
            colour=(discord.Colour.random()),
            description=f"{member.mention}, Yosh Yosh ^^ \n*{interaction.user.name} pats {member.name}*"
        )
        embed.set_image(url=urls)
        await interaction.response.send_message(embed=embed)
        
     # kiss command
    @app_commands.command(name="kiss", description="kiss a person")
    @app_commands.describe(member="the person to kiss")
    async def kiss(self, interaction: discord.Interaction, member: discord.Member):
        kiss_gif = "https://apiservice1.kisara.app/satou//api/endpoint/kiss"
        response = requests.get(kiss_gif)
        if response.status_code == 200:
            data = response.json()
            urls = data["url"]
        else:
            print("Error:", response.status_code)
        embed = discord.Embed(
            colour=(discord.Colour.random()),
            description=f"{member.mention}, I love you \n***{interaction.user.name} kisses {member.name}***"
        )
        embed.set_image(url=urls)
        await interaction.response.send_message(embed=embed)        


    # a command for hugging a person
    @app_commands.command(name="hug", description="hug a person")
    @app_commands.describe(member="the person to hug")
    async def hugs(self, interaction: discord.Interaction, member: discord.Member):
        hug_gif = "https://apiservice1.kisara.app/satou//api/endpoint/hug"

        response = requests.get(hug_gif)
        if response.status_code == 200:
            data = response.json()
            urls = data["url"]
        else:
            print("Error:", response.status_code)
        embed = discord.Embed(
            colour=(discord.Colour.random()),
            description=f"{member.mention}, poor hoomans here take a hug \n***{interaction.user.name} hugs {member.name}***"
        )
        embed.set_image(url=urls)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
	await bot.add_cog(action(bot))
