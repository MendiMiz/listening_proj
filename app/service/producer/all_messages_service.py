import os
from collections import Counter

from dotenv import load_dotenv

from app.db.models import HostageMessages, ExplosiveMessages
from app.db.sql_database import session_maker
from app.kafka_settings.producer import produce

load_dotenv(verbose=True)
all_messages_topic = os.environ['ALL_EMAILS_TOPIC']
explosive_messages_topic = os.environ['ALL_EXPLOSIVE_TOPIC']
hostage_messages_topic = os.environ['ALL_HOSTAGE_TOPIC']




def producer(message):
    if include_word('explos',message):
        produce_explosive_emails(message)
    elif include_word('hostage',message):
        produce_hostage_emails(message)
    produce_all_messages(message)

def produce_all_messages(message):
    produce(
        topic=all_messages_topic,
        key=message['id'],
        value=message
    )

def produce_explosive_emails(message):
    processed_message = change_threat_to_index_0('explos', message)
    produce(
        topic=explosive_messages_topic,
        key=processed_message['id'],
        value=processed_message
    )

def produce_hostage_emails(message):
    processed_message = change_threat_to_index_0('hostage', message)
    produce(
        topic=hostage_messages_topic,
        key=processed_message['id'],
        value=processed_message
    )


def include_word(threat, message):
    return any(threat in str(sentence) for sentence in message['sentences'])

def change_threat_to_index_0(threat, message):

    messages = message['sentences']
    for i, sentence in enumerate(messages):
        if threat.lower() in sentence.lower():
            popped = message['sentences'].pop(i)
            message['sentences'].insert(0, popped)
            break
    return message

def find_common_word():
    words = []
    with session_maker() as session:
        result = session.query(HostageMessages.sentence).union(
            session.query(ExplosiveMessages.sentence)
        ).all()
        for sentence_tuple in result:
            sentence = sentence_tuple[0]
            words.extend(sentence.split())
    words_rank = Counter(words).most_common(1)
    return words_rank




