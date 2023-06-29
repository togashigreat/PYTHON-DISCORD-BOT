import discord
from discord.ext import commands
from discord import  app_commands
from bot import MyBot

class Moderation(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot
        
     #kicking member command
    @app_commands.command(
    name="kick",
    description="Kick a member from the server"   
    )
    @app_commands.describe(
    member="select a member to kick",
    reason="reason for kicking"
    )
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction, member: discord.Member, reason: str =None):
    	if not reason:
    		reason = "no reason"
    	try:
    		await member.kick(reason=reason)
    	except:
    		await interaction.response.send_message(f"Sorry, I'm not able to kick {member} from the server")
    	else:
    		await interaction.response.send_message(f'{member.name}#{member.discriminator} has been kicked from the server for {reason}')
    		
    		
    #unbanning memebers command
    
    @app_commands.command(
    name="unban",
    description="Unban a member"
    )
    @app_commands.describe(
    member="The member you want to unban",
    reason="reason for unbanning"
    )
    @app_commands.checks.has_permissions(ban_members=True)
    async def unban(self, interaction, member: discord.Member, reason: str =None):
        if not reason:
        	reason = "Be careful next time"
        try:
        	await member.unban(reason=reason)
        except:
        	await interaction.response.send_message(f"Sorry, I'm not able to unban {member}")
        else:
        	await interaction.response.send_message(f'{member.name} has been unbanned for {reason}')
     #ban members
    @app_commands.command(
    name="ban",
    description="Ban a member from the server"
    )
    @app_commands.describe(
    member="The member you want to ban",
    reason="reason for banning"
    )
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction, member: discord.Member, reason: str =None):
        if not reason:
        	reason = "no reason"
        try:
        	await member.ban(reason=reason)
        except:
        	await interaction.response.send_message(f"Sorry, I'm not able to ban {member} from the server")
        else:
        	await interaction.response.send_message(f'{member.name} has been banned for {reason}')

async def setup(bot):
	await bot.add_cog(Moderation(bot))
