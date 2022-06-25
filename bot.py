import os
import discord
import discord.ext.commands
import discord.reaction

print('script initalized!')

#defines the client and command prefex
client = discord.ext.commands.Bot(command_prefix ='rc.')

#load cogs
print('loading cogs')
client.load_extension('cogs.admin_tools')
client.load_extension('cogs.stuff')
print('done loading cogs!')

#bot initlized msg
@client.event
async def on_ready():
    print("""
    bot initialized...
    waiting for commands master.
    """)

# @client.event
# async def on_message(message):
#     print('new msg')
#     await message.channel.send(message)


# @client.event
# async def on_member_join(member):


#events
    #active logger          => logs who is active and when
    #server stats           => daily msg num log
    #reaction roles         => self-explanitory
    #greeting message       => rand gen


#connect bot to discord
Token = os.getenv("token")
client.run(Token)