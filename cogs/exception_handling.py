import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

class exception_handling(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.BadArgument):
            return await ctx.send("Invalid Argument.")
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send("Required argument missing, use help command.")

def setup(client):
    client.add_cog(exception_handling(client))
