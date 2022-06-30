import discord
import discord.ext.commands

client = discord.ext.commands.Bot(command_prefix="rc.")

class admin_Tools(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
    print("initialized: admin tools")

    @client.command()
    async def test(self, ctx):
        reply_speed = round(self.client.latency * 1000)
        await ctx.send(f'latency: {reply_speed}ms')

    @client.command()
    async def mute(self, ctx, member: discord.Member=None):
        if 'administrator' in str(ctx.author.roles) and member != None :
            muted_role = discord.utils.get(member.guild.roles , id = 990039934725414953)
            member.add_roles(muted_role)
        else:
            await ctx.send('define a user to mute, or... become admin')

    @client.command()
    async def kick(self, ctx, member: discord.Member=None, reason=None):
        if 'administrator' in str(ctx.author.roles) and member != None:
            if reason:
                await member.kick(reason=reason)
            else:
                await member.kick()
        else:
            await ctx.send('u gotta be admin my guy')
            await ctx.send('or something went wrong in dexters code....')

    @client.command()
    async def purge(self, ctx, number=0):
        if 'administrator' in str(ctx.author.roles):
            messages = []   #messages within channel => i dont know how to do this lol
            count = number
            for msg in messages:
                if count <= 0:
                    break
                else:
                    count -= 1
                    await msg.delete()
            await ctx.send(f'deleted {number} messages')
        else:
            await ctx.send('ur not admin lol')
    

def setup(client):
    client.add_cog(admin_Tools(client))
