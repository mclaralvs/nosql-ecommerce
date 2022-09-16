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

# QUERY FUNCTION
def findQuery():
    global mydb
    mycol = mydb.usuario

    print("\nQUERY\n---------------------")
    myquery = {"nome": "Tais Salomao"}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

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

def insertProduct(prodNome, prodPreco, qtd, prodStatus, vendId, vendNome):
    global mydb
    mycol = mydb.produto

    # FAZER UMA QUERY PELO NOME DO VENDOR
    # RETORNAR E SALVAR O ID E NOME EM UMA VARIÁVEL
    # SALVAR A VARIÁVEL NO BANCO
    # VAI PODER TIRAR O vendId/vendNome DA FUNÇÃO

    print("\nINSERT PRODUCT\n---------------------")
    mydict = {"nome": prodNome, "preco": prodPreco, "quantidade": qtd, "status": prodStatus, "vendedor": [{"id": vendId, "nome": vendNome}]}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def insertPurchase(precoTotal, status, data, formaPgt, prodId, prodNome, prodPreco, userId, userNome):
    global mydb
    mycol = mydb.compra

    # FAZER UMA QUERY PELO NOME DO PRODUTO
    # RETORNAR E SALVAR O ID E NOME DO PRODUTO E VENDOR EM UMA VARIÁVEL
    # SALVAR A VARIÁVEL NO BANCO
    # FAZER O MESMO COM O USUÁRIO
    # VAI PODER TIRAR O prodId/prodNome/prodPreco/userId/userNome DA FUNÇÃO

    print("\nINSERT PURCHASE\n---------------------")
    mydict = {"precoTotal": precoTotal, "status": status, "data": data, "formaPagamento": formaPgt, "produto": [{"id": prodId, "nome": prodNome, "preco": prodPreco}], "usuario": [{"id": userId, "nome": userNome}]}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

############# main

findSort()
findQuery()
#insertUser("Tais Salomao", "123.123.123.11", "tais.salomao@gmail.com", "Alameda das Laranjeiras", "Sao Jose dos Campos", "Sao Paulo", "98")
#insertVendor("Mariana Ayumi", "123.123.123.11", "mariana.ayumi@gmail.com", "Alameda das Laranjeiras", "Sao Jose dos Campos", "Sao Paulo", "98")
insertProduct("Ventilador", "19.90", "20", "Disponível")
#insertPurchase("89.90", "Finalizado!", "20/09/2022", "Débito")