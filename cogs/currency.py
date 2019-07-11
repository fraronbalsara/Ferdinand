import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import datetime
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

class currency(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def create_account(self, ctx):
        try:
            a=ctx.message.author.id
            e = datetime.datetime.now().strftime("%d-%m-%y")
            con = psycopg2.connect(DATABASE_URL, sslmode='require')
            cur = con.cursor()
            query="select * from discord_currency where user_id=%d"%(a)
            cur.execute(query)
            b=cur.fetchone()
            if(b != None):
                await ctx.message.channel.send("Account already exists.")
                con.close()
            else:
                a1 = 100
                query1="insert into discord_currency values(%d,%d)"%(a,a1)
                cur.execute(query1)
                query2 = "insert into currency_daily values(%d,'%s')"%(a,e)
                cur.execute(query2)
                con.commit()
                con.close()
                await ctx.message.channel.send("Account created and $100 credited as a bonus.")
        except Exception as ve:
            print(ve)
            await ctx.send("Unknown Error.")

    @commands.command()
    async def balance(self, ctx, user: discord.Member=None):
        try:
            if(user):
                a=user.id
            else:
                a=ctx.message.author.id
            a1=ctx.message.author.id
            con = psycopg2.connect(DATABASE_URL, sslmode='require')
            cur = con.cursor()
            query = "select * from discord_currency where user_id=%d"%(a)
            cur.execute(query)
            b = cur.fetchone()
            con.close()
            await ctx.message.channel.send("Current balance for <@%d> is $%d. <@%d>"%(a,b[1],a1))
        except Exception as ve:
            print(ve)
            await ctx.message.channel.send("Account doesn't exist.")

    @commands.command()
    async def daily(self, ctx):
        try:
            a = ctx.message.author.id
            b = datetime.datetime.now().strftime("%d-%m-%y")
            time = datetime.datetime.now()
            hours = 24 - time.hour
            mins = 60 - time.minute
            con = psycopg2.connect(DATABASE_URL, sslmode='require')
            cur = con.cursor()
            query = "select * from currency_daily where user_id=%d"%(a)
            cur.execute(query)
            c = cur.fetchone()
            if(c[1] != b):
                query1 = "select * from discord_currency where user_id=%d"%(a)
                cur.execute(query1)
                d = cur.fetchone()
                new_balance = d[1] + 100
                query2="update discord_currency set cash=%d where user_id=%d"%(new_balance,a)
                cur.execute(query2)
                query3 = "update currency_daily set date='%s' where user_id=%d"%(b,a)
                cur.execute(query3)
                con.commit()
                con.close()
                await ctx.message.channel.send("You received your daily cash of $100 <@%d>."%(a))
            else:
                con.close()
                await ctx.message.channel.send("You already collected your daily today. Next in %d hours and %d minutes <@%d>."%(hours,mins,a))
        except Exception as ve:
            print(ve)
            await ctx.message.channel.send("Account doesn't exist.")

    @commands.command()
    async def transfer(self, ctx, user: discord.Member, amount: int):
        try:
            a=user.id
            a1=ctx.message.author.id
            con = psycopg2.connect(DATABASE_URL, sslmode='require')
            cur = con.cursor()
            query = "select * from discord_currency where user_id=%d"%(a1)
            cur.execute(query)
            b1 = cur.fetchone()
            if(b1[1] >= amount):
                query1 = "select * from discord_currency where user_id=%d"%(a)
                cur.execute(query1)
                b = cur.fetchone()
                new_balance = b[1] + amount
                new_balance1 = b1[1] - amount
                query2="update discord_currency set cash=%d where user_id=%d"%(new_balance,a)
                cur.execute(query2)
                query3="update discord_currency set cash=%d where user_id=%d"%(new_balance1,a1)
                cur.execute(query3)
                con.commit()
                con.close()
                await ctx.message.channel.send("Transfer Successful.")
            else:
                await ctx.message.channel.send("Insufficient balance.")
        except Exception as ve:
            print(ve)
            await ctx.message.channel.send("Account doesn't exist.")


def setup(client):
    client.add_cog(currency(client))
