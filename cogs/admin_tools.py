import discord
import discord.ext.commands

client = discord.ext.commands.Bot(command_prefix="rc.")

class admin_Tools(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
    print("admin_tools initialized")

    @client.command()
    async def test(self, ctx):
        reply_speed = round(self.client.latency * 1000)
        await ctx.send(f'latency: {reply_speed}ms')

    @client.command()
    async def getRoles(self, ctx, user: discord.Member=None):
        if user == None: 
            user = ctx.author
            await ctx.send(user.roles)
        else:
            await ctx.send(user.roles)

    

def setup(client):
    client.add_cog(admin_Tools(client))


#admin tools
    #mute               => changes roles
    #purge              => deletes messages
    #ban
    #kick