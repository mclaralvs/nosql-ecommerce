from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable


class App:

    # Initiate the system with our credentials ✨
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    # Finish the system ✨
    def close(self):
        self.driver.close()

    # USER FUNCTIONS ✨
    # create ☁
    def createUser(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._createUser)

    @staticmethod
    def _createUser(db):
        print("\nCREATE USER ✨")

        query = (
            "CREATE (object:user { nome: $nome_user, email: $email_user, cpf: $cpf_user, rua: $rua_user, cidade: $cidade_user, estado: $estado_user, numero: $numero_user })"
        )

        nome_user = input("Insert the user's name: ")
        email_user = input("Insert the user's email: ")
        cpf_user = input("Insert the user's document number: ")
        rua_user = input("Insert the user's street: ")
        cidade_user = input("Insert the user's city: ")
        estado_user = input("Insert the user's state: ")
        numero_user = input("Insert the user's house number: ")

        result = db.run(query,
                        nome_user=nome_user,
                        email_user=email_user,
                        cpf_user=cpf_user,
                        rua_user=rua_user,
                        cidade_user=cidade_user,
                        estado_user=estado_user,
                        numero_user=numero_user
                        )

        return [{"object": row["object"]["nome"]["email"]["cpf"]["rua"]["cidade"]["estado"]["numero"]}
                for row in result]

    # read ☁
    def readUsers(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readUsers)
    
    @staticmethod
    def _readUsers(db):
        print("\nREAD ALL USERS ✨")

        query = "MATCH (u:user) RETURN u"

        result = db.run(query)
        
        return [print([row]) for row in result]

    def readUser(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readUser)

    @staticmethod
    def _readUser(db):
        print("\nREAD USER BY DOCUMENT NUMBER ✨")

        cpf_user = input("Insert the user's document number: ")

        query = "MATCH (u:user) WHERE u.cpf = $cpf_user RETURN u"

        result = db.run(query,
                        cpf_user=cpf_user
                        )

        return [print([row]) for row in result]

    # VENDOR FUNCTIONS ✨
    # create ☁
    def createVendor(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._createVendor)

    @staticmethod
    def _createVendor(db):
        print("\nCREATE VENDOR ✨")

        query = (
            "CREATE (object:vendor { nome: $nome_vendor, email: $email_vendor, cpf: $cpf_vendor, rua: $rua_vendor, cidade: $cidade_vendor, estado: $estado_vendor, numero: $numero_vendor })"
        )

        nome_vendor = input("Insert the vendor's name: ")
        email_vendor = input("Insert the vendor's email: ")
        cpf_vendor = input("Insert the vendor's document number: ")
        rua_vendor = input("Insert the vendor's street: ")
        cidade_vendor = input("Insert the vendor's city: ")
        estado_vendor = input("Insert the vendor's state: ")
        numero_vendor = input("Insert the vendor's house number: ")

        result = db.run(query,
                        nome_vendor=nome_vendor,
                        email_vendor=email_vendor,
                        cpf_vendor=cpf_vendor,
                        rua_vendor=rua_vendor,
                        cidade_vendor=cidade_vendor,
                        estado_vendor=estado_vendor,
                        numero_vendor=numero_vendor
                        )

        return [{"object": row["object"]["nome"]["email"]["cpf"]["rua"]["cidade"]["estado"]["numero"]}
                for row in result]

    # read ☁
    def readVendors(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readVendors)
    
    @staticmethod
    def _readVendors(db):
        print("\nREAD ALL VENDORS ✨")
        query = "MATCH (v:vendor) RETURN v"

        result = db.run(query)
        
        return [print([row]) for row in result]

    def readVendor(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readVendor)

    @staticmethod
    def _readVendor(db):
        print("\nREAD VENDOR BY DOCUMENT NUMBER ✨")

        cpf_vendor = input("Insert the vendor's document number: ")

        query = "MATCH (v:vendor) WHERE v.cpf = $cpf_vendor RETURN v"

        result = db.run(query,
                        cpf_vendor=cpf_vendor
                        )

        return [print([row]) for row in result]

    # PRODUCT FUNCTIONS ✨
    # create ☁
    def createProduct(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._createProduct)

    @staticmethod
    def _createProduct(db):
        print("\nCREATE PRODUCT ✨")

        query = (
            "CREATE (object:product { nome: $nome_product, preco: $preco_product, quantidade: $quantidade_product, status: $status_product, cpfVendor: $cpf_vendor })"
        )

        nome_product = input("Insert the products's name: ")
        preco_product = input("Insert the products's price: ")
        quantidade_product = input("Insert the products's quantity: ")
        status_product = input("Insert the products's status: ")
        cpf_vendor = input("Insert the vendor's document number: ")

        result = db.run(query,
                        nome_product=nome_product,
                        preco_product=preco_product,
                        quantidade_product=quantidade_product,
                        status_product=status_product,
                        cpf_vendor=cpf_vendor
                        )

        return [{"object": row["object"]["nome"]["preco"]["quantidade"]["status"]["cpfVendor"]}
                for row in result]
    
     # read ☁
    def readProducts(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readProducts)
    
    @staticmethod
    def _readProducts(db):
        print("\nREAD ALL PRODUCTS ✨")

        query = "MATCH (p:product) RETURN p"

        result = db.run(query)
        
        return [print([row]) for row in result]

    def readProduct(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readProduct)

    @staticmethod
    def _readProduct(db):
        print("\nREAD PRODUCT BY NAME ✨")

        name_product = input("Insert the product's name: ")

        query = "MATCH (p:product) WHERE p.nome = $name_product RETURN p"

        result = db.run(query,
                        name_product=name_product
                        )

        return [print([row]) for row in result]

    # PURCHASE FUNCTIONS ✨
    # create ☁
    def createPurchase(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._createPurchase)

    @staticmethod
    def _createPurchase(db):
        print("\nCREATE PURCHASE ✨")

        query = (
            "CREATE (object:purchase { status: $status_purchase, formaPagamento: $forma_pagamento, idProduct: $id_product, quantidade: $quantidade_product, cpfVendor: $cpf_vendor, cpfUser: $cpf_user })"
        )

        status_purchase = input("Insert the purchase's status: ")
        forma_pagamento = input("Insert the purchase's payment method: ")
        id_product = input("Insert the products's id: ")
        quantidade_product = input("Insert the products's quantity: ")
        cpf_vendor = input("Insert the vendor's document number: ")
        cpf_user = input("Insert the user's document number")

        result = db.run(query,
                        status_purchase=status_purchase,
                        forma_pagamento=forma_pagamento,
                        id_product=id_product,
                        quantidade_product=quantidade_product,
                        cpf_vendor=cpf_vendor,
                        cpf_user=cpf_user
                        )

        return [{"object": row["object"]["status"]["formaPagamento"]["idProduct"]["quantidade"]["cpfVendor"]["cpfUser"]}
                for row in result]

    # read ☁
    def readPurchases(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readPurchases)
    
    @staticmethod
    def _readPurchases(db):
        print("\nREAD ALL PURCHASES ✨")

        query = "MATCH (p:product) RETURN p"

        result = db.run(query)
        
        return [print([row]) for row in result]

    def readPurchase(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._readPurchase)

    @staticmethod
    def _readPurchase(db):
        print("\nREAD PURCHASES BY USER'S DOCUMENT NUMBER ✨")

        cpf_user = input("Insert the user's document number: ")

        query = "MATCH (p:purchase) WHERE p.cpfUser = $cpf_user RETURN p"

        result = db.run(query,
                        cpf_user=cpf_user
                        )

        return [print([row]) for row in result]

    # RELATIONSHIP FUNCTIONS ✨
    def createRelationshipVendorProduct(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._createRelationshipVendorProduct)

    @staticmethod
    def _createRelationshipVendorProduct(db):
        vendor_cpf = input("Insert the vendor's document number: ")
        product_name = input("Insert the product's name: ")

        query = ("MATCH (p2:vendor) WHERE p2.cpf = $vendor_cpf MATCH (p1:product) WHERE p1.nome = $product_name CREATE (p1)-[:SELLED_BY]->(p2) RETURN p1, p2")

        result = db.run(query, 
                        vendor_cpf, 
                        product_name
                        )

        return [{"p1": row["p1"]["nome"], "p2": row["p2"]["cpf"]} for row in result]

if __name__ == "__main__":
    # Credentials ✨
    uri = "neo4j+s://10c94625.databases.neo4j.io"
    user = 'neo4j'
    password = 'bQ9_lXpIpkVvoYiJK44beaRwIWu2v2vWRfa7UdSFnms'
    app = App(uri, user, password)

    # FUNCTIONS ✨
    # user ☁
    #app.createUser()
    #app.readUsers()
    #app.readUser()

    # vendor ☁
    #app.createVendor()
    #app.readVendors()
    #app.readVendor()

    # product ☁
    #app.createProduct()
    #app.readProducts()
    #app.readProduct()
        
    # purchase ☁
    #app.createPurchase()
    #app.readPurchases()
    #app.readPurchase()

    # relationships ☁
    #app.createRelationshipVendorProduct()

    app.close()