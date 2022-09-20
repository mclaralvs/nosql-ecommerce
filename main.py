import pymongo
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("mongodb+srv://maria:1234@mclaralvs.ggbjgpw.mongodb.net/mercadolivre")
db = client.test

global mydb
mydb = client.mercadolivre

# SORT FUNCTION
def findSort():
    global mydb
    mycol = mydb.usuario

    print("\nSORT\n---------------------") 
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x)

# FIND FUNCTIONS
def findUser(cpf):
    global mydb
    mycol = mydb.usuario

    print("\nUSER QUERY\n---------------------")
    myuser = {"cpf": cpf}
    global user
    user = mycol.find_one(myuser)

def findVendor(cpf):
    global mydb
    mycol = mydb.vendedor

    print("\nVENDOR QUERY\n---------------------")
    myvendor = {"cpf": cpf}
    global vendor
    vendor = mycol.find_one(myvendor)

def findProduct(nome):
    global mydb
    mycol = mydb.produto

    print("\nPRODUCT QUERY\n---------------------")
    myproduct = {"nome": nome}
    global product
    product = mycol.find_one(myproduct)

def findPurchase(nome):
    global mydb
    mycol = mydb.purchase

    print("\nPURCHASE QUERY\n---------------------")
    mypurchase = {"nome": nome}
    global purchase
    purchase = mycol.find_one(mypurchase)


# INSERT FUNCTIONS
def insertUser(nome, cpf, email, rua, cidade, estado, numero):
    global mydb
    mycol = mydb.usuario

    print("\nINSERT USER\n---------------------")
    mydict = {"nome": nome, "cpf": cpf, "email": email, "endereco": [{"rua": rua, "cidade": cidade, "estado": estado, "numero": numero}]}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def insertVendor(vendNome, vendCpf, vendEmail, vendRua, vendCidade, vendEstado, vendNumero):
    global mydb
    mycol = mydb.vendedor

    print("\nINSERT VENDOR\n---------------------")
    mydict = {"nome": vendNome, "cpf": vendCpf, "email": vendEmail, "endereco": [{"rua": vendRua, "cidade": vendCidade, "estado": vendEstado, "numero": vendNumero}]}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def insertProduct(prodNome, prodPreco, qtd, prodStatus):
    global mydb
    mycol = mydb.produto

    print("\nINSERT PRODUCT\n---------------------")
    mydict = {"nome": prodNome, "preco": prodPreco, "quantidade": qtd, "status": prodStatus, "vendedor": {"id": vendor.get("_id"), "nome": vendor.get("nome")}}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def insertPurchase(precoTotal, status, data, formaPgt):
    global mydb
    mycol = mydb.compra

    print("\nINSERT PURCHASE\n---------------------")
    mydict = {"precoTotal": precoTotal, "status": status, "data": data, "formaPagamento": formaPgt, "produto": [{"id": product.get("_id"), "nome": product.get("nome"), "preco": product.get("preco"), "vendedor": {"id": vendor.get("_id"), "nome": vendor.get("nome")}}], "usuario": {"id": user.get("_id"), "nome": user.get("nome"), "cpf": user.get("cpf")}}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)


# SEARCH FUNCTION
def searchUsers():
    global mydb
    mycol = mydb.usuario

    print("\nUSERS SEARCH\n---------------------")
    users = mycol.find({})
    userslist = []
    for user in users:
        userslist.append(user)
    return print(userslist)

def searchVendors():
    global mydb
    mycol = mydb.vendedor

    print("\nVENDORS SEARCH\n---------------------")
    vendors = mycol.find({})
    vendorslist = []
    for vendor in vendors:
        vendorslist.append(vendor)
    return print(vendorslist)

def searchProducts():
    global mydb
    mycol = mydb.produto

    print("\nPRODUCTS SEARCH\n---------------------")
    products = mycol.find({})
    productslist = []
    for product in products:
        productslist.append(product)
    return print(productslist)

def searchPurchases():
    global mydb
    mycol = mydb.compra

    print("\nPURCHASES SEARCH\n---------------------")
    purchases = mycol.find({})
    purchaseslist = []
    for purchase in purchases:
        purchaseslist.append(purchase)
    return print(purchaseslist)


# DELETE FUNCTION
def deleteUser():
    global mydb
    mycol = mydb.usuario

    print("\nUSER DELETE\n---------------------")
    mycol.delete_one({"_id": user.get("_id")})

def deleteVendor():
    global mydb
    mycol = mydb.vendedor

    print("\nVENDOR DELETE\n---------------------")
    mycol.delete_one({"_id": vendor.get("_id")})

def deleteProduct():
    global mydb
    mycol = mydb.produto

    print("\nPRODUCT DELETE\n---------------------")
    mycol.delete_one({"_id": product.get("_id")})


############# main

#findSort()
#findQuery()
#findUser("123.123.123.11")
#findVendor("123.123.123.11")
#findProduct("Ventilador")
#insertUser("Tais Salomao", "123.123.123.11", "tais.salomao@gmail.com", "Alameda das Laranjeiras", "Sao Jose dos Campos", "Sao Paulo", "98")
#insertVendor("Mariana Ayumi", "123.123.123.11", "mariana.ayumi@gmail.com", "Alameda das Laranjeiras", "Sao Jose dos Campos", "Sao Paulo", "98")
#insertProduct("Ventilador", "19.90", "20", "Disponível")
#insertPurchase("89.90", "Finalizado!", "20/09/2022", "Débito")
#searchUsers()
#searchVendors()
#searchProducts()
#searchPurchases()
#deleteUser()
#deleteVendor()
#deleteProduct()