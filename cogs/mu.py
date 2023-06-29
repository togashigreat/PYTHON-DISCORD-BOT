import discord
import youtube_dl
from discord.ext import commands
from bot import MyBot

class Music(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, query):
        voice_channel = ctx.author.voice.channel
        if not voice_channel:
            await ctx.send("You are not connected to a voice channel.")
            return

        # Create a YoutubeDL instance
        ydl_opts = {
            'format': 'bestaudio/best'
        }
        ydl = youtube_dl.YoutubeDL(ydl_opts)

        # Search and extract information about the videos
        try:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        except Exception as e:
            await ctx.send("An error occurred while searching for the song.")
            print(e)
            return

        # Get the video URL and title
        url = info['formats'][0]['url']
        title = info['title']

        # Connect to the voice channel
        voice_client = await voice_channel.connect()

        # Create an embedded message for the song
        embed = discord.Embed(title="Now Playing", description=f"**{title}**", color=discord.Color.green())
        embed.set_thumbnail(url=info['thumbnail'])
        embed.add_field(name="Author", value=info['uploader'], inline=True)
        embed.add_field(name="Duration", value=info['duration'], inline=True)
        embed.add_field(name="URL", value=f"[Click Here]({url})")

        # Send the embedded message
        message = await ctx.send(embed=embed)

        # Play the song using FFmpeg
        voice_client.play(discord.FFmpegPCMAudio(url))

        # Add reactions for controlling the music
        await message.add_reaction("⏸️")
        await message.add_reaction("⏹️")
        await message.add_reaction("▶️")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user == self.bot.user:
            return

        if reaction.emoji == "⏸️":
            if reaction.message.guild.voice_client.is_playing():
                reaction.message.guild.voice_client.pause()
                await reaction.message.channel.send("Playback paused.")
        elif reaction.emoji == "⏹️":
            if reaction.message.guild.voice_client.is_playing():
                reaction.message.guild.voice_client.stop()
                await reaction.message.channel.send("Playback stopped.")
        elif reaction.emoji == "▶️":
            if reaction.message.guild.voice_client.is_paused():
                reaction.message.guild.voice_client.resume()
                await reaction.message.channel.send("Playback resumed.")

async def setup(bot):
    await bot.add_cog(Music(bot))

