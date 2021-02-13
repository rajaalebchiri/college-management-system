from flask import  request, Blueprint, Response
from flask_jwt_extended import create_access_token
from database.models import User
import datetime

users = Blueprint('users', __name__)

@users.route('/signup', methods=['POST'])
def signup():
    body = request.get_json()
    user = User(**body)
    print('i am here')
    user.hash_password()
    user.save()
    id = user.id
    return {'id': str(id)}, 200

@users.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    user = User.objects.get(email=body.get('email'))
    authorized = user.check_password(body.get('password'))
    if not authorized:
        return {'error': 'Email or password invalid'}, 401
    expires = datetime.timedelta(days=7)
    access_token = create_access_token(identity=str(user.id), expires_delta=expires)
    return {'token': access_token}, 200