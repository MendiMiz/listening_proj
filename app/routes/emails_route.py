from flask import Blueprint, jsonify, request

from app.service.producer.all_messages_service import produce_all_messages

emails_blueprint = Blueprint('email', __name__)

@emails_blueprint.route('/', methods=['POST'])
def post_email():
    email = request.get_json()
    produce_all_messages(email)
    return jsonify({'received': email}), 200
