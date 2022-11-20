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

    # getting data from redis ✨
    status = dbRedis.hget('user:' + cpf, 'status')

    # checks if user's already logged in ✨
    if (status.decode() == 'logged in'):
        print('User is already logged in')

    # if not, they can log in ✨
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

    # getting data from redis ✨
    status = dbRedis.hget('user:' + cpf, 'status')

    # checks if user's in fact logged in so they can log out ✨
    if (status.decode() == 'logged in'):
        dbRedis.hset('user:' + cpf, 'status', 'logged out')

        print(dbRedis.hget('user:' + cpf, 'status'))

    # if not, they can't log out ✨
    else:
        print('User is already logged out')

# FUNCTION: change product price ✨
def changePrice(id, price):
    # finding the collection from mongodb ✨
    mycol = mydb.produto

    product = mycol.find_one(ObjectId(id))

    # sets the new price on redis ✨
    dbRedis.hset('product:' + id, 'preco', price)

    # updates the data on mongodb ✨
    mycol.update_one({"_id": ObjectId(id)}, {"$set": {
        "preco": json.loads(dbRedis.hget("product:" + id, 'preco')),
    }}, upsert=True)

    print('Price Updated ✨')
    print(dbRedis.hget('product:' + id, 'preco'))

# FUNCTION: change product status ✨
def changeStatus(id, status):
    # finding the collection from mongodb ✨
    mycol = mydb.produto

    product = mycol.find_one(ObjectId(id))

    # sets the new status on redis ✨
    dbRedis.hset('productStatus:' + id, 'status', status)

    # updates the status on mongodb ✨
    mycol.update_one({"_id": ObjectId(id)}, {"$set": {
        "status": dbRedis.hget("productStatus:" + id, str('status')).decode(),
    }}, upsert=True)

    print('Status Updated ✨')
    print(dbRedis.hget('productStatus:' + id, 'status'))


# commands ✨
# login commands ☁
login("123.123.123.11")
logout("123.123.123.11")

# change product price command ☁
changePrice("6377fdd45498906bad49f4e4", 256.64)

# change product status command ☁
changeStatus("6377fdeb9ad4153e292d70ae", "Indisponivel")