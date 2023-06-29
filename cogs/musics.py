from re import VERBOSE
import discord
from discord.ext import commands
import youtube_dl
from bot import MyBot

class Music(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, url):
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("You need to be in a voice channel to play music.")
            return
        else:
            await voice_channel.connect()

        guild = ctx.guild
        ydl_opts = {'format': 'bestaudio', 'verbose': True}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
            if not guild.voice_client.is_playing():
                guild.voice_client.play(discord.FFmpegPCMAudio(URL), after=None)
                await ctx.send(f'Playing: {info["title"]}')

async def setup(bot):
    await bot.add_cog(Music(bot))

