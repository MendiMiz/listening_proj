from flask import Blueprint, jsonify, request

from app.service.producer.all_messages_service import producer, find_common_word

emails_blueprint = Blueprint('email', __name__)

@emails_blueprint.route('/', methods=['POST'])
def post_email():
    email = request.get_json()
    producer(email)
    return jsonify({'received': email}), 200

@emails_blueprint.route('/common', methods=['POST'])
def common_word():
    the_common_word = find_common_word()
    return jsonify({'common_word': the_common_word}), 200
