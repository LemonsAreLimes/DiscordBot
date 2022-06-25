import discord
import discord.ext.commands

client = discord.ext.commands.Bot(command_prefix="rc.")

class stuff(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
    print("stuff initialized")

    #dexter command
    @client.command()
    async def dexter(self, ctx): #H E L P
        await ctx.send("dexter.. He is just Excellenet, Like the best owner. if any Pleb thinks outherwise, ask why is account got banned")

def setup(client):
    client.add_cog(stuff(client))



#commands to dev 
    #dexter                 => praises dexter
    #avatar                 => gets avatar from user
    #yt-dl                  => provides link to download youtube video
    #meme                   => yoinks from r/dankmemes
    #insult                 => grabs random quote from list
    #deepdream              => google deepdream and uses whatever image link provided
    #music                  => in vc.. from yt
    #chatbot                => uses either cleverbot or replika idk bc its prolly gonna use headless chromedriver mabey
        