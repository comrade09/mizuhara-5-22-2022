import io
import asyncio
import os
import requests

from chizuru_mizuharaBot import MONGO_DB_URI
from pymongo import MongoClient


client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["chizuru_mizuharaBot"]
