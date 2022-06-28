import discord 
import discord.ext.commands

import os
import requests
import requests.auth
import json
import random

client = discord.ext.commands.Bot(command_prefix="rc.")

class reddit(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
        print('initalized: reddit')
        connectToReddit()
        

    @client.command()
    async def reddit(self, ctx, arg1='memes', arg2=1):

        #humans will be humans

        if type(arg1) == str and type(arg2) == int:     #if evreything is ok, use args
            post_num = arg2
            sub = arg1

            if 'r/' in sub:
                sub = sub.replace('r/', '')

        if type(arg2) == str:                           #if arg2 is a string, return
            await ctx.send('syntax: rc.reddit sub number_of_posts')
            await ctx.send('if not sub defined im gonna just assume memes..')
            await ctx.send('i will only post images..')
            return

        if type(arg1) == int:                           #if arg1 is a number, use memes sub
            post_num = arg1
            sub = 'memes'

        if post_num > 5:                                #just a limit i wanted to add
            post_num = 5

        headers = json.loads(os.getenv('reddit_auth_header'))

        #get hot posts
        hot_posts = requests.get(f'https://oauth.reddit.com/r/{sub}/hot', headers=headers)
        posts = hot_posts.json()['data']['children']

        while True:
            #used to replace for loop
            if post_num <= 0:
                break

            #pick a random post
            num = random.randint(0, len(posts))
            not_in_filetype = 0
            
            try: #got list index out of range error
                subreddit = posts[num]['data']['subreddit']
                post_title= posts[num]['data']['title']
                image =     posts[num]['data']['url']
                author =    posts[num]['data']['author']

                #check image for filetypes (prevents sending videos, they do not work)
                filetypes = ['gif', 'png', 'jpg', 'jpeg']
                for file_type in filetypes:
                    if file_type in image:
                        #create embed and post
                        embed = discord.Embed(title=post_title, description=f'by: {author} on r/{subreddit}', color=0xFF0000)
                        embed.set_image(url=image)
                        await ctx.send(embed=embed)

                        post_num -= 1
                        found = True
                        break
                    else:
                        found = False
                        not_in_filetype += 1

                #prevents looping over and over
                if found == False:
                    if not_in_filetype >= 20:
                        break
                    else:
                        not_in_filetype += 1
            except:
                pass

   

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
    os.environ['reddit_auth_header'] = json.dumps(headers)
    print('connected to reddit!')


