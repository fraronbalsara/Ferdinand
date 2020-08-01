import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

class alerts(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        server = guild.id
        owner = guild.owner.id
        con = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = con.cursor()
        query="insert into ferdinand_server_list values(%d,%d)"%(server,owner)
        cur.execute(query)
        con.commit()
        con.close()
        a = len(self.client.guilds)
        await self.client.change_presence(activity=discord.Game(name=" on %d servers"%(a)))

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        server = guild.id
        con = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = con.cursor()
        query="delete from ferdinand_server_list where server_id = %d"%(server)
        cur.execute(query)
        con.commit()
        con.close()
        a = len(self.client.guilds)
        await self.client.change_presence(activity=discord.Game(name=" on %d servers"%(a)))

def setup(client):
    client.add_cog(alerts(client))
