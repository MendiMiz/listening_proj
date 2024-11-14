from dotenv import load_dotenv

from app.db.mongo_database import emails_collection
from app.kafka_settings.consumer import consume
import os

load_dotenv(verbose=True)
new_email_topic = os.environ['ALL_EMAILS_TOPIC']

def consume_emails():
    consume(
        topic=new_email_topic,
        function=insert_email
    )

def insert_email(email):
    email = emails_collection.insert_one(email.value)
    return email.inserted_id
