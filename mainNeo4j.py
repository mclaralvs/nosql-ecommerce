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

    # update ☁
    def updateUser(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._updateUser)

    @staticmethod
    def _updateUser(db):
        print("\nUPDATE USER ✨")

        cpf_user = input("Insert the user's document number: ")

        print('''\nWhat do you want to update?\n
                1 - Name
                2 - Email
                3 - Document number
                4 - Street
                5 - City
                6 - State
                7 - House number
            ''')
        
        option = input("Insert the number of the option: ")

        while int(option) < 1 or int(option) > 7:
            print("Invalid option.")
            option = input("Insert the number of the option: ")

        if option == "1": option = "nome"
        elif option == "2": option = "email"
        elif option == "3": option = "cpf"
        elif option == "4": option = "rua"
        elif option == "5": option = "cidade"
        elif option == "6": option = "estado"
        elif option == "7": option = "numero"

        new_value = input("Insert the new value: ")

        query = (
            "MATCH (u:user) WHERE u.cpf = $cpf_user SET u." +
            option + " = $new_value"
        )

        db.run(query,
               cpf_user=cpf_user,
               option=option,
               new_value=new_value
               )

    def deleteUser(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._deleteUser)

    @staticmethod
    def _deleteUser(db):
        print("\nDELETE USER ✨")

        cpf_user = input("Insert the user's document number: ")

        query = "MATCH (u:user) WHERE u.cpf = $cpf_user DETACH DELETE u"

        db.run(query, cpf_user=cpf_user)


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

    # update ☁
    def updateVendor(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._updateVendor)

    @staticmethod
    def _updateVendor(db):
        print("\nUPDATE VENDOR ✨")

        cpf_vendor = input("Insert the vendor's document number: ")

        print('''\nWhat do you want to update?\n
                1 - Name
                2 - Email
                3 - Document number
                4 - Street
                5 - City
                6 - State
                7 - House number
            ''')
        
        option = input("Insert the number of the option: ")

        while int(option) < 1 or int(option) > 7:
            print("Invalid option.")
            option = input("Insert the number of the option: ")

        if option == "1": option = "nome"
        elif option == "2": option = "email"
        elif option == "3": option = "cpf"
        elif option == "4": option = "rua"
        elif option == "5": option = "cidade"
        elif option == "6": option = "estado"
        elif option == "7": option = "numero"

        new_value = input("Insert the new value: ")

        query = (
            "MATCH (v:vendor) WHERE v.cpf = $cpf_vendor SET v." +
            option + " = $new_value"
        )

        db.run(query,
               cpf_vendor=cpf_vendor,
               option=option,
               new_value=new_value
               )

    # delete ☁
    def deleteVendor(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._deleteVendor)

    @staticmethod
    def _deleteVendor(db):
        print("\nDELETE VENDOR ✨")

        cpf_vendor = input("Insert the vendor's document number: ")

        query = "MATCH (v:vendor) WHERE v.cpf = $cpf_vendor DETACH DELETE v"

        db.run(query, cpf_vendor=cpf_vendor)


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

    # update ☁
    def updateProduct(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._updateProduct)

    @staticmethod
    def _updateProduct(db):
        print("\nUPDATE PRODUCT ✨")

        name_product = input("Insert the product's name: ")

        print('''\nWhat do you want to update?\n
                1 - Name
                2 - Preco
                3 - Quantidade
                4 - Status
            ''')
        
        option = input("Insert the number of the option: ")

        while int(option) < 1 or int(option) > 4:
            print("Invalid option.")
            option = input("Insert the number of the option: ")

        if option == "1": option = "nome"
        elif option == "2": option = "preco"
        elif option == "3": option = "quantidade"
        elif option == "4": option = "status"

        new_value = input("Insert the new value: ")

        query = (
            "MATCH (p:product) WHERE p.nome = $name_product SET p." +
            option + " = $new_value"
        )

        db.run(query,
               name_product=name_product,
               option=option,
               new_value=new_value
               )

    # delete ☁
    def deleteProduct(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self._deleteProduct)
    
    @staticmethod
    def _deleteProduct(db):
        print("\nDELETE PRODUCT ✨")

        name_product = input("Insert the product's name: ")

        query = "MATCH (p:product) WHERE p.nome = $name_product DETACH DELETE p"

        db.run(query, name_product=name_product)


    # PURCHASE FUNCTIONS ✨
    # create ☁
    def createPurchase(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._createPurchase)

    @staticmethod
    def _createPurchase(db):
        print("\nCREATE PURCHASE ✨")

        query = (
            "CREATE (object:purchase { id: $id_purchase, status: $status_purchase, formaPagamento: $forma_pagamento, nomeProduct: $nome_product, quantidade: $quantidade_product, cpfVendor: $cpf_vendor, cpfUser: $cpf_user })"
        )

        id_purchase = input("Insert the purchase's id: ")
        status_purchase = input("Insert the purchase's status: ")
        forma_pagamento = input("Insert the purchase's payment method: ")
        nome_product = input("Insert the products's nome: ")
        quantidade_product = input("Insert the products's quantity: ")
        cpf_vendor = input("Insert the vendor's document number: ")
        cpf_user = input("Insert the user's document number: ")

        result = db.run(query,
                        id_purchase=id_purchase,
                        status_purchase=status_purchase,
                        forma_pagamento=forma_pagamento,
                        nome_product=nome_product,
                        quantidade_product=quantidade_product,
                        cpf_vendor=cpf_vendor,
                        cpf_user=cpf_user
                        )

        return [{"object": row["object"]["id"]["status"]["formaPagamento"]["nomeProduct"]["quantidade"]["cpfVendor"]["cpfUser"]}
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

    # update ☁
    def updatePurchase(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._updatePurchase)

    @staticmethod
    def _updatePurchase(db):
        print("\nUPDATE PURCHASE ✨")

        id_purchase = input("Insert the purchase's id: ")

        print('''\nWhat do you want to update?\n
                1 - Payment method
                2 - Quantity
                3 - Status
            ''')
        
        option = input("Insert the number of the option: ")

        while int(option) < 1 or int(option) > 3:
            print("Invalid option.")
            option = input("Insert the number of the option: ")

        if option == "1": option = "formaPagamento"
        elif option == "2": option = "quantidade"
        elif option == "3": option = "status"

        new_value = input("Insert the new value: ")

        query = (
            "MATCH (p:purchase) WHERE p.id = $id_purchase SET p." + option +" = $new_value"
        )

        db.run(query,
                id_purchase=id_purchase, 
                option=option,
                new_value=new_value
            )

    # RELATIONSHIP FUNCTIONS ✨
    def createRelationshipVendorProduct(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._updatePurchase)

    @staticmethod
    def _updatePurchase(db):
        print("\nUPDATE PURCHASE ✨")

        id_purchase = input("Insert the purchase's id: ")

        print('''\nWhat do you want to update?\n
                1 - Payment method
                2 - Quantity
                3 - Status
            ''')

        option = input("Insert the number of the option: ")

        while int(option) < 1 or int(option) > 3:
            print("Invalid option.")
            option = input("Insert the number of the option: ")

        if option == "1":
            option = "formaPagamento"
        elif option == "2":
            option = "quantidade"
        elif option == "3":
            option = "status"

        new_value = input("Insert the new value: ")

        query = (
            "MATCH (p:purchase) WHERE p.id = $id_purchase SET p." +
            option + " = $new_value"
        )

        db.run(query,
               id_purchase=id_purchase,
               option=option,
               new_value=new_value
               )


    # RELATIONSHIP FUNCTIONS ✨
    # vendor - product ☁
    def vendorProduct(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._vendorProduct)

    @staticmethod
    def _vendorProduct(db):
        vendor_cpf = input("Insert the vendor's document number: ")
        product_name = input("Insert the product's name: ")

        query = (
            "MATCH (v:vendor) WHERE v.cpf = $vendor_cpf MATCH (p:product) WHERE p.nome = $product_name CREATE (p)-[:SELLED_BY]->(v) RETURN p, v")

        result = db.run(query,
                        vendor_cpf=vendor_cpf,
                        product_name=product_name
                        )

        return [{"p": row["p"]["nome"], "v": row["v"]["cpf"]} for row in result]

    # user - product ☁
    def userPurchase(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._userPurchase)

    @staticmethod
    def _userPurchase(db):
        user_cpf = input("Insert the user's document number: ")
        purchase_id = input("Insert the purchase's id: ")

        query = (
            "MATCH (u:user) WHERE u.cpf = $user_cpf MATCH (p:purchase) WHERE p.id = $purchase_id CREATE (u)-[:BUYS]->(p) RETURN p, u")

        result = db.run(query,
                        user_cpf=user_cpf,
                        purchase_id=purchase_id
                        )

        return [{"p": row["p"]["id"], "u": row["u"]["cpf"]} for row in result]

    # purchase - product ☁
    def purchaseProduct(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._purchaseProduct)

    @staticmethod
    def _purchaseProduct(db):
        purchase_id = input("Insert the purchase's id: ")
        product_name = input("Insert the product's name: ")

        query = (
            "MATCH (pu:purchase) WHERE pu.id = $purchase_id MATCH (p:product) WHERE p.nome = $product_name CREATE (pu)-[:CONTAINS]->(p) RETURN p, pu")

        result = db.run(query,
                        product_name=product_name,
                        purchase_id=purchase_id
                        )

        return [{"p": row["p"]["nome"], "pu": row["pu"]["id"]} for row in result]

if __name__ == "__main__":
    # Credentials ✨
    uri = "neo4j+s://10c94625.databases.neo4j.io"
    user = 'neo4j'
    password = 'bQ9_lXpIpkVvoYiJK44beaRwIWu2v2vWRfa7UdSFnms'
    app = App(uri, user, password)

    # FUNCTIONS ✨
    # user ☁
    # app.createUser()
    # app.readUsers()
    # app.readUser()
    # app.updateUser()
    # app.deleteUser()

    # vendor ☁
    # app.createVendor()
    # app.readVendors()
    # app.readVendor()
    # app.updateVendor()
    # app.deleteVendor()

    # product ☁
    # app.createProduct()
    # app.readProducts()
    # app.readProduct()
    # app.updateProduct()
    # app.deleteProduct()

    # purchase ☁
    # app.createPurchase()
    # app.readPurchases()
    # app.readPurchase()
    # app.updatePurchase()

    # relationships ☁
    # app.vendorProduct()
    # app.userPurchase()
    # app.purchaseProduct()

    app.close()