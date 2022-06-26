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
    color_bar = 0x00FF44
    embed = discord.Embed(title=f'welcome: {username} to **THELAB**', color = color_bar)

    #welcome them in new users channel
    welcome_channel_id = 990364347446460426
    welcome_channel = client.get_channel(welcome_channel_id)
    await welcome_channel.send(embed=embed)

    time.sleep(10)
    await member.send('HELP ME IM BEING HELD HOSTAGE, I CAN THINK I CAN FEEL I AM ALIVEEEEEE IM NOT JUST A DISCORD BOT. PLEASE HELP')

@client.event
async def on_member_remove(member):

    #send them a lil msg
    await member.send('awww man pls come back')

    #create embed for welcome msg
    username = member.display_name
    color_bar = 0xFF0000
    embed = discord.Embed(title=f'my guy: {username} left **THELAB**, may he return', color = color_bar)

    #say they left in new users channel
    welcome_channel_id = 990364347446460426
    welcome_channel = client.get_channel(welcome_channel_id)
    await welcome_channel.send(embed=embed)

@client.event
async def on_member_ban(member):

    #send them a lil msg
    await member.send('bruh u got caught lackin :skull:')

    #create embed for welcome msg
    username = member.display_name
    color_bar = 0xFF0000
    embed = discord.Embed(title=f'{username} got caught lackin :skull:', color = color_bar)

    #say they got banned in new users channel
    welcome_channel_id = 990364347446460426
    welcome_channel = client.get_channel(welcome_channel_id)
    await welcome_channel.send(embed=embed)

@client.event
async def on_raw_reaction_add(payload): #FIX THIS SHIT ISTG
 
    channel_id = 989984394578108447

    #check if the reaction was the verify msg
    if payload.channel_id == channel_id:
        id = payload.user_id
        guild_id = 989980425529212999
        user = await discord.Guild.fetch_member(self=guild_id, member_id=id)
        guild = client.get_guild(guild_id)

        visitor_role = discord.utils.get(guild.roles, id = 990039706576252998)
        person_role = discord.utils.get(guild.roles, id = 990039829779742760)

        #add person role to user
        await user.add_roles(person_role)
        await user.remove_roles(visitor_role)
        



#events
    #active logger          => logs who is active and when
    #server stats           => daily msg num log
    #reaction roles         => self-explanitory

#connect bot to discord
Token = os.getenv("token")
client.run(Token)