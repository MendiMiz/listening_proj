from app.db.mongo_database import emails_collection


def insert_email(email):
    email = emails_collection.insert_one(email.value)
    return email.inserted_id