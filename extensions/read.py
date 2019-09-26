import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

class read(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        post_channel = self.client.get_channel(624434158642659329)
        get_channel = self.client.get_channel(259536527221063683)
        bot_1 = self.client.get_user(551326629729927188)

        if get_channel == channel:
            mes = message.content.split(" ")
            flag = mes[0]
            name = mes[1].replace("*","")
            if not mes[2].startswith("<"):
                name = name + mes[2]
            gender = "-"
            dsp = "-"
            for i in range(0, len(mes) - 1):
                if mes[i].startswith("IV"):
                    iv = mes[i]
                elif mes[i].startswith("**CP"):
                    cp = mes[i].replace("*","")
                elif mes[i].startswith("**L") and len(mes[i]) <= 7:
                    level = mes[i].replace("*","")
                elif mes[i] == "♂" or mes[i] == "♀":
                    gender = mes[i].replace("*","")
                elif "free" in mes[i]:
                    link = mes[i].split("\n")
                elif "DSP" in mes[i]:
                    dsp = mes[i] + " " + mes[i + 1] + " " + mes[i + 2]

            if "L35" in message.content:
                #send level 35 spawns with @35 tag
                await bot_1.send(flag + " " + name + " " + iv + " " + cp + " " + level + " " + gender + " " + dsp + "\n" + link[0]  + "\n<@&%d>"%(624503251575898142))
            else:
                #regular spawn testing
                await bot_1.send(flag + " " + name + " " + iv + " " + cp + " " + level + " " + gender + " " + dsp + "\n" + link[0])

def setup(client):
    client.add_cog(read(client))
