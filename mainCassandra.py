from cmath import log
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# connecting to cassandra ✨
cloud_config= {'secure_connect_bundle': 'secure-connect-mydb.zip'}

auth_provider = PlainTextAuthProvider('<PLAIN TEXT AUTH PROVIDER>')

cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)

session = cluster.connect()

# connecting to the db ✨
print ("\nCreating Keyspace ✨")
session.execute("USE mercadolivre")
print ("----------------------------")


# creating tables ✨
## users ☁
print ("\nCreating Users Table ✨")
session.execute("CREATE TABLE IF NOT EXISTS usuario (email text PRIMARY KEY, nome text, cpf text, endereco list<text>, fav list<text>);")
print ("----------------------------")

## vendors ☁
print ("\nCreating Vendors Table ✨")
session.execute("CREATE TABLE IF NOT EXISTS vendedor (email text PRIMARY KEY, nome text, cpf text, endereco list<text>);")
print ("----------------------------")

## products ☁
print ("\nCreating Products Table ✨")
session.execute("CREATE TABLE IF NOT EXISTS produto (id text PRIMARY KEY, nome text, preco text, quantidade text, status text, vendedor list<text>);")
print ("----------------------------")

## purchases ☁
print ("\nCreating Purchases Table ✨")
session.execute("CREATE TABLE IF NOT EXISTS compra (id text PRIMARY KEY, precototal text, status text, data text, formapagamento text, produto list<text>, vendedor list<text>, usuario list<text>);")
print ("----------------------------")


# function: CREATE
## users ☁
def insertUser(email, cpf, endereco, nome):
    print ("\nCreating User ✨")

    preInsert = session.prepare("INSERT INTO usuario (email, cpf, endereco, nome) VALUES (?, ?, ?, ?);")

    session.execute(preInsert, [email, cpf, endereco, nome])

    print ("----------------------------")

## vendors ☁
def insertVendor(email, cpf, endereco, nome):
    print ("\nCreating Vendor ✨")

    preInsert = session.prepare("INSERT INTO vendedor (email, cpf, endereco, nome) VALUES (?, ?, ?, ?);")

    session.execute(preInsert, [email, cpf, endereco, nome])

    print ("----------------------------")

## products ☁
def insertProduct(id, nome, preco, quantidade, status, vendorEmail):
    print ("\nCreating Product ✨")

    vendors = session.execute("SELECT * FROM vendedor;")

    for vendor in vendors:
        if (vendor.email == vendorEmail):
            vendorInfo = [vendorEmail, vendor.nome]
            preInsert = session.prepare("INSERT INTO produto (id, nome, preco, quantidade, status, vendedor) VALUES (?, ?, ?, ?, ?, ?);")

            session.execute(preInsert, [id, nome, preco, quantidade, status, vendorInfo])

            print ("----------------------------")
            
## purchases ☁
def insertPurchase(id, status, data, formaPagamento, productName, quantidade, vendorEmail, userEmail):
    print ("\nCreating Purchase ✨")

    products = session.execute("SELECT * FROM produto;")
    vendors = session.execute("SELECT * FROM vendedor;")
    users = session.execute("SELECT * FROM usuario;")

    for product in products:
        if (product.nome == productName):
            for vendor in vendors:
                if (vendor.email == vendorEmail):
                    for user in users:
                        if (user.email == userEmail):
                            precoTotal = float(product.preco) * int(quantidade)
                            
                            preInsert = session.prepare("INSERT INTO compra (id, precototal, status, data, formapagamento, produto, vendedor, usuario) VALUES (?, ?, ?, ?, ?, ?, ?, ?);")

                            session.execute(preInsert, [id, str(precoTotal), status, data, formaPagamento, [product.id, productName, product.preco, quantidade], [vendorEmail, vendor.nome], [userEmail, user.nome]])

                            print ("----------------------------")

## favs ☁
def insertFav(email, productName):
    print ("\nCreating Fav ✨")

    products = session.execute("SELECT * FROM produto;")
    users = session.execute("SELECT * FROM usuario;")

    for user in users:
        if (user.email == email):
            for product in products:
                if (product.nome == productName):
                    preInsert = session.prepare("UPDATE usuario SET fav = fav + ? WHERE email = ?;")
            
                    session.execute(preInsert, [ [product.id, productName, product.preco, product.vendedor[0], product.vendedor[1] ], email])
    
                    print ("----------------------------")


