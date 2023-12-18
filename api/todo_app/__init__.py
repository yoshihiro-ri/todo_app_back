from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager

db = SQLAlchemy()
ma = Marshmallow()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['JSON_AS_ASCII'] = False
    db.init_app(app)
    ma.init_app(app)
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
