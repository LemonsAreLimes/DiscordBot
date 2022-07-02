# import discord
# import discord.ext.commands
# from youtube_dl import YoutubeDL
# from discord import FFmpegPCMAudio

# client = discord.ext.commands.Bot(command_prefix="rc.")

# class music(discord.ext.commands.Cog):
#     def __init__(self, client):
#         self.client = client
#         print("initialized: music")

#     @client.command()
#     async def join(self, ctx):
        
#         #get memeber id from ctx
#         user_id = ctx.author.id
#         member = ctx.guild.get_member(user_id=user_id)
#         voice = member.voice 

#         #check if user is in voice channel
#         if voice != None:
#             await ctx.send(f'joining voice channel with {ctx.author}')
#             await voice.channel.connect()
#         else:
#             await ctx.send('join a vc broh')

#     @client.command()
#     async def leave(self, ctx):
#         await ctx.voice_client.disconnect()

#     @client.command()
#     async def play(self, ctx, url=None):
#         if url != None:

#             #definetly not stolen from stack over flow ;)
#             ydl_opts = {'format': 'bestaudio', 'noplaylist':'True'}
#             FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
#             voice = ctx.voice_client

#             with YoutubeDL(ydl_opts) as ydl:
#                 info = ydl.extract_info(url, download=False)
#             URL = info['formats'][0]['url']
#             voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
 
#         else:
#             await ctx.send('give us something man')

#     @client.command()
#     async def stop(self, ctx):
#         pass
#         #stops plying the music

# def setup(client):
#     client.add_cog(music(client))




# #music
#     #play       [link], join vc with sender
#     #pause           
#     #stop
#     #skip
#     #join
#     #leave
