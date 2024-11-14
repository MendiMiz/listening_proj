from flask import Flask

from app.service.consumer.explosive_messages_service import consume_explosive_messages

app = Flask(__name__)


if __name__ == '__main__':
    consume_explosive_messages()
    app.run()