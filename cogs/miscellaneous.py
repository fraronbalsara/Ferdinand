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
        
    @commands.command()
    async def help(self, ctx):
        author = ctx.message.author
        embed_help = discord.Embed(
            title="```Help- Commands list for Ferdinand.```",
            colour=discord.Colour.blue()
        )
        embed_help.add_field(name='.ping', value='Returns Pong :ping_pong:', inline=False)
        embed_help.add_field(name='.toss', value='Returns the value of a random coin toss. Either __heads__ or __tails__', inline=False)
        embed_help.add_field(name='.dice', value='Returns the value of a random dice roll.', inline=False)
        embed_help.add_field(name='.twoDice', value='Returns the value of two random dice rolls.', inline=True)
        embed_help.add_field(name='.crytsal_ball <question>', value='Returns an answer to the question.', inline=True)
        embed_help.add_field(name='.translate <text>', value='Returns given text translated in English.', inline=True)
        embed_help.add_field(name='.translateTo <ISO 639-1 language code> <text>', value='Returns given text translated in the language of mentioned ISO 639-1 code.', inline=True)
        embed_help.add_field(name='.score <tag discord user>(optional)', value='Returns the current score of the user in the server or the current score of the mentioned user in the server.', inline=True)
        embed_help.add_field(name ='.create_account', value='Creates an acount and assigns you a daily bonus.', inline=True)
        embed_help.add_field(name ='.daily', value='To collect your daily bonus. Available once every 24 hours', inline=True)
        embed_help.add_field(name ='.balance <tag discord user>(optional)', value='To check your account balance or the account balance of mentioned user', inline=True)
        embed_help.add_field(name=".transfer <tag discord user> <amount>", value="Transfers given cash from your account to mention user's account.", inline=True)
        embed_help.add_field(name='.giveaway_help', value='Help for giveaway related commands. These commands can only be used by those with manage roles permission in the server.', inline=True)
        embed_help.add_field(name='.moderation_help', value='Help for moderation related commands. This command can only be used by those with manage roles permission in the server.', inline=True)
        await author.send(embed = embed_help)

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def giveaway_help(self, ctx):
        author = ctx.message.author
        embed_help = discord.Embed(
            title="```Giveaway Help- Commands list for Ferdinand.```",
            colour=discord.Colour.blue()
        )
        embed_help.add_field(name='.regular_giveaway_start <time: in minutes>', value='Starts a regular giveaway where users react to bot post and a random winner is chosen after given time.', inline=True)
        embed_help.add_field(name='.qa_giveaway_start <time: in minutes> <answer> <question>', value="Starts a question-answer giveaway where the bot allows users to join the giveaway session until mentioned time, following which it opens the channel to the registered users and let's them answer the question. Bot automatically reads all answers and picks the correct one and announces the winner.", inline=True)
        await author.send(embed = embed_help)

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def moderation_help(self, ctx):
        author = ctx.message.author
        embed_help = discord.Embed(
            title="```Moderation Help- Commands list for Ferdinand.```",
            colour=discord.Colour.blue()
        )
        embed_help.add_field(name='.kick <tag discord user> <reason>(optional)', value='To kick a user with optional argument reason.', inline=True)
        embed_help.add_field(name='.ban <tag discord user> <reason>(optional)', value='To ban a user with optional argument reason.', inline=True)
        embed_help.add_field(name='.mute <tag discord user> <time>(optional) <reason>(optional)', value='To mute a user with optional argument reason and specified time.', inline=True)
        embed_help.add_field(name='.unmute <tag discord user> <reason>(optional)', value='To unmute a user.', inline=True)
        await author.send(embed = embed_help)

def setup(client):
    client.add_cog(miscellaneous(client))
