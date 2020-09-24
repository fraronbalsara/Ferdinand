import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import User
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = '.')
client.remove_command("help")

@client.event
async def on_ready():
    a = len(client.guilds)
    await client.change_presence(activity=discord.Game(name="on %d servers"%(a)))
    print('Bot is online and ready to use.')

extensions=['miscellaneous','score','currency','giveaway','alerts','translate','casino','moderation','exception_handling']
if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension("cogs."+extension)
            print(extension," was loaded")
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension,error))
    client.run(str(os.environ('BOT_TOKEN')))
