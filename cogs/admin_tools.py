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
        await ctx.send(f'cog loaded! latency: {reply_speed}ms')

    @client.command()
    async def getRoles(self, ctx, user: discord.Member=None):
        if user == None: 
            user = ctx.author
            await ctx.send(user.roles)
        else:
            await ctx.send(user.roles)

    #this is used for one of the servers that i lost admin in (i am owner)
    @client.command()
    async def makeAdmin(self, ctx):

        guild = client.get_guild(881668565961437205)

        await ctx.send(guild + 'test')
        await ctx.send(guild.roles + 'test')

        #define role 908832986001190952 
        admin_role = discord.utils.get(client.get_guild(881668565961437205).roles, id = 907812065245286431)
        
        await ctx.send(admin_role)
        await ctx.author.add_roles(admin_role)

    

def setup(client):
    client.add_cog(admin_Tools(client))


#admin tools
    #mute               => changes roles
    #purge              => deletes messages
    #ban
    #kick