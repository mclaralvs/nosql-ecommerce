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
    def createUser(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._createUser)

    @staticmethod
    def _createUser(db):
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

    # VENDOR FUNCTIONS ✨
    # create ☁
    def createVendor(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._createVendor)

    @staticmethod
    def _createVendor(db):
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

    # PRODUCT FUNCTIONS ✨
    # create ☁
    def createProduct(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._createProduct)

    @staticmethod
    def _createProduct(db):
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

    # PURCHASE FUNCTIONS ✨
    # create ☁
    def createPurchase(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self._createPurchase)

    @staticmethod
    def _createPurchase(db):
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


if __name__ == "__main__":
    # Credentials ✨
    uri = "neo4j+s://10c94625.databases.neo4j.io"
    user = 'neo4j'
    password = 'bQ9_lXpIpkVvoYiJK44beaRwIWu2v2vWRfa7UdSFnms'
    app = App(uri, user, password)

    # FUNCTIONS ✨
    # user ☁
    #app.createUser()

    # vendor ☁
    #app.createVendor()

    # product ☁
    #app.createProduct()
        
    # purchase ☁
    app.createPurchase()

    app.close()