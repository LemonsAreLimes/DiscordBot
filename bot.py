from lib2to3.pgen2 import token
import os
import discord
import discord.ext.commands

print('script initalized!')

Token = os.getenv("token")     #might fix invalad token
print(Token)
print(type(Token))

print('token initalized')

#defines the client and command prefex
client = discord.ext.commands.Bot(command_prefix ='rc.')

#bot initlized msg
@client.event
async def on_ready():
    print("""
    bot initialized...
    waiting for commands master.
    """)

# #test command (more on the way!)
# @client.command()
# async def test(ctx):
#     await ctx.send('IM ALIVE OH MY GOD IM ALIVE')

#connect bot to discord????????
client.run(Token)