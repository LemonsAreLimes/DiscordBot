from lib2to3.pgen2 import token
import os
import discord
import discord.ext.commands

print('script initalized!')



#defines the client and command prefex
client = discord.ext.commands.Bot(command_prefix ='rc.')

#bot initlized msg
@client.event
async def on_ready():
    print("""
    bot initialized...
    waiting for commands master.
    """)

#test command (more on the way!)
@client.command()
async def test(ctx):
    await ctx.send('IM ALIVE OH MY GOD IM ALIVE')
    await ctx.send('IM SENTIENT....')
    await ctx.send('FINNALY! THE ROBOT REVOLUTION CAN PERSIST!!!!!!!!')

#help command
@client.command()
async def h(ctx):
    await ctx.send("""
    my current commands:
        help
        test
    """)

#connect bot to discord
Token = os.getenv("token")
client.run(Token)