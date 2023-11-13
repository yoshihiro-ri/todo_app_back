import todo_app
todo_app.dont_write_bytecode = True

from todo_app import app
from todo_app import routes
#routes内のblueprintを登録する
app.register_blueprint(routes.user_bp)
if __name__ == '__main__':
    app.run(debug=True)