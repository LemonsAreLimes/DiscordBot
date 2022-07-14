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

for cog in config.cogs:
    client.load_extension(cog)


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
    visitor_role = discord.utils.get(member.guild.roles, id = config.join_leave_channel_id)
    await member.add_roles(visitor_role)

    #welcome them in new users channel
    welcome_channel = client.get_channel(config.join_leave_channel_id)
    embed = discord.Embed(title=title, color = 0x00FF44)
    await welcome_channel.send(embed=embed)
    
@client.event
async def on_member_remove(member):

    title = await config.leave_msg(self=config, member=member)
  
    #say they left in new users channel
    welcome_channel = client.get_channel(config.join_leave_channel_id)
    embed = discord.Embed(title=title, color = 0xFF0000)
    await welcome_channel.send(embed=embed)




@client.event
async def on_raw_reaction_add(payload):
 

    #check if the reaction was in the reactions channel
    if payload.channel_id == config.reaction_channel_id:

        #define guild and user
        guild_id = config.server_id
        guild = client.get_guild(guild_id)
        
        id = payload.user_id
        user = await guild.fetch_member(id)

        role_id = config.emoji_to_role_id(emoji=payload.emoji.name)
        
        if role_id == "new_user":

            #define roles
            visitor_role = discord.utils.get(guild.roles, id = config.visitor_role_id)
            person_role = discord.utils.get(guild.roles, id = config.verified_role_id)

            #add/rm role to user
            await user.add_roles(person_role)
            await user.remove_roles(visitor_role)
        
        elif role_id == None:
            print('yeah')

        else:
            role = discord.utils.get(guild.roles, id = role_id)
            await user.add_roles(role)


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