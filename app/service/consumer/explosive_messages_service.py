import os

from dotenv import load_dotenv

from app.kafka_settings.consumer import consume
from app.repository.consumer.explosive_repository import insert_explosive
from app.service.producer.all_messages_service import produce_explosive_emails

load_dotenv(verbose=True)
new_email_topic = os.environ['ALL_EXPLOSIVE_TOPIC']



def consume_explosive_messages():
    consume(
        topic=new_email_topic,
        function=insert_explosive
    )


