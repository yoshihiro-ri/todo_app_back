from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['JSON_AS_ASCII'] = False  # 日本語を利用

    # dbとmaにアプリケーションを関連付ける
    db.init_app(app)
    ma.init_app(app)

    return app

# Flaskアプリケーションを作成
app = create_app()
#models.pyをインポート 
import todo_app.models
if __name__ == "__main__":
    app.run(debug=True)
