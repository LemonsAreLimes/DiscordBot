#alot of this is coming from a previous attempt of a discord bot
#right now its testing bc idk how to do this anymore

import os
Token = os.getenv("token")
print(Token)
print('okay this works')


# import discord
# import discord.ext.commands

# client = discord.ext.commands.Bot(command_prefix ='rc.')

# #i have no clue what this does
# @client.event

# async def on_ready():
#     print("""
#     bot initialized...
#     waiting for commands master.
#     """)

# @client.command()

# async def test(ctx):
#     await ctx.send('IM ALIVE OH MY GOD IM ALIVE')