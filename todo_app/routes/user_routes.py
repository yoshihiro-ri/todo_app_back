from flask import Blueprint, jsonify, request, redirect
from sqlalchemy import desc
from todo_app.models import User  # モデルのインポート
from todo_app import db
from todo_app import ma
from todo_app.routes.operate_db import add_entry_and_close_session
from todo_app.routes.request_utils import get_data_from_json

user_bp = Blueprint('user', __name__, url_prefix='/user')

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ("id", "name", "email", "password")  

user_schema = UserSchema(many=True)

# #GET(全件参照)
@user_bp.route('/', methods=["GET"])
def get_all_users():
    data = User.query.all()
    return jsonify(user_schema.dump(data))

#GET(1件参照)
@user_bp.route('/<int:id>', methods=["GET"])
def get_user(id):
    data = User.query.filter_by(id=id).all() 
    return jsonify(user_schema.dump(data))

#POST(登録)
@user_bp.route('/', methods=["POST"])
def create_user():
    entry = User()
    data = get_data_from_json(request)
    entry.name = data["name"]
    entry.email = data["email"]
    entry.password = data["password"]
    add_entry_and_close_session(entry)

    latestData = User.query.order_by(desc(User.id)).first()   
    return redirect('/user/' + str(latestData.id))

#PUT(更新)
@user_bp.route('/<int:id>', methods=["PUT"])
def update_user(id):
    entry = User.query.get(id)
    data = get_data_from_json(request)

    entry.name = data["name"]
    entry.email = data["email"]
    entry.password = data["password"]
    add_entry_and_close_session(entry)

    return redirect('/user/' + str(id))

#DELETE(削除)
@user_bp.route('/<int:id>', methods=["DELETE"])
def delete_user(id):
    entry = User.query.get(id)
    add_entry_and_close_session(entry)

    return 'deleted', 204


