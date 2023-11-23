from flask import Blueprint, request, jsonify, redirect
from flask_login import login_user, logout_user, login_required, current_user
from todo_app.models import User
from todo_app import ma
from todo_app.routes.request_utils import get_data_from_json
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ("id", "name", "email", "password")  

user_schema = UserSchema(many=True)

from todo_app import login_manager


@auth_bp.route('/login', methods=['POST'])
def login():
    data = get_data_from_json(request)
    name = data.get('name')
    password = data.get('password')
    user = User.query.filter_by(name=name).first()
    if user and check_password_hash(user.password,password):
        login_user(user)
        return 'Logged in successfully.'
    else:
        return 'Invalid username or password.'

@auth_bp.route('/logout',methods=['GET'])
@login_required
def logout():
    logout_user()
    return 'Logged out successfully.'

@auth_bp.route('/check_login',methods=['GET'])
def check_login():
    if current_user.is_authenticated:
        return 'Logged in as {}'.format(current_user.name)
    else:
        return 'Not logged in'


