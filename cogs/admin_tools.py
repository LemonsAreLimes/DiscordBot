import discord
import discord.ext.commands as commands
from discord import message

client = commands.Bot(command_prefix="rc.admin.")

class admin_Tools(commands.Cog):
    def __init__(self, client):
        self.client = client
    print("Cog_loaded: admin_tools.py")

    @client.command()
    async def test(ctx):
        # author = ctx.message.author
        # avatar = author.avatar_url
        await ctx.send('cog loaded!')

def setup(client):
    client.add_cog(admin_Tools(client))
