import discord
import discord.ext.commands
import requests #used for deepdream and meme

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
        embed = discord.Embed(title=f"{user}'s avatar", colour=0xA900FF)
        embed.set_image(url=avatar)
        await ctx.send(embed=embed)

    #youtube download link
    @client.command()
    async def ytdl(self, ctx, video_link=None):
        if video_link == None:
            await ctx.send('no youtube link provided!')

        video_link = f'{video_link[:19]}pp{video_link[19:]}'
        await ctx.send(str(video_link))

    #deepdream
    @client.command()
    async def dream(self, ctx, Link=None):

        if Link == None:
            await ctx.send("no image link provieded")
        else:
            #send image to google deepdream
            r = requests.post(
            "https://api.deepai.org/api/deepdream",
            data={'image':Link,},
            headers={'api-key': 'fc7ab6e9-055d-4967-bcfc-d9f754c97bc1'})
    
            #get the response
            dest = r.json()
            if "output_url" in str(dest):

                #create embed with image dest on it
                sender = ctx.message.author
                image = dest['output_url']

                embed = discord.Embed(title=f"{sender}'s deepdream", description="this image will disapear soon", colour=0xA900FF)
                embed.set_image(url=image)
                await ctx.send(embed=embed)

            else:
                await ctx.send("Something went wrong")

                #create embed with image dest on it
                sender = ctx.message.author
                image = dest['output_url']

                embed = discord.Embed(title=f"{sender}'s deepdream", description="this image will disapear soon", colour=0xA900FF)
                embed.set_image(url=image)
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
        