import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

class miscellaneous(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        a=message.author.id
        if(message.content=="cookie" or message.content=="Cookie"):
            await channel.send(":cookie: <@%d>"%(a))

    @commands.command()
    async def ping(self,ctx):
        await ctx.send('Pong :ping_pong:')

    @commands.command()
    async def toss(self,ctx):
        flip = random.randint(1,2)
        if(flip==1):
            await ctx.send('Heads')
        else:
            await ctx.send('Tails')

    @commands.command()
    async def help(self, ctx):
        author = ctx.message.author.id
        embed_help = discord.Embed(
            title="```Help- Commands list for Ferdinand.```",
            colour=discord.Colour.green()
        )
        embed_help.add_field(name='.ping', value='Returns Pong :ping_pong:', inline=True)
        embed_help.add_field(name='.toss', value='Returns the value of a random coin toss. Either __heads__ or __tails__', inline=True)
        embed_help.add_field(name='.score', value='Returns the current score of the user in the server.', inline=True)
        await ctx.send(embed = embed_help)

    @commands.command()
    async def crystal_ball(self, ctx, *que):
        if(que[len(que) - 1].endswith("?")):
            a = ctx.message.author.id
            b = "<@%d>"%(a)
            await ctx.send(random.choice(['It is certain. :crystal_ball: '+b,'Without a doubt. :crystal_ball: '+b,'You may rely on it. :crystal_ball: '+b,'Yes definitely. :crystal_ball: '+b,'It is decidedly so. :crystal_ball: '+b,'As I see it. :crystal_ball: '+b,'Yes. :crystal_ball: '+b,'Most likely. :crystal_ball: '+b,'Outlook good.:crystal_ball: '+b,'Signs point to yes. :crystal_ball: '+b,'Reply hazy try again. :crystal_ball: '+b,'Better not tell you now. :crystal_ball: '+b,'Ask again later. :crystal_ball: '+b,'Cannot predict now. :crystal_ball: '+b,'Concentrate and ask again. :crystal_ball: '+b,'Don’t count on it. :crystal_ball: '+b,'Outlook not so good. :crystal_ball: '+b,'My sources say no. :crystal_ball: '+b,'Very doubtful. :crystal_ball: '+b,'My reply is no. :crystal_ball: '+b]))
        else:
            await ctx.send("Question should end with a '?' symbol.")

    @commands.command()
    async def dice(self, ctx):
        author = ctx.message.author.id
        roll = random.randint(1,6)
        if(roll == 1):
            await ctx.send("<:1_:593094094150959117>")
        elif(roll == 2):
            await ctx.send("<:2_:593094106289537035>")
        elif(roll == 3):
            await ctx.send("<:3_:593094125197197312>")
        elif(roll == 4):
            await ctx.send("<:4_:593094152191868934>")
        elif(roll == 5):
            await ctx.send("<:5_:593094162648137778>")
        elif(roll == 6):
            await ctx.send("<:6_:593094183527645204>")

    @commands.command()
    async def twoDice(self, ctx):
        author = ctx.message.author.id
        roll = random.randint(1,6)
        roll2 = random.randint(1,6)
        mes = ""
        if(roll == 1):
            mes = mes + "<:1_:593094094150959117>"
        elif(roll == 2):
            mes = mes + "<:2_:593094106289537035>"
        elif(roll == 3):
            mes = mes + "<:3_:593094125197197312>"
        elif(roll == 4):
            mes = mes + "<:4_:593094152191868934>"
        elif(roll == 5):
            mes = mes + "<:5_:593094162648137778>"
        elif(roll == 6):
            mes = mes + "<:6_:593094183527645204>"
        if(roll2 == 1):
            mes = mes + "<:1_:593094094150959117>"
        elif(roll2 == 2):
            mes = mes + "<:2_:593094106289537035>"
        elif(roll2 == 3):
            mes = mes + "<:3_:593094125197197312>"
        elif(roll2 == 4):
            mes = mes + "<:4_:593094152191868934>"
        elif(roll2 == 5):
            mes = mes + "<:5_:593094162648137778>"
        elif(roll2 == 6):
            mes = mes + "<:6_:593094183527645204>"
        await ctx.send(mes)

def setup(client):
    client.add_cog(miscellaneous(client))
