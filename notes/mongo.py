from django.conf import settings
from pymongo import MongoClient

def collection():
    return MongoClient(settings.MONGO_URI)[settings.MONGO_DB]['notes']
