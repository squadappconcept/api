import uuid

from flask import Blueprint, jsonify, request
from Crypto import Random

from models import db
from models.user import User
from models.session import Session

SESSION_ID_ENCRYPTION_KEY = 'asdf'

auth = Blueprint('auth', __name__)

def generate_session_id():
    return str(uuid.UUID(bytes=Random.get_random_bytes(16)))

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    facebook_id = data.get('facebook_id')

    if not all((name, email, facebook_id)):
        raise Exception('not all required values provided')

    user = User.query.filter_by(facebook_id=facebook_id).first()
    if not user:
        user_uuid = str(uuid.uuid4())
        user = User(
            uuid=user_uuid,
            name=name,
            email=email,
            facebook_id=facebook_id,
        )
        db.session.add(user)

    else:
        user_uuid = user.uuid

    session_id = generate_session_id()
    session = Session(
        uuid=session_id,
        user_uuid=user_uuid,
    )
    db.session.add(session)

    db.session.commit()

    return jsonify({
        'session_id': session_id,
    })

@auth.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()

    session_id = data.get('session_id')

    Session.query.filter_by(uuid=session_id).delete()
    db.session.commit()

    return jsonify({})
