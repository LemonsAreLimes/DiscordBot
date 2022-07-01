import discord 
import discord.ext.commands

import os
import rule34
import requests
import requests.auth
import json
import random

client = discord.ext.commands.Bot(command_prefix="rc.")

class apis(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client
        print('initialized: apis')
        connectToReddit()
        

    @client.command()                       #google deepdream
    async def dream(self, ctx, Link=None):
        if Link:
            api_key = os.getenv('google_api_key')

            #send image to google deepdream
            r = requests.post(
            "https://api.deepai.org/api/deepdream",
            data={'image':Link},
            headers={'api-key': api_key}
            )
    
            #get the response
            dest = r.json()
            if "output_url" not in str(dest):
                await ctx.send('something went wrong....')

            #create embed with image dest on it
            sender = ctx.author.name
            image = dest['output_url']
            embed = discord.Embed(title=f"{sender}'s deepdream", description="this image will disapear soon", colour=0xA900FF)
            embed.set_image(url=image)
            await ctx.send(embed=embed)
        else:
            await ctx.send("no image link provieded")


    @client.command()                        #reddit/meme
    async def reddit(self, ctx, subreddit_or_post_number=None, post_number_if_subreddit_provided=None):

        #humans will be humans

        if subreddit_or_post_number == None:                    #no args? use default
            post_num = 1
            sub = 'memes'
        elif subreddit_or_post_number.isnumeric() == True:      #int? thats the number of posts to show
            post_num = subreddit_or_post_number
            sub = 'memes'
        else:                                                   #string? use it for the sub
            sub = subreddit_or_post_number

        if post_number_if_subreddit_provided == None:                    #no arg? post 1
            post_num = 1
        elif post_number_if_subreddit_provided.isnumeric() == True:      #int? thats the numeber of things to post 
            post_num = int(post_number_if_subreddit_provided)
        else:                                                            #string? call em a dumb dumb
            await ctx.send('no no no, wrong syntax there bud')
            return

        if post_num > 5:                    #just a limit i wanted to add
            post_num = 5
            await ctx.send('post limit is 5 ok')

        if 'r/' in sub:                     #humman error is quite common
            sub = sub.replace('r/', '')

    
        #get hot posts
        headers = json.loads(os.getenv('reddit_auth_header'))
        hot_posts = requests.get(f'https://oauth.reddit.com/r/{sub}/hot', headers=headers)
        posts = hot_posts.json()['data']['children']

        while True: #used to replace for loop
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
                        break
                    else:
                        not_in_filetype += 1

                #prevents looping over and over
                if not_in_filetype >= 20:
                    break

            except:
                pass

    @client.command() 
    async def r34(self, ctx, images=1, tags=''):
        await ctx.send(f'images: {images}, tags: {tags}')

        # rule34 = rule34.Sync()
        # req = rule34.getImages(tags='mario blush gay')

        # print(req)

        # for i in req:
        #     print(i.file_url)
        #     print(i.score)
        #     print(i.tags)
    


def setup(client):
    client.add_cog(apis(client))


#apis
    #rule34



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