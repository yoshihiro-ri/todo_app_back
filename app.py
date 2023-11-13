import todo_app
todo_app.dont_write_bytecode = True

from todo_app import app
#routes/user_routes.pyをインポート
from todo_app.routes import user_routes
#routes/usr_route.py内のblueprintをappに登録
app.register_blueprint(user_routes.user_bp)
if __name__ == '__main__':
    app.run(debug=True)