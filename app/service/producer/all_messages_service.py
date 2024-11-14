import os

from dotenv import load_dotenv

from app.kafka_settings.producer import produce

load_dotenv(verbose=True)
all_messages_topic = os.environ['ALL_EMAILS_TOPIC']
explosive_messages_topic = os.environ['ALL_EXPLOSIVE_TOPIC']
hostage_messages_topic = os.environ['ALL_HOSTAGE_TOPIC']



def producer(message):
    produce_all_messages(message)
    if include_word('explos',message):
        produce_explosive_emails(message)
    elif include_word('hostage',message):
        produce_hostage_emails(message)

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


def include_word(word, message):
    for sentence in message['sentences']:
        if sentence.lower().__contains__(word):
            return True
    return False

def change_threat_to_index_0(threat, message):
    for sentence in message['sentences']:
        if sentence.lower().__contains__(threat):
            popped = message['sentences'].pop(sentence)
            message['sentences'].insert(0, popped)
    return message

