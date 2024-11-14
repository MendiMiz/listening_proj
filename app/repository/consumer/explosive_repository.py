from app.db.models.devices import Devices
from app.db.models.explosive_messages import ExplosiveMessages
from app.db.models.hostage_messages import HostageMessages
from app.db.models.locations import Locations
from app.db.models.users import Users
from app.db.sql_database import session_maker


def insert_explosive(message):
    message = message.value

    inserted_user_id = insert_user(message)

    insert_location(message, inserted_user_id)

    insert_device(message, inserted_user_id)

    insert_messages(message, inserted_user_id)


def insert_user(message):
    with session_maker() as session:
        user_to_insert = Users(
            email=message['email'],
            username=message['username'],
            ip_address=message['ip_address'],
            created_at=message['created_at']
        )
        session.add(user_to_insert)
        session.commit()
        session.refresh(user_to_insert)
        return user_to_insert.id


def insert_location(message, user_id):
    with session_maker() as session:
        location_to_insert = Locations(
            latitude=message['location']['latitude'],
            longitude=message['location']['longitude'],
            city=message['location']['city'],
            country=message['location']['country'],
            user_id=user_id
        )
        session.add(location_to_insert)
        session.commit()
        session.refresh(location_to_insert)
        return location_to_insert.id


def insert_device(message, user_id):
    with session_maker() as session:
        device_to_insert = Devices(
            browser=message['device_info']['browser'],
            os=message['device_info']['os'],
            device_id=message['device_info']['device_id'],
            user_id=user_id
        )
        session.add(device_to_insert)
        session.commit()
        session.refresh(device_to_insert)
        return device_to_insert.id


def insert_messages(message, user_id):
    messages_id = []
    for sentence in message['sentences']:
        with session_maker() as session:
            sentence_to_insert = ExplosiveMessages(
                sentence=sentence,
                user_id=user_id
            )
            session.add(sentence_to_insert)
            session.commit()
            session.refresh(sentence_to_insert)
            messages_id.append(sentence_to_insert.id)
    return messages_id
