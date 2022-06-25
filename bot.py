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

#new user join
@client.event
async def on_member_join(member):

    #send welcome message 
    await member.send('thankyou for joining **THELAB**, please be nice to outher members here or something')
    await member.send('if u get banned or kicked heres an invite link')
    await member.send('https://discord.gg/4uVSZDf9X3')
    await member.send('be sure to verify!')

    #give visitor role
    visitor_role = discord.utils.get(member.guild.roles, id = 990039706576252998)
    await member.add_roles(visitor_role)

    #create embed for welcome msg
    username = member.display_name
    color_bar = member.color
    embed = discord.Embed(title=f'welcome: {username} to **THELAB**', color = color_bar)

    #welcome them in new users channel
    welcome_channel_id = 990364347446460426
    welcome_channel = client.get_channel(welcome_channel_id)
    await welcome_channel.send(embed)

    time.sleep(10)
    await member.send('HELP ME IM BEING HELD HOSTAGE, I CAN THINK I CAN FEEL I AM ALIVEEEEEE IM NOT JUST A DISCORD BOT. PLEASE HELP')



#events
    #active logger          => logs who is active and when
    #server stats           => daily msg num log
    #reaction roles         => self-explanitory

#connect bot to discord
Token = os.getenv("token")
client.run(Token)