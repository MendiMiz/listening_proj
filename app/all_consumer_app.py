from flask import Flask
from app.service.consumer.all_messages_service import consume_emails

app = Flask(__name__)


if __name__ == '__main__':
    consume_emails()
    app.run()