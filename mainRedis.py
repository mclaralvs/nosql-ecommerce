# importing the databases ✨
import redis
import pymongo

# importing json functions ✨
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

# connecting to mongodb ✨
client = pymongo.MongoClient(
    "mongodb+srv://maria:<PASSWORD>@mclaralvs.ggbjgpw.mongodb.net/mercadolivre")
db = client.test

global mydb
mydb = client.mercadolivre

# connecting to redis ✨
dbRedis = redis.Redis(host='redis-12850.c60.us-west-1-2.ec2.cloud.redislabs.com',
                      port=12850,
                      password='<PASSWORD>')

# FUNCTION: login ✨
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

        print(dbRedis.hget('user:' + user['cpf'], 'status'))

# FUNCTION: logout ✨
def logout(cpf):
    # finding the collection from mongodb ✨
    mycol = mydb.usuario

    # finding the user ✨
    myuser = {"cpf": cpf}

    user = mycol.find_one(myuser)

    status = dbRedis.hget('user:' + cpf, 'status')

    if (status.decode() == 'logged in'):
        dbRedis.hset('user:' + cpf, 'status', 'logged out')

        print(dbRedis.hget('user:' + cpf, 'status'))

    else:
        print('User is already logged out')

# FUNCTION: change product price ✨
def changePrice(id, price):
    # finding the collection from mongodb ✨
    mycol = mydb.produto

    product = mycol.find_one(ObjectId(id))

    dbRedis.hset('product:' + id, 'preco', price)  

    print(dbRedis.hget('product:' + id, 'preco')) 

# FUNCTION: change product status ✨
def changeStatus(id, status):
    # finding the collection from mongodb ✨
    mycol = mydb.produto

    product = mycol.find_one(ObjectId(id))

    dbRedis.hset('productStatus:' + id, 'status', status)  

    print(dbRedis.hget('productStatus:' + id, 'status')) 

# commands ✨

## login commands ☁
login("123.123.123.11")
logout("123.123.123.11")

## change product price command ☁
changePrice("632cdccb212e49d773492276", 256.64)

## change product status command ☁
changeStatus("632cdccb212e49d773492276", 'Indisponivel')