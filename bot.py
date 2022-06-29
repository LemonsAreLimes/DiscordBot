import os
import discord
import discord.ext.commands
import discord.reaction
import time

from .src import mongo_stuff as moong

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
client.load_extension('cogs.apis')
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

    #create new log in mongo
    user_id = member.id
    name = member.name
    moong.mongo.CreateUser(user_id, name)


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
async def on_raw_reaction_add(payload):
 
    channel_id = 989984394578108447

    #check if the reaction was the verify msg
    if payload.channel_id == channel_id:
        id = payload.user_id
        guild_id = 989980425529212999
        guild = client.get_guild(guild_id)
        user = await guild.fetch_member(id)

        print(payload.emoji)
        print(payload.emoji.name)

        emoji = payload.emoji.name
        if emoji == '✅':

            #define roles
            visitor_role = discord.utils.get(guild.roles, id = 990039706576252998)
            person_role = discord.utils.get(guild.roles, id = 990039829779742760)

            #add/rm role to user
            await user.add_roles(person_role)
            await user.remove_roles(visitor_role)
        
        elif emoji == '🇷':
            red = discord.utils.get(guild.roles, id=990039992799752192)
            await user.add_roles(red)

        elif emoji == '🇬':
            green = discord.utils.get(guild.roles, id=990040077902180443)
            await user.add_roles(green)

        elif emoji == '🇧':
            blue = discord.utils.get(guild.roles, id=990040103512571924)
            await user.add_roles(blue)

        elif emoji == '🇨':
            cyan = discord.utils.get(guild.roles, id=990040131874480158)
            await user.add_roles(cyan)

        elif emoji == '🇲':
            magenta = discord.utils.get(guild.roles, id=990040172118827060)
            await user.add_roles(magenta)

        elif emoji == '🇾':
            yellow = discord.utils.get(guild.roles, id=990040219053097050)
            await user.add_roles(yellow)

        elif emoji == '🇰':
            black = discord.utils.get(guild.roles, id=990040253081477140)
            await user.add_roles(black)

        else:
            print(emoji)
            print('emoji not found')




#events
    #active logger          => logs who is active and when
    #server stats           => daily msg num log
    #auto mod???

#connect bot to discord
Token = os.getenv("token")
client.run(Token)