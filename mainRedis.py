# importing the databases ✨
import redis
import pymongo

# importing json functions ✨
import json
from bson.json_util import dumps

# connecting to mongodb ✨
client = pymongo.MongoClient("mongodb+srv://maria:<PASSWORD>@mclaralvs.ggbjgpw.mongodb.net/mercadolivre")
db = client.test

global mydb
mydb = client.mercadolivre

# connecting to redis ✨
dbRedis = redis.Redis(host='redis-12850.c60.us-west-1-2.ec2.cloud.redislabs.com',
    port=12850,
    password='<PASSWORD>')

# get data from mongo ✨
users = mydb['usuario'].find()

# transform it into json ✨
usersObject = dumps(users)

# sends it to redis ✨
sendRedis = dbRedis.set('mydb', usersObject)

usersList = json.loads(dbRedis.get('mydb'))

# printing the user
for user in usersList:
    print(user['nome'])
    userObject = dumps(user)

    #dbRedis.hmset('nome', 'oiii')
    #print(us8er['nome'])