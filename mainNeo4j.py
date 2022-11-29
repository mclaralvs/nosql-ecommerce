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

    # CREATE FUNCTIONS ✨
    def createUser(self):
        with self.driver.session(database="neo4j") as session:
            result = session.execute_write(self._createUser)

    @staticmethod
    def _createUser(db):
        query = (
            "CREATE (user:user { nome: $nome_user, email: $email_user, cpf: $cpf_user, rua: $rua_user, cidade: $cidade_user, estado: $estado_user, numero: $numeroz })"
        )

        nome_user = input("Insert the user name: ")  
        email_user = input("Insert the user's email: "), 
        cpf_user = input("Insert the user's document number: "), 
        rua_user = input("Insert the user's street: "), 
        cidade_user = input("Insert the user's city: "), 
        estado_user = input("Insert the user's state: "), 
        numero_user = input("Insert the user's house number: ")        

        result = db.run(query,
                nome_user=nome_user,
                email_user=email_user,
                cpf_user=cpf_user,
                rua_user=rua_user,
                cidad_usere=cidade_user,
                estado_user=estado_user,
                numero_user=numero_user
            )

        return [{"user": row["user"]["nome"]["email"]["cpf"]["rua"]["cidade"]["estado"]["numero"]}
            for row in result]


if __name__ == "__main__":
    # Credentials ✨
    uri = "neo4j+s://10c94625.databases.neo4j.io"
    user = 'neo4j'
    password = 'bQ9_lXpIpkVvoYiJK44beaRwIWu2v2vWRfa7UdSFnms'
    app = App(uri, user, password)

    # FUNTIONS ✨
    app.createUser()
    #app.find_person("Alice")
    app.close()