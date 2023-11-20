from flask import Blueprint, jsonify, request,redirect
from todo_app.models import Task, db,ma
from sqlalchemy import desc
from todo_app.routes.operate_db import add_entry_and_close_session,delete_entry_and_close_session
from todo_app.routes.request_utils import get_data_from_json

task_bp= Blueprint('task', __name__, url_prefix='/task')

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        fields = ("id", "user_id", "title")  
task_schema = TaskSchema(many=True)

@task_bp.route('/', methods=['GET'])
def get_all_tasks():
    data = Task.query.all()
    return jsonify(task_schema.dump(data))

@task_bp.route('/<int:id>', methods=["GET"])
def get_task(id):
    data = Task.query.filter_by(id=id).all() 
    return jsonify(task_schema.dump(data))

@task_bp.route('/', methods=['POST'])
def create_task():
    entry = Task()
    data = get_data_from_json(request)

    entry.user_id = data["user_id"]
    entry.title = data["title"]
    add_entry_and_close_session(entry)

    latestData = Task.query.order_by(desc(Task.id)).first()   
    return redirect('/task/' + str(latestData.id))

@task_bp.route('/<int:id>', methods=['PUT'])
def update_task(id):
    entry = Task.query.get(id)
    data = get_data_from_json(request)
    
    entry.user_id = data["user_id"]
    entry.title = data["title"]
    add_entry_and_close_session(entry)

    return redirect('/task/' + str(id))

@task_bp.route('/<int:id>', methods=['DELETE'])
def delete_task(id):
    entry = Task.query.get(id)
    delete_entry_and_close_session(entry)

    return jsonify({'message': 'Task card deleted successfully'})
