from src.mongo_stuff import mongo

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

    multiple_join_and_leave_msg = True

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