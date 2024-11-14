from flask import Flask

from app.service.consumer.explosive_messages_service import consume_explosive_messeges

app = Flask(__name__)


if __name__ == '__main__':
    consume_explosive_messeges()
    app.run()