import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from mysql.connector import *
import random
import youtube_dl
from discord import User
import logging
import time

Client = discord.Client()
client = commands.Bot(command_prefix = '.')
client.remove_command("help")

@client.event
async def on_ready():
    a = len(client.guilds)
    await client.change_presence(activity=discord.Game(name="on %d servers"%(a)))
    print('Bot is online and ready to use.')

client.run(str(os.environ.get('BOT_TOKEN')))
