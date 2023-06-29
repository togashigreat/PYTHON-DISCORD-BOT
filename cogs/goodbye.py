import discord
import random
from picEditor import edits
from discord.ext import commands
from discord import File
import json
from bot import MyBot
class Goodbye(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot
        with open("servers.json", "r") as f:
            self.servers = json.load(f)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        #taking server welcome/goodbye  channel_id to send the message
        server_id = str(member.guild.id)
        if server_id not in self.servers:
            return

        channel_id = self.servers[server_id]["goodbye_channel_id"]
        if channel_id is None:
            return
        
        channel = await self.bot.fetch_channel(channel_id)
            
        background_images = ["pic1.jpg", "pic2.jpg", "pic3.jpg"] # replace these with your own image filenames
        
        background_image_filename = random.choice(background_images)
        #the text to br showm on good bye image
        text = f"Good Bye, {member.name}"
        #edits function returns a file 
        file = await edits(member, background_image_filename, text)
        
        embed = discord.Embed(colour=(discord.Colour.random()), description=f"**{member.mention}, Hope we will see you here again^^**")

        embed.set_image(url="attachment://hking.jpg")
        #await channel.send(f"Good Bye {member.mention}!  \n **Hope We will see you here again^^**")
        await channel.send(file=file, embed=embed)
        
async def setup(bot):
    await bot.add_cog(Goodbye(bot))
