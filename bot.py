from lib2to3.pgen2 import token
import os
import discord
import discord.ext.commands
import discord.reaction

print('script initalized!')



#defines the client and command prefex
client = discord.ext.commands.Bot(command_prefix ='rc.')

#bot initlized msg
@client.event
async def on_ready():
    print("""
    bot initialized...
    waiting for commands master.
    """)

#help command
@client.command()
async def h(ctx):
    await ctx.send("""
    learn more about me here => https://github.com/LemonsAreLimes/DiscordBot
    i am hosted on heroku, now i can live forever!!
    my current commands:
        help
        dexter
    """)

@client.command()
async def dexter(ctx): #H E L P
    await ctx.send("dexter.. He is just Excellenet, Like the best owner. if any Pleb thinks outherwise, ask why is account got banned")

@client.command()
async def reac(ctx):
    users = await discord.Message.reactions
    await ctx.send(users)

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