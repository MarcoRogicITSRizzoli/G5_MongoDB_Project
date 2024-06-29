from database import get_db_connection, export_data
import pymongo

def buy_ticket(concert, ticket_type, num_tickets):
    db = get_db_connection()
    for ticket in concert['biglietti']:
        if ticket['tipo'] == ticket_type and ticket['disponibilità'] >= num_tickets:
            ticket['disponibilità'] -= num_tickets
            db.concerts.update_one({"_id": concert['_id']}, {"$set": {"biglietti": concert['biglietti']}})
            print(f'Acquisto completato! Totale: {ticket['prezzo'] * num_tickets}€')
            #export_data('data/struttura.json')
            for i in range(num_tickets):
                print(f'I tuoi biglietti per un totale di {ticket['prezzo'] * num_tickets}€:')
                
            print(f'{concert['nome_concerto']}, {ticket['data']}, n.{i + 1}')
            export_data('data/struttura.json')
            
            return
        print('Biglietti non sufficienti disponibili. Sold-out.')
        return
    print('Tipo di biglietto non trovato.')