# function: READ
## users ☁
def readAllUsers():
    print ("\nReading All Users ✨")

    users = session.execute("SELECT * FROM usuario;")
    usersList = [{}]

    for user in users:
        usersList.append({user.email, user.nome, user.endereco[0], user.endereco[1], user.endereco[2], user.endereco[3]})
        print (usersList)
    
    print ("----------------------------")

def readUser(email):
    print ("\nReading User ✨")

    users = session.execute("SELECT * FROM usuario;")
    userList = {}

    for user in users:
        if (user.email == email):
            userList = {user.nome, user.cpf, user.endereco[0], user.endereco[1], user.endereco[2], user.endereco[3]}
        print (userList)

    print ("----------------------------")

## vendors ☁
def readAllVendors():
    print ("\nReading All Vendors ✨")

    vendors = session.execute("SELECT * FROM vendedor;")
    vendorsList = [{}]

    for vendor in vendors:
        vendorsList.append({vendor.email, vendor.nome, vendor.endereco[0], vendor.endereco[1], vendor.endereco[2], vendor.endereco[3]})
        print (vendorsList)
    
    print ("----------------------------")

def readVendor(email):
    print ("\nReading Vendor ✨")

    vendors = session.execute("SELECT * FROM vendedor;")
    vendorList = {}

    for vendor in vendors:
        if (vendor.email == email):
            vendorList = {vendor.nome, vendor.cpf, vendor.endereco[0], vendor.endereco[1], vendor.endereco[2], vendor.endereco[3]}
        print (vendorList)

    print ("----------------------------")

## products ☁
def readAllProducts():
    print ("\nReading All Products ✨")
    products = session.execute("SELECT * FROM produto;")
    productsList = [{}]

    for product in products:
        productsList.append({product.nome, product.preco, product.quantidade, product.status, product.vendedor[0], product.vendedor[1]})
        print (productsList)
    
    print ("----------------------------")

def readProduct(id):
    print ("\nReading Product ✨")

    products = session.execute("SELECT * FROM produto;")
    productList = {}

    for product in products:
        if (product.id == id):
            productList = {product.nome, product.preco, product.quantidade, product.status, product.vendedor[0], product.vendedor[1]}
        print (productList)

    print ("----------------------------")

## products ☁
def readAllPurchases():
    print ("\nReading All Purchases ✨")

    purchases = session.execute("SELECT * FROM compra;")
    purchasesList = [{}]

    for purchase in purchases:
        purchasesList.append({purchase.id, purchase.precototal, purchase.status, purchase.data, purchase.formapagamento, purchase.produto[0], purchase.produto[1], purchase.produto[2], purchase.produto[3], purchase.vendedor[0], purchase.vendedor[1], purchase.usuario[0], purchase.usuario[1]})
    
    print (purchasesList)
    
    print ("----------------------------")

def readPurchase(id):
    print ("\nReading Purchase ✨")

    purchases = session.execute("SELECT * FROM compra;")
    purchaseList = [{}]

    for purchase in purchases:
        if (purchase.id == id):
            purchaseList = {purchase.id, purchase.precototal, purchase.status, purchase.data, purchase.formapagamento, purchase.produto[0], purchase.produto[1], purchase.produto[2], purchase.produto[3], purchase.vendedor[0], purchase.vendedor[1], purchase.usuario[0], purchase.usuario[1]}
    
    print (purchaseList)
    
    print ("----------------------------")

## favs ☁
def readUserFavs(email):
    print ("\nReading User's Fav ✨")

    users = session.execute("SELECT * FROM usuario;")

    for user in users:
        if (user.email == email):
            favs = user.fav

            index = 0

            while (index < len(favs)):

                print (f'Id: {favs[index]}')
                print (f'Name: {favs[index + 1]}')
                print (f'Price: {favs[index + 2]}')
                print (f'Vendor Email: {favs[index + 3]}')
                print (f'Vendor Name: {favs[index + 4]}')

                print ("---")

                index += 5

    print ("----------------------------")

