import discord
import discord.ext.commands

client = discord.ext.commands.Bot(command_prefix="rc.")

class admin_Tools(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
    print("admin_tools initialized")

    @client.command()
    async def test(ctx):
        # author = ctx.message.author
        # avatar = author.avatar_url
        await ctx.send('cog loaded!')

def setup(client):
    client.add_cog(admin_Tools(client))
