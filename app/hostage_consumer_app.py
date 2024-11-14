from flask import Flask
from app.service.consumer.all_messages_service import consume_emails
from app.service.consumer.hostage_messages_service import consume_hostage_messages

app = Flask(__name__)


if __name__ == '__main__':
    consume_hostage_messages()
    app.run()