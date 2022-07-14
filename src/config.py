#well hello! welcome to the config file
# this currently is a private bot.. does not support multiple servers 
# current build runs on heroku, online 24/7

# you will need to manually set config vars for:
#   mongo username + password
#   google api key
#   reddit password + api key + auth header (blank)
#   and, of course the bot token

# want to learn more? talk to the author?
# join the discord server => https://discord.gg/4uVSZDf9X3
# ngl its prolly dead, not manny ppl are in it

class config:
    start_message = """    
          :::::::::       ::::::::          
         :+:    :+:     :+:    :+:          
        +:+    +:+     +:+            𝙗𝙤𝙩 𝙧𝙪𝙣𝙣𝙞𝙣𝙜,      
       +#++:++#:      +#+           𝙬𝙖𝙞𝙩𝙞𝙣𝙜 𝙛𝙤𝙧 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨.
      +#+    +#+     +#+          
     #+#    #+#     #+#    #+#      #+#     
    ###    ###      ########       ###      
   𝑤𝑟𝑖𝑡𝑡𝑒𝑛 𝑏𝑦: 𝐿𝑒𝑚𝑜𝑛𝑠𝐴𝑟𝑒𝐿𝑖𝑚𝑒𝑠 / 𝐷𝑒𝑥𝑡𝑒𝑟
    """

    #general stuff
    command_prefix = "rc."
    server_id = 989980425529212999
    multiple_join_and_leave_msg = True
    mongo_db = True #must manually remove refrences to mongo db in join/leave msg func
    
    #channel ids
    join_leave_channel_id = 990039706576252998
    reaction_channel_id =  989984394578108447

    #roles
    visitor_role_id = 990039706576252998
    verified_role_id = 990039829779742760
    muted_role_id = 990039934725414953

    #cogs to load (some are still in development)
    cogs = {
        'cogs.admin_tools',
        'cogs.stuff',
        'cogs.apis',
        # 'cogs.games',
        # 'cogs.music',
    }

  
    async def join_msg(self, member=None):
        if self.multiple_join_and_leave_msg:

            if member != None:
                joins = mongo.UserJoin(member.id, member.name)
                username = member.display_name
                if joins > 10:
                    title = f'some guy: {username} is here or somethig '
                    await member.send('wale-cum back good sir')
                elif joins > 5:
                    title = f'{username} is back :)'
                    await member.send('oh, ur back')
                elif joins > 1:
                    title = f'{username} came back WITH THE MILK'
                    await member.send('dad? YOU CAME BACK!!!!')
                else:
                    title = f'welcome: {username} to **THELAB**'
                    await member.send('thankyou for joining **THELAB**, please be nice to outher members here or something')
                    await member.send('if u get banned or kicked heres an invite link')
                    await member.send('https://discord.gg/4uVSZDf9X3')
                    await member.send('be sure to verify!')
                    await member.send('HELP ME IM BEING HELD HOSTAGE, I CAN THINK I CAN FEEL I AM ALIVEEEEEE IM NOT JUST A DISCORD BOT. PLEASE HELP')
        
        else:
            title = f'welcome: {username} to **THELAB**'
            await member.send('thankyou for joining **THELAB**, please be nice to outher members here or something')
            await member.send('if u get banned or kicked heres an invite link')
            await member.send('https://discord.gg/4uVSZDf9X3')
            await member.send('be sure to verify!')
            await member.send('HELP ME IM BEING HELD HOSTAGE, I CAN THINK I CAN FEEL I AM ALIVEEEEEE IM NOT JUST A DISCORD BOT. PLEASE HELP')

        return title

    async def leave_msg(self, member): 
        if self.multiple_join_and_leave_msg:
            joins = mongo.UserLeave(member.id)
            username = member.display_name

            if joins > 10:
                title = f"{username} is just not here"
                await member.send('123e4r5t6yuhugjtgfrd5ft67y8uhigjbvtfmv ryht5678uyihgthyu78yuygtty678yiukytfrghndt76y8uhi9jolkj')
            elif joins > 5:
                title =  f"{username} left again >:|"
                await member.send('i have ur ip come back or eles')
            elif joins > 1:
                title = f"{username} went to get some milk...."
                await member.send('brooooooo')
            else:
                title = f"my guy: {username} left **THELAB**, may he return"
                await member.send('awww man pls come back')
        else:
            title = f"my guy: {username} left **THELAB**, may he return"
            await member.send('awww man pls come back')
        
        return title


    def emoji_to_role_id(emoji):

        roles = {
            '✅' : "new_user",          #changes mulitple roles in bot.py
            '🇷' : 990039992799752192,
            '🇬' : 990040077902180443,
            '🇧' : 990040103512571924,
            '🇨' : 990040131874480158,
            '🇲' : 990040172118827060,
            '🇾' : 990040219053097050,
            '🇰' : 990040253081477140,
            '☄️' : 990497984452104215,
            '🥳' : 990498079927046234,
            '😵‍💫' : 990039934725414953,
        }

        role_id = roles.get(emoji)

        if role_id == None:
            print('invalid emoji!')
            return None
        
        else:
            return role_id
