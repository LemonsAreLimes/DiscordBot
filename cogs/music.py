import discord
import discord.ext.commands

client = discord.ext.commands.Bot(command_prefix="rc.")

class music(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
        print("initialized: music")


    @client.command()
    async def join(self, ctx):
        
        user_id = ctx.author.id

        member = await discord.Guild.get_member(self=self, user_id=user_id)
        
        voice_channel = member.voice.channel 

        #get memeber id from ctx
        if voice_channel != None:
            await ctx.send(f'joining voice channel with {ctx.author}')
            await voice_channel.connect()
        else:
            await ctx.send('join a vc broh')

    @client.command()
    async def leave(self, ctx):
        pass
        #leave vc with author
        #must be only one in vc OR cast vote OR have the music stoped

    @client.command()
    async def play(self, ctx, YTlink=None):
        if YTlink != None:
            pass
            #check if the bot is in a vc with author
            #check if its a youtube link
            #play audio

        else:
            await ctx.send('please provide a link')

    @client.command()
    async def stop(self, ctx):
        pass
        #stops plying the music

def setup(client):
    client.add_cog(music(client))



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
