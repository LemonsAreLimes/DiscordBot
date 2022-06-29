from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

import os 

class mongo():
    def CreateUser(user_id=None, name=None):
        if user_id != None and name != None:
            db = ConnectToMongo()
            
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

    def EditUserData(user_id=None, data=None):
        if user_id != None and data != None:
            db = ConnectToMongo()
            user = db.find_one({"id":user_id})
            print(user)
        else:
            print('user ID or data not defined!')




def ConnectToMongo():
    password = os.getenv('mongoPass')
    username = os.getenv('mongoName')
    client = MongoClient(f"mongodb+srv://{username}:{password}@sitelogging.ccoj7.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
    db = client['Discord_bot']['user_logging']
    return db