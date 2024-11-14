import os

from dotenv import load_dotenv

from app.kafka_settings.producer import produce

load_dotenv(verbose=True)
all_messages_topic = os.environ['ALL_EMAILS_TOPIC']

def produce_all_messages(message):
    produce(
        topic=all_messages_topic,
        key=message['id'],
        value=message
    )

