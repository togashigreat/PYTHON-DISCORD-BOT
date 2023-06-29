import json
import discord

async def save_servers(bot):
    servers = {}
    for guild in bot.guilds:
        server_id = str(guild.id)
        servers[server_id] = {}
        for channel in guild.channels:
            if channel.name == "♧welcome♧":
                servers[server_id]["welcome_channel_id"] = str(channel.id)
            elif channel.name == "♧good-bye♧":
                servers[server_id]["goodbye_channel_id"] = str(channel.id)
    with open("servers.json", "w") as f:
        json.dump(servers, f, indent=4)
