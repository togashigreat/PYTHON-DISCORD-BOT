import discord
from discord.ext import commands
from discord import utils
from servers import save_servers
from colorama import Fore, Style, Back
from keep_live import keep_alive
class MyBot(commands.Bot):
    def __init__(self, command_prefix: str, intents: discord.Intents, **kwargs):
        super().__init__(command_prefix, intents=intents, **kwargs)

    async def on_ready(self):
        await self.change_presence(status=discord.Status.idle, activity=discord.Game(name="with Yuuta"))
        
        #styling console on LOGGING

        yume = Fore.BLUE + "\033[1m[ Rikka ] ->\033[0m" + Style.RESET_ALL
        print(f" {yume} {Fore.GREEN}{Style.BRIGHT} Loading commands......{Style.RESET_ALL}")
        
        # saving servers ID to send welcome & goodbye messages [cogs/welcome.py & cogs/goodbye.py] 
        await save_servers(bot)
        
        # loading the commands
        cog_list = ['cogs.hello_cog', 'cogs.say', 'cogs.gpt', 'cogs.welcome', 'cogs.goodbye', 'cogs.ban', 'cogs.action', 'cogs.mu']

        for cog in cog_list:
            try:
                cog_name = cog.split('.')[-1]
                await bot.load_extension(cog)
                print(f" {yume}{Style.BRIGHT}{Fore.CYAN} Successfully installed module {cog_name}{Style.RESET_ALL}")

            except Exception as e:
                print(f" {yume} {Fore.RED} Error loading cog: {cog} - {e}{Style.RESET_ALL}")
        
        #syncing the commands
        await bot.tree.sync()

        #styling console on Ready 
        print(f" {yume} {Fore.GREEN} {Style.BRIGHT}Cogs loaded Successfully")
        print(f" {yume} {Fore.CYAN} {Style.BRIGHT}Commands are loaded Successfully!{Style.RESET_ALL}")
        print(f" {yume} {Back.RED}{Fore.WHITE}{Style.BRIGHT} Rikka is Ready{Style.RESET_ALL}")
        keep_alive()
if __name__ == '__main__':
    #prefix fo4 commands
    bot = MyBot(command_prefix='!', intents=discord.Intents.all())
    TOKEN = "YOUR TOKEN"
    bot.run(TOKEN)
