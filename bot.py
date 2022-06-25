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
client.load_extension('cogs.events')
print('done loading cogs!')

#bot initlized msg
@client.event
async def on_ready():
    print("""
    bot initialized...
    waiting for commands master.
    """)

#commands to dev 
    #dexter                 => praises dexter
    #reaction roles         => self-explanitory
    #greeting message       => rand gen
    #avatar                 => gets avatar from user
    #active logger          => logs who is active and when
    #server stats           => daily msg num log

    #yt-dl                  => provides link to download youtube video
    #meme                   => yoinks from r/dankmemes
    #insult                 => grabs random quote from list

    #deepdream              => google deepdream and uses whatever image link provided
    #music                  => in vc.. from yt
    #chatbot                => uses either cleverbot or replika idk bc its prolly gonna use headless chromedriver mabey
        
    #admin tools
        #mute               => changes roles
        #purge              => deletes messages
    #games w/ currency sys
        #gesser             => 50/50 channce
        #blackjack          
        #roulette           => significantly lower chance
        #connect4           => no clue how im going to do this 
        #buy_role           => kinda act like levels


#connect bot to discord
Token = os.getenv("token")
client.run(Token)