# function: UPDATE
## users ☁
def updateUser(email, nome, cpf, endereco):
    print ("\nUpdating User ✨")

    users = session.execute("SELECT * FROM usuario;")

    for user in users:
        if (user.email == email):
            session.execute("UPDATE usuario SET nome = '%s', cpf = '%s', endereco = ['%s', '%s', '%s', '%s'] WHERE email = '%s'" % (nome, cpf, endereco[0], endereco[1], endereco[2], endereco[3], email))
            
            readUser(email)

## vendors ☁
def updateVendor(email, nome, cpf, endereco):
    print ("\nUpdating Vendor ✨")

    vendors = session.execute("SELECT * FROM vendedor;")

    for vendor in vendors:
        if (vendor.email == email):
            session.execute("UPDATE vendedor SET nome = '%s', cpf = '%s', endereco = ['%s', '%s', '%s', '%s'] WHERE email = '%s'" % (nome, cpf, endereco[0], endereco[1], endereco[2], endereco[3], email))
            
            readVendor(email)

## products ☁
def updateProduct(id, nome, preco, quantidade, status, vendorEmail):
    print ("\nUpdating Product ✨")

    produtos = session.execute("SELECT * FROM produto;")

    vendors = session.execute("SELECT * FROM vendedor;")

    for vendor in vendors:
        if (vendor.email == vendorEmail):
            for product in produtos:
                if (product.id == id):
                    session.execute("UPDATE produto SET nome = '%s', preco = '%s', quantidade = '%s', status = '%s', vendedor = ['%s', '%s'] WHERE id = '%s'" % (nome, preco, quantidade, status, vendorEmail, vendor.nome, id))
                    
                    readProduct(id)

# function: DELETE
## users ☁
def deleteUser(email):
    print ("\nDeleting User ✨")
    
    users = session.execute("SELECT * FROM usuario;")

    for user in users:
        if (user.email == email):
            session.execute("DELETE FROM usuario WHERE email = '%s'" % email)
            
            readAllUsers()

## vendors ☁
def deleteVendor(email):
    print ("\nDeleting Vendor ✨")

    vendors = session.execute("SELECT * FROM vendedor;")

    for vendor in vendors:
        if (vendor.email == email):
            session.execute("DELETE FROM vendedor WHERE email = '%s'" % email)
            
            readAllVendors()

## products ☁
def deleteProduct(id):
    print ("\nDeleting Product ✨")

    products = session.execute("SELECT * FROM produto;")

    for product in products:
        if (product.id == id):
            session.execute("DELETE FROM produto WHERE id = '%s'" % id)
            
            readAllProducts()


# commands ✨

## insert commands ☁
###insertUser('mclaralvs@gmail.com', '111.222.333.45', ['bogota', '20', 'sjc', 'sp'], 'maria clara')
### insertVendor('mclaralvs@gmail.com', '111.222.333.45', ['bogota', '30', 'sjc', 'sp'], 'maria clara')
### insertProduct('1', 'Travesseiro', '39.99', '10', 'Disponível', 'mclaralvs@gmail.com')
### insertPurchase('1', 'Finalizada!', '26.10.2022', 'Boleto', 'Travesseiro', '2', 'mclaralvs@gmail.com', 'mclaralvs@gmail.com')
### insertFav('mclaralvs@gmail.com', 'Cama')

## read commands ☁
### readAllUsers()
### readUser('mclaralvs@gmail.com')
### readAllVendors()
### readVendor('mclaralvs@gmail.com')
### readAllProducts()
### readProduct('1')
### readAllPurchases()
### readPurchase('1')
readUserFavs('mclaralvs@gmail.com')

## update commands ☁
### updateUser('mclaralvs@gmail.com', 'mariazinha', '555.555.555.55', ['alameda', '40', 'cacapava', 'ge'])
### updateVendor('mclaralvs@gmail.com', 'mariazinha', '555.555.555.55', ['alameda', '40', 'cacapava', 'rj'])
### updateProduct('1', 'Cama', "190.99", '9', 'Disponível', 'mclaralvs@gmail.com')

## delete commands ☁
### deleteUser('mclaralvs@gmail.com')
### deleteVendor('mclaralvs@gmail.com')
### deleteProduct('1')