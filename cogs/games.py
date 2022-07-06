import discord
import discord.ext.commands

# #game libs (cleans up help command)
# from src.GAME_coinflp import coinflip

class View(discord.ui.View):
    @discord.ui.button(label="test", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        await interaction.response.send_message('clicked button')


client = discord.ext.commands.Bot(command_prefix="rc.")

class games(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
        print("initialized: games")

    @client.command()
    async def MenuTest(self, ctx):
        await ctx.send("okay this part worked", View=View())

    # @client.command()
    # async def flip(self, ctx):
    #     coin = coinflip.gen()
    #     print(coin)

    #     buttons = [
    #         create_butt

    #     ]


def setup(client):
    client.add_cog(games(client))



#games:
    #coin flip
    #blackjack
    #roulette
    #wordle?
    #minesweeper?