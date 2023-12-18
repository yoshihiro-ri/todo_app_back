import todo_app
from todo_app import app
from todo_app.routes import user_routes
from todo_app.routes import task_routes
from todo_app.routes import task_card_routes
from todo_app.routes import auth
from flask_login import LoginManager
from flask_cors import CORS

login_manager = LoginManager()
login_manager.init_app(app)
todo_app.dont_write_bytecode = True
app.register_blueprint(user_routes.user_bp)
app.register_blueprint(task_card_routes.task_card_bp)
app.register_blueprint(task_routes.task_bp)

app.register_blueprint(auth.auth_bp)
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE='None'
)
CORS(app, resources={r"/*": {"origins": "https://todo-app-front-xi.vercel.app/"}}, methods=['GET', 'POST', 'PUT', 'DELETE'], allow_headers=['Content-Type', 'Authorization'], supports_credentials=True)
@app.route('/')
def home():
    return 'Hello, World!'
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-store"
    return response
@login_manager.user_loader
def load_user(user_id):
    from todo_app.models import User
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)