import pymongo
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://bruno:solo0182@rogic-cluster-free.tqzezwa.mongodb.net/?retryWrites=true&w=majority&appName=Rogic-cluster-free"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def get_db_connection():
    db = client["project_mongo"]
    return db

def import_data(file_path):
    db = get_db_connection()
    with open(file_path, 'r') as file:
        data = json.load(file)
        db.concerts.insert_many(data)
        db.concerts.create_index([("luogo.coordinate", pymongo.GEOSPHERE)])