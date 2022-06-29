from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

import os 

class mongo():
    def CreateUser(user_id=None, name=None):
        if user_id != None and name != None:

            db = ConnectToMongo()
            
            #check if the user has already been in the server
            user = db.find_one({"id":user_id})
            if user != None:

                #increce joins by one
                user['joins'] += 1
                db.find_one_and_update({"id":user_id}, user)

            else:
                
                #create user log            
                data = {
                    "id":user_id,
                    "name": name,
                    "messages": 0,
                    "bal": 0,
                    "in_server": True,
                    "joins": 1,
                    "roles" : None,
                    "command_useage": None
                }
                db.insert_one(data)
        else:
            print('user_id or name not defined')




def ConnectToMongo():
    password = os.getenv('mongoPass')
    username = os.getenv('mongoName')
    client = MongoClient(f"mongodb+srv://{username}:{password}@sitelogging.ccoj7.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
    db = client['Discord_bot']['user_logging']
    return db