import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

class score(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            a=message.author.id
            a1=message.guild.id
            con = psycopg2.connect(DATABASE_URL, sslmode='require')
            cur = con.cursor()
            query="select score from server_score where user_id=%d and server_id=%d"%(a,a1)
            cur.execute(query)
            b = cur.fetchone()
            if(b is not None):
                c = b[0] + 0.1
                query1="update server_score set score=%f where user_id=%d and server_id=%d"%(float(c),a,a1)
                cur.execute(query1)
                con.commit()
                con.close()
            else:
                d=0.1
                query2="insert into server_score values(%d,%d,%f)"%(a,a1,d)
                cur.execute(query2)
                con.commit()
                con.close()
        except:
            None

    @commands.command()
    @commands.guild_only()
    async def score(self, ctx, user: discord.Member=None):
        try:
            if(user):
                a=user.id
            else:
                a=ctx.message.author.id
            a1=ctx.message.guild.id
            a2=ctx.message.guild
            a3=ctx.message.author.id
            con = psycopg2.connect(DATABASE_URL, sslmode='require')
            cur = con.cursor()
            query="select score from server_score where user_id=%d and server_id=%d"%(a,a1)
            cur.execute(query)
            b = cur.fetchone()
            await ctx.message.channel.send("Current score for <@%d> in %s: %d <@%d>"%(a,a2,b[0],a3))
            con.close()
        except Exception as ve:
            print(ve)
            await ctx.message.channel.send("Account doesn't exist.")


def setup(client):
    client.add_cog(score(client))
