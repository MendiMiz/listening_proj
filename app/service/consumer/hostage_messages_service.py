import os

from dotenv import load_dotenv
from app.kafka_settings.consumer import consume
from app.repository.consumer.hostage_repository import insert_hostage
from app.service.producer.all_messages_service import produce_hostage_emails

load_dotenv(verbose=True)
new_email_topic = os.environ['ALL_HOSTAGE_TOPIC']



def consume_hostage_messages():
    consume(
        topic=new_email_topic,
        function=insert_hostage
    )