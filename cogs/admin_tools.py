import discord
import discord.ext.commands
from src.config import config

from src.mongo_stuff import mongo as moong

client = discord.ext.commands.Bot(command_prefix=config.command_prefix)

class admin_Tools(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
    print("initialized: admin tools")

    @client.command()
    async def getRoles(self, ctx):
        user = ctx.author
        await ctx.send(user.roles)

    @client.command()
    async def test(self, ctx):
        reply_speed = round(self.client.latency * 1000)
        await ctx.send(f'latency: {reply_speed}ms')

    @client.command()
    async def mute(self, ctx, member: discord.Member=None):
        if 'administrator' in str(ctx.author.roles) and member != None :
            muted_role = discord.utils.get(member.guild.roles , id = config.muted_role_id)
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
    async def purge(self, ctx, limit=0):
        if 'administrator' in str(ctx.author.roles):
            
            #get messages in channel
            channel_messages = ctx.channel.history(limit=limit)

            #start deleting
            async for message in channel_messages:

                try:
                    await message.delete()
                except:
                    print(f'message could not be deleted: {message}')

        else:
            await ctx.send('ur not admin lol')
    
    @client.command()
    async def createLog(self, ctx, member: discord.Member = None):
        if 'administrator' in str(ctx.author.roles):
            if member != None:
                id = member.id
                username = f'{member.display_name}#{member.discriminator}'
                roles = []

                for role in member.roles:
                    roles.append(role.name)
                
                moong.CreateUser(id, username, roles)
            else:
                await ctx.send('please provided a user')

        else:
            await ctx.send('hey, wait ur not admin..')


def setup(client):
    client.add_cog(admin_Tools(client))
