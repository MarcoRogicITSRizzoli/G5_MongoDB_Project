from database import get_db_connection
from datetime import datetime

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
    lat_prefix = input("Inserisci le prime due cifre della latitudine: ")
    lon_prefix = input("Inserisci le prime due cifre della longitudine: ")
    
    lat = float(lat_prefix)
    lon = float(lon_prefix)
    
    coordinates = [lon, lat]

    radius = 7000  # 7 km in metri
    
    concerts = db.concerts.aggregate([
        {
            "$geoNear": {
                "near": {"type": "Point", "coordinates": coordinates},
                "distanceField": "dist.calculated",
                "maxDistance": radius,
                "spherical": True
            }
        }
    ])
    
    return display_concerts(concerts)