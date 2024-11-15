import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(verbose=True)

client = MongoClient(os.environ['MONGO_URL'])

db = client['listening_proj']
emails_collection = db['all_emails']
