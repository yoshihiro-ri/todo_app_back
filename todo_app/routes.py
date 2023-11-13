from flask import Blueprint, jsonify, request, redirect
from sqlalchemy import desc
from todo_app.models import User  # モデルのインポート
from todo_app import db
from todo_app import ma
from IPython import embed
user_bp = Blueprint('user', __name__, url_prefix='/user')



class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
user_schema = UserSchema(many=True)

# #GET(全件参照)
@user_bp.route('/', methods=["GET"])
def get_all_users():
    print("hoge")

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
    # jsonリクエストから値取得
    json = request.get_json()
    print(json)
    if type(json) == list:
        data = json[0]
    else:
        data = json
    entry.name = data["name"]
    entry.email = data["email"]
    entry.password = data["password"]

    db.session.add(entry)
    db.session.commit()
    db.session.close()

    latestData = User.query.order_by(desc(User.id)).first()   
    return redirect('/user/' + str(latestData.id))

#PUT(更新)
@user_bp.route('/<int:id>', methods=["PUT"])
def update_user(id):
    entry = User.query.get(id)
    # jsonリクエストから値取得
    json = request.get_json()
    if type(json) == list:
        data = json[0]
    else:
        data = json
    entry.name = data["name"]
    entry.email = data["email"]
    entry.password = data["password"]
    db.session.merge(entry)
    db.session.commit()
    db.session.close()

    return redirect('/user/' + str(id))

#DELETE(削除)
@user_bp.route('/<int:id>', methods=["DELETE"])
def delete_user(id):
    entry = User.query.get(id)
    db.session.delete(entry)
    db.session.commit()    
    db.session.close()

    return 'deleted', 204

