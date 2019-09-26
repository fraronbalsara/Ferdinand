import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import User
import time
import os

#Ferdinand
Client = discord.Client()
client = commands.Bot(command_prefix = '.')
client.remove_command("help")

@client.event
async def on_ready():
    a = len(client.guilds)
    await client.change_presence(activity=discord.Game(name="on %d servers"%(a)))
    print('Bot is online and ready to use.')

extensions=['miscellaneous','score','currency','giveaway','clashroyale','translate','casino','moderation','exception_handling']
if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension("cogs."+extension)
            print(extension," was loaded")
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension,error))
    client.run(str(os.environ.get('BOT_TOKEN')))
    
#Destiny
bot = discord.Client()
bot = commands.Bot(command_prefix = '.')
bot.remove_command("help")

@client.event
async def on_ready():
    print('Destiny has been initialised and is ready.')
    channel = bot.get_channel(624434158642659329)
    await channel.send("Destiny has been initialised and is ready.")

extensions=['read']
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension("extensions."+extension)
            print(extension," was loaded")
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension,error))
    bot.run("NjI0NDQ3MTEzNTc2NTc5MTEz.XYRWOA.L2gRBkdLR8Tc9biJeoulpnxxJ9o", bot = False)

