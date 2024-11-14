from dotenv import load_dotenv
from app.kafka_settings.consumer import consume
import os

from app.repository.consumer.all_messages_repository import insert_email

load_dotenv(verbose=True)
new_email_topic = os.environ['ALL_EMAILS_TOPIC']

def consume_emails():
    consume(
        topic=new_email_topic,
        function=insert_email
    )





