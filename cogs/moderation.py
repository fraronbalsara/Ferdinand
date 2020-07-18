import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from profanity import profanity
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

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
                await ctx.send(":warning:%s was kicked by %s for %s."%(user, author, reason))
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
                await ctx.send(":warning:%s was banned by %s for %s."%(user, author, reason))
                await user.send("You were banned from %s by %s for %s."%(server, author, reason))
            else:
                await ctx.send("Cannot ban users with moderator permissions.")
        except discord.Forbidden:
            await ctx.send("Ban Members permission required")
        except Exception as ve:
            print(ve)
            await ctx.send("Unknown error occured.")

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def mute(self, ctx, user: discord.Member = None, time = None, reason = None):
        try:
            author  = ctx.message.author
            server = ctx.message.guild
            try:
                time = int(time)
            except:
                reason = time
                time = None
            if not user:
                return await ctx.send("You must specify a user.")
            if(str(user) == 'Ferdinand#5990'):
                return await ctx.send("I cannot mute myself.")
            if(user == author):
                return await ctx.send("You cannot mute yourself.")
            if(user == ctx.message.guild.owner):
                return await ctx.send("You cannot mute the server owner.")
            if reason is None:
                reason = "unspecified reasons"
            if time is None:
                reason = reason + " " + "indefinitely"
            else:
                reason = reason + " " + "for " + str(time) + " minutes"
            if(user.guild_permissions.kick_members == False):
                q = ""
                existing_roles = ctx.message.guild.roles
                for r in existing_roles:
                    if(r.name == "muted"):
                        q = 1
                        break
                    else:
                        q = 0
                if(q == 0):
                    muted = await server.create_role(name="muted")
                    for channel in ctx.guild.channels:
                        await channel.set_permissions(muted, send_messages=False, add_reactions=False, speak=False)
                Role = discord.utils.get(user.guild.roles, name="muted")
                await user.add_roles(Role)
                await ctx.send(":warning:%s was muted by %s for %s."%(user, author, reason))
                await user.send("You were muted from %s by %s for %s."%(server, author, reason))
                if not time:
                    return
                else:
                    await asyncio.sleep(time*60)
                    await user.remove_roles(Role)
                    await ctx.send(":warning:%s was unmuted cause timer ran out."%(user))
            else:
                await ctx.send("Cannot mute users with moderator permissions.")
        except discord.Forbidden:
            await ctx.send("Missing Permission")
        except Exception as ve:
            print(ve)
            await ctx.send("Unknown error occured.")

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def unmute(self, ctx, user: discord.Member = None):
        try:
            author  = ctx.message.author
            if not user:
                return await ctx.send("You must specify a user.")
            if(str(user) == 'Ferdinand#5990'):
                return await ctx.send("Error! Try someone other than me.")
            if(user == author):
                return await ctx.send("Error! Try someone other than yourself.")
            if(user == ctx.message.guild.owner):
                return await ctx.send("Error! Try someone else, that's the server owner.")
            Roles = user.roles
            mute = False
            for r in Roles:
                if(r.name == "muted"):
                    Role = discord.utils.get(user.guild.roles, name="muted")
                    await user.remove_roles(Role)
                    await ctx.send(":warning:%s was unmuted."%(user))
                    mute = True
            if(mute == False):
                await ctx.send("%s cannot be unmuted since he isn't muted."%(user))
        except discord.Forbidden:
            await ctx.send("Missing Permission")
        except Exception as ve:
            print(ve)
            await ctx.send("Unknown error occured.")

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def profanity_filter_on(self, ctx):
        server = ctx.message.guild.id
        con = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = con.cursor()
        query="select * from profanity where server_id=%d"%(server)
        cur.execute(query)
        b = cur.fetchone()
        if(b == None):
            query="insert into profanity values(%d)"%(server)
            cur.execute(query)
            con.commit()
            con.close()
            await ctx.send("Profanity filter has been turned on.")
        else:
            con.close()
            await ctx.send("Profanity filter is already turned on.")

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def profanity_filter_off(self, ctx):
        server = ctx.message.guild.id
        con = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = con.cursor()
        query="select * from profanity where server_id=%d"%(server)
        cur.execute(query)
        b = cur.fetchone()
        if(b != None):
            query2="delete from profanity where server_id = %d"%(server)
            cur.execute(query2)
            con.commit()
            con.close()
            await ctx.send("Profanity filter has been turned off.")
        else:
            con.close()
            await ctx.send("Profanity filter is already turned off.")

    @commands.Cog.listener()
    async def on_message(self, message):
        server = message.guild.id
        con = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = con.cursor()
        query="select * from profanity where server_id=%d"%(server)
        cur.execute(query)
        b = cur.fetchone()
        con.close()
        if((profanity.contains_profanity(message.content) == True) and message.guild.owner != message.author and b != None):
            await message.delete()
            await message.channel.send(":warning:Warning! Watch your language <@%d>."%(message.author.id))

def setup(client):
    client.add_cog(moderation(client))
