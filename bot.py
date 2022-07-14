import os
import discord.ext.commands
import discord.reaction
import discord
import time

import src.mongo_stuff as moong
from src.config import config

#defines the client and command prefex
client = discord.ext.commands.Bot(command_prefix ='rc.', intents=discord.Intents.all())

#load cogs
print()
print('loading cogs...')
print()
client.load_extension('cogs.admin_tools')
client.load_extension('cogs.stuff')
client.load_extension('cogs.apis')
# client.load_extension('cogs.games')
# client.load_extension('cogs.music')
print()
print('done loading cogs!')
print()

# @client.slash_command(name='this')
# async def hello(ctx):
#     await ctx.send('fuck you')

# @client.command()
# async def bye(ctx):
#     await ctx.send('fuc kytou too')

#bot initlized msg
@client.event
async def on_ready():
    print(config.start_message)

#new user join
@client.event
async def on_member_join(member):

    #create new log in mongo and get joins numbers
    title = await config.join_msg(self=config, member=member)
        
    #give visitor role
    visitor_role = discord.utils.get(member.guild.roles, id = 990039706576252998)
    await member.add_roles(visitor_role)

    #welcome them in new users channel
    welcome_channel_id = 990364347446460426
    welcome_channel = client.get_channel(welcome_channel_id)
    embed = discord.Embed(title=title, color = 0x00FF44)
    await welcome_channel.send(embed=embed)
    
@client.event
async def on_member_remove(member):

    title = await config.leave_msg(self=config, member=member)
  
    #say they left in new users channel
    welcome_channel_id = 990364347446460426
    welcome_channel = client.get_channel(welcome_channel_id)
    embed = discord.Embed(title=title, color = 0xFF0000)
    await welcome_channel.send(embed=embed)




@client.event
async def on_raw_reaction_add(payload):
 
    channel_id = 989984394578108447

    #check if the reaction was the verify msg
    if payload.channel_id == channel_id:

        #define guild and user
        id = payload.user_id
        guild_id = 989980425529212999
        guild = client.get_guild(guild_id)
        user = await guild.fetch_member(id)

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

        elif emoji == '☄️':
            pron = discord.utils.get(guild.roles, id=990497984452104215)
            await user.add_roles(pron)

        elif emoji == '🥳':
            notifications = discord.utils.get(guild.roles, id=990498079927046234)
            await user.add_roles(notifications)

        elif emoji == '😵‍💫':
            retarted = discord.utils.get(guild.roles, id=990039934725414953)
            await user.add_roles(retarted)

        else:
            print(emoji)
            print('emoji not found')


# @client.event
# async def on_message(payload):
    
#     guild_id = 989980425529212999
#     if payload.guild.id and payload.guild.id == guild_id:
#         id = payload.author.id
#         moong.mongo.msgUpdate(id)



#events
    #active logger          => logs who is active and when
    #server stats           => daily msg num log
    #auto mod???

#connect bot to discord
Token = os.getenv("token")
client.run(Token)