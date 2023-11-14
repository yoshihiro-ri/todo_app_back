import todo_app
from todo_app import app
from todo_app.routes import user_routes
from todo_app.routes import task_card_routes

todo_app.dont_write_bytecode = True
app.register_blueprint(user_routes.user_bp)
app.register_blueprint(task_card_routes.task_card_bp)

if __name__ == '__main__':
    app.run(debug=True)