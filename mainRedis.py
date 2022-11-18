# importing the databases ✨
import redis
import pymongo

# importing json functions ✨
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

# connecting to mongodb ✨
client = pymongo.MongoClient(
    "mongodb+srv://maria:1234@mclaralvs.ggbjgpw.mongodb.net/mercadolivre")
db = client.test

global mydb
mydb = client.mercadolivre

# connecting to redis ✨
dbRedis = redis.Redis(host='redis-12850.c60.us-west-1-2.ec2.cloud.redislabs.com',
                      port=12850,
                      password='O4Gy6ZYU3tjsL2JkpznWHeQ9bevrYVwi')

# login function ✨
def login(cpf):
    # finding the collection from mongodb ✨
    mycol = mydb.usuario

    # finding the user ✨
    myuser = {"cpf": cpf}

    user = mycol.find_one(myuser)

    status = dbRedis.hget('user:' + cpf, 'status')

    if (status.decode() == 'logged in'):
        print('User is already logged in')

    else:
        dbRedis.hset('user:' + user['cpf'], 'status', 'logged in')  

        print(dbRedis.keys())

        print(dbRedis.hget('user:' + user['cpf'], 'status'))

# logout function ✨
def logout(cpf):
    status = dbRedis.hget('user:' + cpf, 'status')

    if (status.decode() == 'logged in'):
        dbRedis.hset('user:' + cpf, 'status', 'logged out')
        print(dbRedis.hget('user:' + cpf, 'status'))
    else:
        print('User is already logged out')

# transform it into json ✨
#userObject = dumps(user)


# sends it to redis ✨
#sendRedis = dbRedis.set('mydb', usersObject)

#usersList = json.loads(dbRedis.get('mydb'))

# printing the user
""" for user in usersList:
    print(user['nome'])
    userObject = dumps(user) """

#dbRedis.hmset('nome', 'oiii')
# print(us8er['nome'])

login("123.123.123.11")
#logout("123.123.123.11")