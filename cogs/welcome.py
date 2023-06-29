import discord
from discord import File
import random
from picEditor import edits
from discord import utils
from discord.ext import commands
from discord.embeds import Embed
import json
from bot import MyBot
class Welcome(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot
        with open("servers.json", "r") as f:
            self.servers = json.load(f)
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        server_id = str(member.guild.id)
        if server_id not in self.servers:
            return

        channel_id = self.servers[server_id]["welcome_channel_id"]
        if channel_id is None:
            return
       
        channel = await self.bot.fetch_channel(channel_id)
        rules_channel = discord.utils.get(member.guild.channels, name="rules")
        background_images = ["pic1.jpg", "pic2.jpg", "pic3.jpg"]
        background_image_filename = random.choice(background_images)
        text = f"Welcome to the {member.guild.name} server"

        #edit function returns a "file" including discord.File
        file = await edits(member, background_image_filename, text)
        #embeding welcome message for sendingg 

        embed = discord.Embed(colour=(discord.Colour.random()), description=f"**{member.mention}, welcome to the {member.guild} server\nplease read the rules & regulations in {rules_channel.mention}**")
        
        embed.set_image(url="attachment://hking.jpg")
        #await channel.send(f"Hello {member.mention}! Welcome to the **{member.guild.name} server, Have fun! \n♧Go to {rules_channel.mention}\nRead the Rules and guidelines.**")
        await channel.send(file=file, embed=embed)

async def setup(bot):
    await bot.add_cog(Welcome(bot))

