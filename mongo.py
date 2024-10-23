# liverpool 6716c9b85251a927a7a2a760
# 

from pymongo import MongoClient

try:
    client = MongoClient('localhost', 27017)
    
    # Accede a la base de datos
    database = client['database_2']
    
    # Accede a las colecciones
    players_collection = database['players_db']
    teams_collection = database['teams_db']
    transfers_collection = database['transfers_db']
    
    # Función para imprimir documentos de una colección
    def print_documents(collection_name):
        documents = collection_name.find()
        print(f"\nDocuments in {collection_name.name}:")
        for document in documents: 
            print(document)
    
    # Imprimir documentos de cada colección
    print_documents(players_collection)
    print_documents(teams_collection)
    print_documents(transfers_collection)

except Exception as ex:
    print(f"Connection error: {ex}")
finally:
    print("Connection finished")
