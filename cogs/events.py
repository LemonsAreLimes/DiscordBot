import discord
import discord.ext.commands

client = discord.ext.commands.Bot(command_prefix="rc.")

class events(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
    print("events initialized")

    #doesnt seem to work
    @client.event
    async def on_ready():
        print('bot online, events working')

    #might be easier to test idk
    @client.event
    async def on_message(message):
        print('new msg detected!')

    #join msg not working either
    @client.event
    async def on_member_join(member):
        print('new member!')

        #get username / profile
        print(member)
        new_user = discord.Guild.get_member(member)
        name = new_user.display_name
        color = new_user.color

        #this will be removed if it works fine as is
        print(new_user)
        print(name)
        print(color)

        #send welcome msg
        embed = discord.Embed(title=f"welcome: {name} to **THELAB**", color=color) 

        channel = client.get_channel(990364347446460426)
        await channel.send(embed)
        

def setup(client):
    client.add_cog(events(client))
    


#events 
    #greeting message       => rand gen
    #server stats           => daily msg num log
    #reaction roles         => self-explanitory
    #active logger          => logs who is active and when