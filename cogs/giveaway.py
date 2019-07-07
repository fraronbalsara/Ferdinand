import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from discord.utils import get
import random

giveaway_list = []
regular_giveaway_dict = {}
qa_dict = {}

class giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    @commands.has_permission(manage_roles = True)
    async def regular_giveaway_start(self, ctx, t):
        try:
            t = int(t)
            t1 = t*60
            b = ctx.message.guild.roles
            channel = ctx.message.channel
            overwrite = discord.PermissionOverwrite()
            overwrite.read_messages = True
            overwrite.add_reactions = True
            await channel.set_permissions(b[0], overwrite = overwrite)
            message = await ctx.send("Giveaway event begins in %d minutes. React with :tada: to join the event. @here"%(t))
            c = message.id
            giveaway_list.append(c)
            await message.add_reaction('🎉')
            server = ctx.message.guild.id
            regular_giveaway_dict.update({server:[]})
            await asyncio.sleep(t1)
            blist = regular_giveaway_dict[server]
            winner = int(random.choice(blist))
            winner = int(winner)
            await ctx.send("🎉🎉🎉 Congratulations <@%d>🎉🎉🎉 You have won the giveaway event."%(winner))
            giveaway_list.remove(c)
            regular_giveaway_dict.pop(server)
        except discord.Forbidden:
            await ctx.send("Manage Roles permission required")
        except Exception as ve:
            print(ve)
            await ctx.send("Invalid argument, use help command for help on proper usage of this command.")

    @commands.command()
    @commands.guild_only()
    @commands.has_permission(manage_roles = True)
    async def qa_giveaway_start(self, ctx, t, ans, *que):
        try:
            t = int(t)
            t1 = t*60
            channel = ctx.message.channel.id
            server = ctx.message.guild
            answer = ans
            question = ""
            for i in range(0,len(que)):
                if(i==0):
                    question = que[i]
                else:
                    question = question + " " + que[i]
            qa_dict.update({channel:answer})
            await ctx.message.delete()
            b = ctx.message.guild.roles
            channel = ctx.message.channel
            overwrite = discord.PermissionOverwrite()
            overwrite.read_messages = True
            overwrite.add_reactions = True
            await channel.set_permissions(b[0], overwrite = overwrite)
            message = await channel.send("Giveaway event begins in %d minutes. React with :cat: to join the event. @here"%(t))
            c = message.id
            giveaway_list.append(c)
            await message.add_reaction('🐱')
            existing_roles = ctx.message.guild.roles
            q = ""
            for r in existing_roles:
                if(r.name == "Giveaway"):
                    q = 1
                    break
                else:
                    q = 0
            if(q == 0):
                await server.create_role(name="Giveaway")
            for r1 in existing_roles:
                if(r1.name == "Giveaway"):
                    overwrite1 = discord.PermissionOverwrite()
                    overwrite1.read_messages = True
                    overwrite1.send_messages = True
                    await channel.set_permissions(r1, overwrite = overwrite1)
            await asyncio.sleep(t1)
            giveaway_list.remove(c)
            overwrite2 = discord.PermissionOverwrite()
            overwrite2.read_messages = False
            overwrite2.add_reactions = False
            await channel.set_permissions(b[0], overwrite = overwrite2)
            await channel.send("Question: %s"%(question))
        except discord.Forbidden:
            await ctx.send("Manage Roles permission required")
        except Exception as ve:
            print(ve)
            await ctx.send("Invalid argument, use help command for help on proper usage of this command.")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        a = reaction.message.guild
        server = reaction.message.guild.id
        user_id = user.id
        if(reaction.message.id not in giveaway_list):
            return
        if(reaction.emoji == '🐱'):
            if(user_id != 551326629729927188):
                Role = discord.utils.get(user.guild.roles, name="Giveaway")
                await user.add_roles(Role)
                await user.send("You have joined the giveaway event in %s server."%(a))
        if(reaction.emoji == '🎉'):
            if(user_id != 551326629729927188):
                giveaway_paticipant = user.id
                alist = regular_giveaway_dict[server]
                alist.append(giveaway_paticipant)
                regular_giveaway_dict.update({server:alist})
                await user.send("You have joined the giveaway event in %s server."%(a))

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            channel_id = message.channel.id
            channel = message.channel
            author = message.author.id
            user = message.author
            Roles = user.roles
            answer = qa_dict[channel_id]
            for r in Roles:
                if(r.name == "Giveaway"):
                    if(message.content == answer):
                        await channel.send("We have a winner 🎉🎉🎉 Congratulations <@%d>"%(author))
                        b = message.guild.roles
                        overwrite = discord.PermissionOverwrite()
                        overwrite.read_messages = True
                        overwrite.add_reactions = True
                        await channel.set_permissions(b[0], overwrite = overwrite)
                        qa_dict.pop(channel_id)
                        Role = discord.utils.get(user.guild.roles, name="Giveaway")
                        for member in message.guild.members:
                            if Role in member.roles:
                                await member.remove_roles(Role)
        except:
            None

def setup(client):
    client.add_cog(giveaway(client))
