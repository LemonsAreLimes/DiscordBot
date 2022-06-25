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

    #avatar => i already wrote this in prev bot
    @client.command()
    async def avatar(self, ctx, user: discord.Member=None):
        if user == None:
            #use the pfp of sender of command
            user = ctx.message.author

        avatar = user.avatar_url

        #create an embed with image of pfp
        embed = discord.Embed(title=f"{user}'s avatar", colour=0x00FF2A)
        embed.set_image(url=avatar)
        await ctx.send(embed=embed)


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
        