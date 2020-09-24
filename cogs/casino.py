import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import psycopg2
import random

DATABASE_URL = os.environ['DATABASE_URL']

blackjack_dict = {}
cards = ["A:hearts:","2:hearts:","3:hearts:","4:hearts:","5:hearts:","6:hearts:","7:hearts:","8:hearts:","9:hearts:","10:hearts:","J:hearts:","Q:hearts:","K:hearts:","A:diamonds:","2:diamonds:","3:diamonds:","4:diamonds:","5:diamonds:","6:diamonds:","7:diamonds:","8:diamonds:","9:diamonds:","10:diamonds:","J:diamonds:","Q:diamonds:","K:diamonds:","A:clubs:","2:clubs:","3:clubs:","4:clubs:","5:clubs:","6:clubs:","7:clubs:","8:clubs:","9:clubs:","10:clubs:","J:clubs:","Q:clubs:","K:clubs:","A:spades:","2:spades:","3:spades:","4:spades:","5:spades:","6:spades:","7:spades:","8:spades:","9:spades:","10:spades:","J:spades:","Q:spades:","K:spades:"]

class casino(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def slots(self, ctx, bet: int):
        try:
            if(bet >= 10):
                user = ctx.message.author.id
                con = psycopg2.connect(DATABASE_URL, sslmode='require')
                cur = con.cursor()
                query = "select * from discord_currency where user_id=%d"%(user)
                cur.execute(query)
                b = cur.fetchone()
                if(b[1] >= bet):
                    no1 = random.randint(1,9)
                    no2 = random.randint(1,9)
                    no3 = random.randint(1,9)
                    mes = ""
                    if(no1 == 1):
                        mes = mes + ":one:"
                    elif(no1 == 2):
                        mes = mes + ":two:"
                    elif(no1 == 3):
                        mes = mes + ":three:"
                    elif(no1 == 4):
                        mes = mes + ":four:"
                    elif(no1 == 5):
                        mes = mes + ":five:"
                    elif(no1 == 6):
                        mes = mes + ":six:"
                    elif(no1 == 7):
                        mes = mes + ":seven:"
                    elif(no1 == 8):
                        mes = mes + ":eight:"
                    elif(no1 == 9):
                        mes = mes + ":nine:"

                    if(no2 == 1):
                        mes = mes + ":one:"
                    elif(no2 == 2):
                        mes = mes + ":two:"
                    elif(no2 == 3):
                        mes = mes + ":three:"
                    elif(no2 == 4):
                        mes = mes + ":four:"
                    elif(no2 == 5):
                        mes = mes + ":five:"
                    elif(no2 == 6):
                        mes = mes + ":six:"
                    elif(no2 == 7):
                        mes = mes + ":seven:"
                    elif(no2 == 8):
                        mes = mes + ":eight:"
                    elif(no2 == 9):
                        mes = mes + ":nine:"

                    if(no3 == 1):
                        mes = mes + ":one:"
                    elif(no3 == 2):
                        mes = mes + ":two:"
                    elif(no3 == 3):
                        mes = mes + ":three:"
                    elif(no3 == 4):
                        mes = mes + ":four:"
                    elif(no3 == 5):
                        mes = mes + ":five:"
                    elif(no3 == 6):
                        mes = mes + ":six:"
                    elif(no3 == 7):
                        mes = mes + ":seven:"
                    elif(no3 == 8):
                        mes = mes + ":eight:"
                    elif(no3 == 9):
                        mes = mes + ":nine:"

                    await ctx.send(mes)

                    if (no1 == no2 == no3):
                        winnings = bet * 2
                        new_balance = b[1] + bet
                        query2="update discord_currency set cash=%d where user_id=%d"%(new_balance,user)
                        cur.execute(query2)
                        con.commit()
                        con.close()
                        await ctx.send("Congratulations! You won back $%d"%(winnings))
                    else:
                        new_balance = b[1] - bet
                        query2="update discord_currency set cash=%d where user_id=%d"%(new_balance,user)
                        cur.execute(query2)
                        con.commit()
                        con.close()
                        await ctx.send("Yikes! You lost $%d. Better luck next time."%(bet))
                else:
                    con.close()
                    await ctx.message.channel.send("Insufficient balance.")
            else:
                await ctx.message.channel.send("Bet cannot be less than $10.")
        except:
            await ctx.message.channel.send("Invalid argument, use help command for help on proper usage of this command.")

    @commands.command()
    async def roulette(self, ctx, type, bet: int):
        if(bet >= 10):
            user = ctx.message.author.id
            con = psycopg2.connect(DATABASE_URL, sslmode='require')
            cur = con.cursor()
            query = "select * from discord_currency where user_id=%d"%(user)
            cur.execute(query)
            b = cur.fetchone()
            if(b[1] >= bet):
                a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,"red","black","odd","even","low","high"]
                if(type in a):
                    odd = False
                    even = False
                    low = False
                    high = False
                    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
                    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
                    num = random.randint(0,36)
                    await ctx.send("Bot rolled %d"%(num))

                    if(num != 0 and num % 2== 0):
                        even = True
                    elif(num != 0 and num % 2 != 0):
                        odd = True

                    if(0 < num < 19):
                        low = True
                    elif(18 < num):
                        high = True

                    if(type == "black" and num in black):
                        winnings = bet * 2
                        new_balance = b[1] + bet
                        query2="update discord_currency set cash=%d where user_id=%d"%(new_balance,user)
                        cur.execute(query2)
                        con.commit()
                        con.close()
                        await ctx.send("Congratulations! You won back $%d"%(winnings))
                    elif(type == "red" and num in red):
                        winnings = bet * 2
                        new_balance = b[1] + bet
                        query2="update discord_currency set cash=%d where user_id=%d"%(new_balance,user)
                        cur.execute(query2)
                        con.commit()
                        con.close()
                        await ctx.send("Congratulations! You won back $%d"%(winnings))
                    elif(type == "high" and high is True):
                        winnings = bet * 2
                        new_balance = b[1] + bet
                        query2="update discord_currency set cash=%d where user_id=%d"%(new_balance,user)
                        cur.execute(query2)
                        con.commit()
                        con.close()
                        await ctx.send("Congratulations! You won back $%d"%(winnings))
                    elif(type == "low" and low is True):
                        winnings = bet * 2
                        new_balance = b[1] + bet
                        query2="update discord_currency set cash=%d where user_id=%d"%(new_balance,user)
                        cur.execute(query2)
                        con.commit()
                        con.close()
                        await ctx.send("Congratulations! You won back $%d"%(winnings))
                    elif(type == "odd" and odd is True):
                        winnings = bet * 2
                        new_balance = b[1] + bet
                        query2="update discord_currency set cash=%d where user_id=%d"%(new_balance,user)
                        cur.execute(query2)
                        con.commit()
                        con.close()
                        await ctx.send("Congratulations! You won back $%d"%(winnings))
                    elif(type == "even" and even is True):
                        winnings = bet * 2
                        new_balance = b[1] + bet
                        query2="update discord_currency set cash=%d where user_id=%d"%(new_balance,user)
                        cur.execute(query2)
                        con.commit()
                        con.close()
                        await ctx.send("Congratulations! You won back $%d"%(winnings))
                    elif(type == str(num)):
                        winnings = bet * 10
                        new_balance = b[1] + (bet * 9)
                        query2="update discord_currency set cash=%d where user_id=%d"%(new_balance,user)
                        cur.execute(query2)
                        con.commit()
                        con.close()
                        await ctx.send("Congratulations! You won back $%d"%(winnings))
                    else:
                        new_balance = b[1] - bet
                        query2="update discord_currency set cash=%d where user_id=%d"%(new_balance,user)
                        cur.execute(query2)
                        con.commit()
                        con.close()
                        await ctx.send("Yikes! You lost $%d. Better luck next time."%(bet))
                else:
                    await ctx.message.channel.send("Invalid argument, use help command for help on proper usage of this command.")
            else:
                con.close()
                await ctx.message.channel.send("Insufficient balance.")
        else:
            await ctx.message.channel.send("Bet cannot be less than $10.")

    @commands.command()
    async def blackjack_rules(self, ctx):
        await ctx.send("https://bicyclecards.com/how-to-play/blackjack/")

    @commands.command()
    async def blackjack(self, ctx, bet: int):
        player = ctx.message.author.id
        channel = ctx.message.channel.id
        player_cards = random.sample(cards, 2)
        dealer_cards = random.sample(cards, 2)
        soft = False
        insurance = False
        a = player_cards[0].split(":")
        b = player_cards[1].split(":")
        c = dealer_cards[0].split(":")
        d = dealer_cards[1].split(":")
        if(a[0] == 'J' or a[0] == 'Q' or a[0] == 'K'):
            a[0] = '10'
        if(b[0] == 'J' or b[0] == 'Q' or b[0] == 'K'):
            b[0] = '10'
        if(c[0] == 'J' or c[0] == 'Q' or c[0] == 'K'):
            c[0] = '10'
        if(d[0] == 'J' or d[0] == 'Q' or d[0] == 'K'):
            d[0] = '10'
        if(a[0] == 'A'):
            a[0] = '11'
        if(b[0] == 'A'):
            if(a[0] != '11'):
                b[0] = '11'
            else:
                b[0] = '1'
        if(c[0] == 'A'):
            c[0] = '11'
            soft = True
        if(d[0] == 'A'):
            if(c[0] != '11'):
                d[0] = '11'
                soft = True
            else:
                d[0] = '1'
        player_total = int(a[0]) + int(b[0])
        dealer_total = int(c[0]) + int(d[0])
        if(c[0] == '11'):
            embed_blackjack = discord.Embed(
                title="```BLACKJACK```",
                colour=discord.Colour.blue()
            )
            embed_blackjack.add_field(name='Your hand:', value=player_cards[0] + player_cards[1] + "\nTotal: " + str(player_total))
            embed_blackjack.add_field(name="Dealer's hand:", value=dealer_cards[0] + "\nTotal: " + c[0])
            embed_blackjack.add_field(name=".hit:", value="To draw a new card.")
            embed_blackjack.add_field(name=".stand:", value="To end your turn")
            embed_blackjack.add_field(name=".split:", value="To split a pair.")
            embed_blackjack.add_field(name=".double:", value="To double your bet.")
            embed_blackjack.add_field(name=".insurance:", value="Insure yourself against a dealer blackjack.")
            embed_blackjack.add_field(name=".fold:", value="Quit and get half the bet amount back.")
            message = await ctx.send(embed = embed_blackjack)

        else:
            embed_blackjack = discord.Embed(
                title="```BLACKJACK```",
                colour=discord.Colour.blue()
            )
            embed_blackjack.add_field(name='Your hand:', value=player_cards[0] + player_cards[1] + "\nTotal: " + str(player_total))
            embed_blackjack.add_field(name="Dealer's hand:", value=dealer_cards[0] + "\nTotal: " + c[0])
            embed_blackjack.add_field(name=".hit:", value="To draw a new card.")
            embed_blackjack.add_field(name=".stand:", value="To end your turn")
            embed_blackjack.add_field(name=".split:", value="To split a pair.")
            embed_blackjack.add_field(name=".double:", value="To double your bet.")
            embed_blackjack.add_field(name=".fold:", value="Quit and get half the bet amount back.")
            message = await ctx.send(embed = embed_blackjack)
        blackjack_dict.update({player:[player_cards,dealer_cards,bet,channel,message,soft,insurance]})

    @commands.command()
    async def hit(self, ctx):
        player = ctx.message.author.id
        channel = ctx.message.channel.id
        if(blackjack_dict[player]):
            z = blackjack_dict[player]
            if(channel == z[3]):
                player_cards = z[0]
                dealer_cards = z[1]
                bet = z[2]
                message = z[4]
                soft = z[5]
                insurance = z[6]

                new_card = random.choice(cards)
                player_cards.append(new_card)

                new_total = []
                for i in range(0,len(player_cards)):
                    temp = player_cards[i].split(":")
                    if(temp[0] == 'J' or temp[0] == 'Q' or temp[0] == 'K'):
                        new_total.append(10)
                    elif(temp[0] == 'A'):
                        if(11 in new_total):
                            new_total.append(1)
                        else:
                            new_total.append(11)
                    else:
                        new_total.append(int(temp[0]))
                if((sum(new_total) > 21) and (11 in new_total)):
                    new_total.remove(11)
                    new_total.append(1)
                player_total = sum(new_total)
                if(player_total <= 21):
                    x = dealer_cards[0].split(":")
                    if(x[0] == 'J' or x[0] == 'Q' or x[0] == 'K'):
                        x[0] = '10'
                    if(x[0] == 'A'):
                        x[0] = '11'

                    embed_player_cards = ''.join(player_cards)

                    embed_blackjack = discord.Embed(
                        title="```BLACKJACK```",
                        colour=discord.Colour.blue()
                    )
                    embed_blackjack.add_field(name='Your hand:', value=embed_player_cards + "\nTotal: " + str(player_total))
                    embed_blackjack.add_field(name="Dealer's hand:", value=dealer_cards[0] + "\nTotal: " + x[0])
                    embed_blackjack.add_field(name=".hit:", value="To draw a new card.")
                    embed_blackjack.add_field(name=".stand:", value="To end your turn")
                    embed_blackjack.add_field(name=".split:", value="To split a pair.")
                    embed_blackjack.add_field(name=".fold:", value="Quit and get half the bet amount back.")
                    await message.edit(embed = embed_blackjack)
                    blackjack_dict.update({player:[player_cards,dealer_cards,bet,channel,message,soft,insurance]})

                elif(player_total > 21):
                    embed_dealer_cards = ''.join(dealer_cards)
                    embed_player_cards = ''.join(player_cards)

                    x = dealer_cards[0].split(":")
                    if(x[0] == 'J' or x[0] == 'Q' or x[0] == 'K'):
                        x[0] = '10'
                    if(x[0] == 'A'):
                        x[0] = '11'
                    y = dealer_cards[1].split(":")
                    if(y[0] == 'J' or y[0] == 'Q' or y[0] == 'K'):
                        y[0] = '10'
                    if(y[0] == 'A'):
                        if(x[0] != '11'):
                            y[0] = '11'
                        else:
                            y[0] = '1'
                    dealer_total = int(x[0]) + int(y[0])

                    embed_blackjack = discord.Embed(
                        title="```BLACKJACK```",
                        colour=discord.Colour.red()
                    )
                    embed_blackjack.add_field(name='Your hand:', value=embed_player_cards + "\nTotal: " + str(player_total))
                    embed_blackjack.add_field(name="Dealer's hand:", value=embed_dealer_cards + "\nTotal: " + str(dealer_total))
                    await message.edit(embed = embed_blackjack)

                    if(insurance == True):
                        await ctx.send("Insurance successfully received along with 2:1 profit.")

                    blackjack_dict.pop(player)

    @commands.command()
    async def stand(self, ctx):
        player = ctx.message.author.id
        channel = ctx.message.channel.id
        if(blackjack_dict[player]):
            z = blackjack_dict[player]
            if(channel == z[3]):
                player_cards = z[0]
                dealer_cards = z[1]
                bet = z[2]
                message = z[4]
                soft = z[5]
                insurance = z[6]
                c = dealer_cards[0].split(":")
                d = dealer_cards[1].split(":")
                if(c[0] == 'J' or c[0] == 'Q' or c[0] == 'K'):
                    c[0] = '10'
                if(d[0] == 'J' or d[0] == 'Q' or d[0] == 'K'):
                    d[0] = '10'
                if(c[0] == 'A'):
                    c[0] = '11'
                    soft = True
                if(d[0] == 'A'):
                    if(c[0] != '11'):
                        d[0] = '11'
                        soft = True
                dealer_total = int(c[0]) + int(d[0])

                while(dealer_total < 17 and soft == False):
                    new_dealer_card = random.choice(cards)
                    dealer_cards.append(new_dealer_card)

                    new_dealer_total = []
                    for i in range(0,len(dealer_cards)):
                        temp = dealer_cards[i].split(":")
                        if(temp[0] == 'J' or temp[0] == 'Q' or temp[0] == 'K'):
                            new_dealer_total.append(10)
                        elif(temp[0] == 'A'):
                            if(11 in new_dealer_total):
                                new_dealer_total.append(1)
                            else:
                                new_dealer_total.append(11)
                                soft = True
                        else:
                            new_dealer_total.append(int(temp[0]))
                        dealer_total = sum(new_dealer_total)
                    if((sum(new_dealer_total) > 21) and (11 in new_dealer_total)):
                        new_dealer_total.remove(11)
                        new_dealer_total.append(1)
                        soft = False
                    dealer_total = sum(new_dealer_total)

                new_total = []
                for i in range(0,len(player_cards)):
                    temp = player_cards[i].split(":")
                    if(temp[0] == 'J' or temp[0] == 'Q' or temp[0] == 'K'):
                        new_total.append(10)
                    elif(temp[0] == 'A'):
                        if(11 in new_total):
                            new_total.append(1)
                        else:
                            new_total.append(11)
                    else:
                        new_total.append(int(temp[0]))
                if((sum(new_total) > 21) and (11 in new_total)):
                    new_total.remove(11)
                    new_total.append(1)
                player_total = sum(new_total)

                embed_player_cards = ''.join(player_cards)
                embed_dealer_cards = ''.join(dealer_cards)

                if(dealer_total == player_total):
                    embed_blackjack = discord.Embed(
                        title="```BLACKJACK```",
                        colour=discord.Colour.blue()
                    )
                    embed_blackjack.add_field(name='Your hand:', value=embed_player_cards + "\nTotal: " + str(player_total))
                    embed_blackjack.add_field(name="Dealer's hand:", value=embed_dealer_cards + "\nTotal: " + str(dealer_total))

                    await message.edit(embed = embed_blackjack)

                elif(dealer_total > player_total and dealer_total <= 21):
                    embed_blackjack = discord.Embed(
                        title="```BLACKJACK```",
                        colour=discord.Colour.red()
                    )
                    embed_blackjack.add_field(name='Your hand:', value=embed_player_cards + "\nTotal: " + str(player_total))
                    embed_blackjack.add_field(name="Dealer's hand:", value=embed_dealer_cards + "\nTotal: " + str(dealer_total))

                    await message.edit(embed = embed_blackjack)

                elif((dealer_total < player_total) or (dealer_total > player_total and dealer_total > 21) ):
                    embed_blackjack = discord.Embed(
                        title="```BLACKJACK```",
                        colour=discord.Colour.green()
                    )
                    embed_blackjack.add_field(name='Your hand:', value=embed_player_cards + "\nTotal: " + str(player_total))
                    embed_blackjack.add_field(name="Dealer's hand:", value=embed_dealer_cards + "\nTotal: " + str(dealer_total))

                    await message.edit(embed = embed_blackjack)

                if(insurance == True):
                    await ctx.send("Insurance successfully received along with 2:1 profit.")

                blackjack_dict.pop(player)

    @commands.command()
    async def double(self, ctx):
        player = ctx.message.author.id
        channel = ctx.message.channel.id
        if(blackjack_dict[player]):
            z = blackjack_dict[player]
            if(channel == z[3]):
                player_cards = z[0]
                if(len(player_cards) == 2):
                    dealer_cards = z[1]
                    bet = z[2] * 2
                    message = z[4]
                    soft = z[5]
                    insurance = z[6]

                    new_card = random.choice(cards)
                    player_cards.append(new_card)

                    new_total = []
                    for i in range(0,len(player_cards)):
                        temp = player_cards[i].split(":")
                        if(temp[0] == 'J' or temp[0] == 'Q' or temp[0] == 'K'):
                            new_total.append(10)
                        elif(temp[0] == 'A'):
                            if(11 in new_total):
                                new_total.append(1)
                            else:
                                new_total.append(11)
                        else:
                            new_total.append(int(temp[0]))
                    if((sum(new_total) > 21) and (11 in new_total)):
                        new_total.remove(11)
                        new_total.append(1)
                    player_total = sum(new_total)

                    c = dealer_cards[0].split(":")
                    d = dealer_cards[1].split(":")
                    if(c[0] == 'J' or c[0] == 'Q' or c[0] == 'K'):
                        c[0] = '10'
                    if(d[0] == 'J' or d[0] == 'Q' or d[0] == 'K'):
                        d[0] = '10'
                    if(c[0] == 'A'):
                        c[0] = '11'
                        soft = True
                    if(d[0] == 'A'):
                        if(c[0] != '11'):
                            d[0] = '11'
                            soft = True
                    dealer_total = int(c[0]) + int(d[0])

                    if(player_total <= 21):
                        while(dealer_total < 17 and soft == False):
                            new_dealer_card = random.choice(cards)
                            dealer_cards.append(new_dealer_card)

                            new_dealer_total = []
                            for i in range(0,len(dealer_cards)):
                                temp = dealer_cards[i].split(":")
                                if(temp[0] == 'J' or temp[0] == 'Q' or temp[0] == 'K'):
                                    new_dealer_total.append(10)
                                elif(temp[0] == 'A'):
                                    if(11 in new_dealer_total):
                                        new_dealer_total.append(1)
                                    else:
                                        new_dealer_total.append(11)
                                        soft = True
                                else:
                                    new_dealer_total.append(int(temp[0]))
                                dealer_total = sum(new_dealer_total)
                            if((sum(new_dealer_total) > 21) and (11 in new_dealer_total)):
                                new_dealer_total.remove(11)
                                new_dealer_total.append(1)
                                soft = False
                            dealer_total = sum(new_dealer_total)

                        embed_player_cards = ''.join(player_cards)
                        embed_dealer_cards = ''.join(dealer_cards)

                        if(dealer_total == player_total):
                            embed_blackjack = discord.Embed(
                                title="```BLACKJACK```",
                                colour=discord.Colour.blue()
                            )
                            embed_blackjack.add_field(name='Your hand:', value=embed_player_cards + "\nTotal: " + str(player_total))
                            embed_blackjack.add_field(name="Dealer's hand:", value=embed_dealer_cards + "\nTotal: " + str(dealer_total))

                            await message.edit(embed = embed_blackjack)

                        elif(dealer_total > player_total and dealer_total <= 21):
                            embed_blackjack = discord.Embed(
                                title="```BLACKJACK```",
                                colour=discord.Colour.red()
                            )
                            embed_blackjack.add_field(name='Your hand:', value=embed_player_cards + "\nTotal: " + str(player_total))
                            embed_blackjack.add_field(name="Dealer's hand:", value=embed_dealer_cards + "\nTotal: " + str(dealer_total))

                            await message.edit(embed = embed_blackjack)

                        elif((dealer_total < player_total) or (dealer_total > player_total and dealer_total > 21) ):
                            embed_blackjack = discord.Embed(
                                title="```BLACKJACK```",
                                colour=discord.Colour.green()
                            )
                            embed_blackjack.add_field(name='Your hand:', value=embed_player_cards + "\nTotal: " + str(player_total))
                            embed_blackjack.add_field(name="Dealer's hand:", value=embed_dealer_cards + "\nTotal: " + str(dealer_total))

                            await message.edit(embed = embed_blackjack)

                        if(insurance == True):
                            await ctx.send("Insurance successfully received along with 2:1 profit.")

                    else:
                        embed_player_cards = ''.join(player_cards)
                        embed_dealer_cards = ''.join(dealer_cards)

                        embed_blackjack = discord.Embed(
                            title="```BLACKJACK```",
                            colour=discord.Colour.red()
                        )
                        embed_blackjack.add_field(name='Your hand:', value=embed_player_cards + "\nTotal: " + str(player_total))
                        embed_blackjack.add_field(name="Dealer's hand:", value=embed_dealer_cards + "\nTotal: " + str(dealer_total))
                        await message.edit(embed = embed_blackjack)

                        if(insurance == True):
                            await ctx.send("Insurance successfully received along with 2:1 profit.")

                    blackjack_dict.pop(player)

                else:
                    await ctx.send("Cannot double down now. Read blackjack rules at https://bicyclecards.com/how-to-play/blackjack/")

    @commands.command()
    async def insurance(self, ctx):
        player = ctx.message.author.id
        channel = ctx.message.channel.id
        if(blackjack_dict[player]):
            z = blackjack_dict[player]
            if(channel == z[3]):
                player_cards = z[0]
                if(len(player_cards) == 2):
                    dealer_cards = z[1]
                    bet = z[2]
                    message = z[4]
                    soft = z[5]
                    insurance = False
                    c = dealer_cards[0].split(":")
                    d = dealer_cards[1].split(":")
                    if(c[0] == 'A'):
                        c[0] = '11'
                        if(d[0] == 'J' or d[0] == 'Q' or d[0] == 'K' or d[0] == '10'):
                            d[0] = '10'
                            insurance = True
                            blackjack_dict.update({player:[player_cards,dealer_cards,bet,channel,message,soft,insurance]})
                            await ctx.send("You are now insured.")
                        else:
                            None
                    else:
                        await ctx.send("Cannot insure now. Read blackjack rules at https://bicyclecards.com/how-to-play/blackjack/")

    @commands.command()
    async def fold(self,ctx):
        player = ctx.message.author.id
        channel = ctx.message.channel.id
        if(blackjack_dict[player]):
            z = blackjack_dict[player]
            if(channel == z[3]):
                bet = z[2]
                back = z[2] * (1/2)
                blackjack_dict.pop(player)

def setup(client):
    client.add_cog(casino(client))
