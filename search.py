from database import get_db_connection
from datetime import datetime
from geopy.distance import geodesic

def display_concerts(concerts):
    count = 1
    concert_list = []
    for concert in concerts:
        for ticket in concert['biglietti']:
            status = "sold-out" if ticket['disponibilita'] == 0 else f"disp:{ticket['disponibilita']}, {ticket['prezzo']}€"
            print(f"{count}: {concert['nome_concerto']}, {ticket['data']}, {status}, {concert['luogo']['citta']}")
            concert_list.append((concert, ticket))
            count += 1
    if not concert_list:
        print("Nessun concerto trovato.")
    return concert_list

def search_concerts_by_artist():
    db = get_db_connection()
    artist = input("Artista: ")
    concerts = db.concerts.find({"artista": artist})
    return display_concerts(concerts)

def search_concerts_by_date_range():
    db = get_db_connection()
    start_date = input("Data inizio (YYYY-MM-DD): ")
    end_date = input("Data fine (YYYY-MM-DD): ")
    
    query = {"date": {"$gte": start_date, "$lte": end_date}}
    concerts = db.concerts.find(query)
    
    return display_concerts(concerts)

def search_concerts_by_name():
    db = get_db_connection()
    concert_name = input("Nome Concerto: ")
    concerts = db.concerts.find({"nome_concerto": {"$regex": concert_name, "$options": "i"}})
    
    return display_concerts(concerts)

def search_concerts_by_location():
    db = get_db_connection()
    longitude = float(input("Longitudine: "))
    latitude = float(input("Latitudine: "))

    user_location = (latitude, longitude)

    concerts = db.concerts.find()

    nearby_concerts = []
    for concert in concerts:
        concert_location = concert["luogo"]["coordinate"]["coordinates"]
        concert_coordinates = (concert_location[1], concert_location[0])

        distance = geodesic(user_location, concert_coordinates).km
        if distance <= 7:
            nearby_concerts.append(concert)

    return display_concerts(nearby_concerts)