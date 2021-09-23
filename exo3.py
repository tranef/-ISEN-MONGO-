# Import nécessaire
from pymongo import  MongoClient, GEOSPHERE
import pymongo
from pymongo.message import query
import requests

#Connexion à la base mongo
ConnectionString = "localhost:27017"
myClient = MongoClient(ConnectionString)

#Initialisation des collections
myDB=myClient['Station']

exo3_collection=myDB['Exo3']
exo3_collection.drop()
exo3_collection.create_index([("location",GEOSPHERE)])

exo2_collection=myDB['Exo2']

cursor = exo2_collection.find({"etat":"EN SERVICE"})

for doc in cursor:
    myDB['Exo3'].insert_one(doc)



lat = input("Entrer votre latitude:")
lon = input("Entrer votre longitude:")

query = {"location":{"$near": { "$geometry": {"type":"Point", "coordinates":[float(lat),float(lon)]}}}}

for doc in exo3_collection.find(query).limit(3):
    print(doc)