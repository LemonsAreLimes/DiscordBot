import random
import discord
from src.config import config
from src.mongo_stuff import mongo


class cfButtons(discord.ui.View):

    @discord.ui.button(label="Heads", style=discord.ButtonStyle.primary)
    async def heads_callback(self, button, interaction):
        user_id = interaction.user.id
        
        for child in self.children: 
            child.disabled = True

        #gen random coin
        flip = bool(random.getrandbits(1))
        if flip:
            coins = config.cf_coins
            button.style = discord.ButtonStyle.green
            await interaction.response.edit_message(content="you won!", view=self)

        else:
            coins = 0-(config.cf_coins)
            button.style = discord.ButtonStyle.red
            await interaction.response.edit_message(content="you lost..", view=self)

        mongo.addCoins(user_id, coins)

    @discord.ui.button(label="Tails", style=discord.ButtonStyle.primary)
    async def tails_callback(self, button, interaction):
        user_id = interaction.user.id
        
        for child in self.children: 
            child.disabled = True

        #gen random coin
        flip = bool(random.getrandbits(1))
        if flip:
            coins = config.cf_coins
            button.style = discord.ButtonStyle.green
            await interaction.response.edit_message(content="you won!", view=self)

        else:
            coins = 0-(config.cf_coins)
            button.style = discord.ButtonStyle.red
            await interaction.response.edit_message(content="you lost..", view=self)

        mongo.addCoins(user_id, coins)