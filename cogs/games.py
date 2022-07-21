import discord
import discord.ext.commands

# #game libs (cleans up help command)
from src.GAME_coinflp import cfButtons

client = discord.ext.commands.Bot(command_prefix ='rc.', intents=discord.Intents.all())

class games(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
        print("initialized: games")

    @client.command()
    async def cf(self, ctx):
        view = cfButtons()
        await ctx.send("heads or tails", view=view)

        


def setup(client):
    client.add_cog(games(client))



#games:
    #coin flip
    #blackjack
    #roulette
    #wordle?
    #minesweeper?