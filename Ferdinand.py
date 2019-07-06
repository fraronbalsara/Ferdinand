import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import User
import time

Client = discord.Client()
client = commands.Bot(command_prefix = '.')
client.remove_command("help")

@client.event
async def on_ready():
    a = len(client.guilds)
    await client.change_presence(activity=discord.Game(name="on %d servers"%(a)))
    print('Bot is online and ready to use.')

client.run("NTUxMzI2NjI5NzI5OTI3MTg4.D2FEwQ.Gzh06ETEs4CJEMTlHytoNgo1J9s")
