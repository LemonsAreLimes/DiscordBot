import random
import discord

class cfButtons(discord.ui.View):

    @discord.ui.button(label="Heads", style=discord.ButtonStyle.primary)
    async def heads_callback(self, button, interaction):

        for child in self.children: 
            child.disabled = True

        #gen random coin
        flip = bool(random.getrandbits(1))
        if flip:
            button.style = discord.ButtonStyle.green
            await interaction.response.edit_message(content="you won!", view=self)
        else:
            button.style = discord.ButtonStyle.red
            await interaction.response.edit_message(content="you lost..", view=self)

    @discord.ui.button(label="Tails", style=discord.ButtonStyle.primary)
    async def tails_callback(self, button, interaction):

        for child in self.children: 
            child.disabled = True

        #gen random coin
        flip = bool(random.getrandbits(1))
        if flip:
            button.style = discord.ButtonStyle.green
            await interaction.response.edit_message(content="you won!", view=self)
        else:
            button.style = discord.ButtonStyle.red
            await interaction.response.edit_message(content="you lost..", view=self)

        