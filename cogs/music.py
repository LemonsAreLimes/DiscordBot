import discord
import discord.ext.commands

client = discord.ext.commands.Bot(command_prefix="rc.")

class music(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
        print("initialized: music")


    @client.command()
    async def join(self, ctx):
        
        #get memeber id from ctx
        user_id = ctx.author.id
        member = ctx.guild.get_member(user_id=user_id)
        voice = member.voice 

        #check if user is in voice channel
        if voice != None:
            await ctx.send(f'joining voice channel with {ctx.author}')
            await voice.channel.connect()
        else:
            await ctx.send('join a vc broh')

    @client.command()
    async def leave(self, ctx):
        #get memeber id from ctx
        user_id = ctx.author.id
        member = ctx.guild.get_member(user_id=user_id)
        voice = member.voice 

        #check if user is in voice channel
        if voice != None:
            await ctx.send('disconnecting...')
            await voice.channel.disconnect()
        else:
            await ctx.send('you gotta be in the vc to do that!')

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
