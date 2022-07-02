import discord
import discord.ext.commands

client = discord.ext.commands.Bot(command_prefix="rc.")

class stuff(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
        print("initialized: stuff")

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

    @client.command()
    async def racisim(self, ctx):
        await ctx.send('I HATE NIGGERS!!!!!')

def setup(client):
    client.add_cog(stuff(client))



#commands to dev 
    #insult                 => grabs random quote from list
    #chatbot                => uses either cleverbot or replika idk bc its prolly gonna use headless chromedriver mabey

#music
    #play       [link], join vc with sender
    #pause           
    #stop
    #skip
    #join
    #leave
