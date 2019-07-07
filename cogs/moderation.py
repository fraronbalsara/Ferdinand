import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.Member = None, reason = None):
        author  = ctx.message.author
        server = ctx.message.guild
        if not user:
            return await ctx.send("You must specify a user.")
        if(str(user) == 'Ferdinand#5990'):
            return await ctx.send("I cannot kick myself.")
        if(user == author):
            return await ctx.send("You cannot kick yourself.")
        if(user == ctx.message.guild.owner):
            return await ctx.send("You cannot kick the server owner.")
        if reason is None:
            reason = "unspecified reasons"
        try:
            if(user.guild_permissions.kick_members == False):
                await ctx.guild.kick(user)
                await ctx.send("%s was kicked for %s."%(user, reason))
                await user.send("You were kicked from %s by %s for %s."%(server, author, reason))
            else:
                await ctx.send("Cannot kick users with moderator permissions.")
        except discord.Forbidden:
            await ctx.send("Kick Members permission required")
        except Exception as ve:
            print(ve)
            await ctx.send("Unknown error occured.")

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Member = None, reason = None):
        author  = ctx.message.author
        server = ctx.message.guild
        if not user:
            return await ctx.send("You must specify a user.")
        if(str(user) == 'Ferdinand#5990'):
            return await ctx.send("I cannot ban myself.")
        if(user == author):
            return await ctx.send("You cannot ban yourself.")
        if(user == ctx.message.guild.owner):
            return await ctx.send("You cannot ban the server owner.")
        if reason is None:
            reason = "unspecified reasons"
        try:
            if(user.guild_permissions.kick_members == False):
                await ctx.guild.ban(user)
                await ctx.send("%s was banned for %s."%(user, reason))
                await user.send("You were banned from %s by %s for %s."%(server, author, reason))
            else:
                await ctx.send("Cannot ban users with moderator permissions.")
        except discord.Forbidden:
            await ctx.send("Ban Members permission required")
        except Exception as ve:
            print(ve)
            await ctx.send("Unknown error occured.")

    @commands.Cog.listener()
    async def on_message(self, message):
        mes = message.content.split(" ")
        profanity = ['fuck', 'Fuck', 'FUCK', 'fucking', 'Fucking', 'pussy', 'cunt', 'asshole', 'bitch', 'dick']
        for i in profanity:
            for j in mes:
                if i==j:
                    await message.delete()
                    return

def setup(client):
    client.add_cog(moderation(client))
