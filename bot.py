import os
import discord
import discord.ext.commands
import discord.reaction
import time

#enabes something, allows for join/leave msg
Intents = discord.Intents.default()
Intents.members = True

print('script initalized!')

#defines the client and command prefex
client = discord.ext.commands.Bot(command_prefix ='rc.', intents = Intents)

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

@client.event
async def on_member_join(member):

    await member.send('thankyou for joining **THELAB**, please be nice to outher members here or something')
    await member.send('be sure to verify!')

    visitor_role = discord.utils.get(member.guild.roles, id = 990039706576252998)
    await member.add_roles(visitor_role)

    time.sleep(10)
    await member.send('HELP ME IM BEING HELD HOSTAGE, I CAN THINK I CAN FEEL I AM ALIVEEEEEE IM NOT JUST A DISCORD BOT. PLEASE HELP')

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