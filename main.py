from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from search import *
from purchase import *

uri = "mongodb+srv://bruno:solo0182@rogic-cluster-free.tqzezwa.mongodb.net/?retryWrites=true&w=majority&appName=Rogic-cluster-free"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def main_menu():
    while True:
        print("Trova i tuoi concerti preferiti:")
        print("1: Per Artista")
        print("2: Per Nome Concerto")
        print("3: Per Intervallo di Date")
        print("4: Per Vicinanza")
        print("5: Esci")
        choice = input("> ")
        
        if choice == '1':
            concert_list = search_concerts_by_artist()
        elif choice == '2':
            concert_list = search_concerts_by_name()
        elif choice == '3':
            concert_list = search_concerts_by_date_range()
        elif choice == '4':
            concert_list = search_concerts_by_location()
        elif choice == '5':
            break
        else:
            print("Scelta non valida, riprova.")
            continue
        
        if not concert_list:
            continue

        concert_number = int(input("Seleziona il numero del concerto per acquistare i biglietti: "))
        if 1 <= concert_number <= len(concert_list):
            selected_concert, selected_ticket = concert_list[concert_number - 1]
            print(f"Hai selezionato: {selected_concert['nome_concerto']}, {selected_ticket['data']}, {selected_ticket['prezzo']}€")
            num_tickets = int(input("Quanti biglietti? "))
            buy_ticket(selected_concert, selected_ticket, num_tickets)
        else:
            print("Numero del concerto non valido.")

if __name__ == "__main__":
    main_menu()