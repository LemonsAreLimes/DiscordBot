import discord 
import discord.ext.commands

import os
import requests
import requests.auth
import random

client = discord.ext.commands.Bot(command_prefix="rc.")

class reddit(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
        print('initalized: reddit')
        connectToReddit()
        

    @client.command()
    async def meme(ctx):
        await ctx.send('meme')


def setup(client):
    client.add_cog(reddit(client))



def connectToReddit():
    print('connecting to reddit...')
    client_id = '2SyMUvmDPc3jJUz9PwZm5g'
    key = os.getenv("reddit_key")
    password = os.getenv("reddit_pass")

    #get auth key
    auth = requests.auth.HTTPBasicAuth(client_id, key)

    #login
    data = {
        'grant_type': 'password',
        'username': 'robocough_robot',
        'password': password
    }

    #this is needed ig
    headers = {'User-Agent': 'MyApi/0.0.1'}

    #aquire token
    token = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers).json()['access_token']
    headers['Authorization'] = f'bearer {token}'

    #set it as an eviroment var so it can be used later 
    os.environ['reddit_auth_header'] = headers
    print('connected to reddit!')

# print(headers)

# #get hot posts
# hot_posts = requests.get('https://oauth.reddit.com/r/memes/hot', headers=headers)
# posts = hot_posts.json()['data']['children']

# #pick a random post
# num = random.randint(0, len(posts))

# subreddit = posts[num]['data']['subreddit']
# title = posts[num]['data']['title']
# image = posts[num]['data']['url']
# author = posts[num]['data']['author']

# print(subreddit)
# print(title)
# print(image)
# print(author)

