from flask import Blueprint, jsonify, request,redirect
from todo_app.models import Task, db,ma
from sqlalchemy import desc
from todo_app.routes.operate_db import add_entry_and_close_session,delete_entry_and_close_session
from todo_app.routes.request_utils import get_data_from_json

task_bp= Blueprint('task', __name__, url_prefix='/task')

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        fields = ("id", "task_card_id", "task_id","content","order_index")
task_schema = TaskSchema(many=True)

@task_bp.route('/', methods=['GET'])
def get_all_tasks():
    data = Task.query.all()
    return jsonify(task_schema.dump(data))

@task_bp.route('/<uuid>', methods=['GET'])
def get_all_tasks_by_card_id(uuid):
    data = Task.query.filter_by(task_card_id=uuid).order_by(Task.order_index).all()
    return jsonify(task_schema.dump(data))

# @task_bp.route('/<int:id>', methods=["GET"])
# def get_task(id):
#     data = Task.query.filter_by(id=id).all() 
#     return jsonify(task_schema.dump(data))

@task_bp.route('/', methods=['POST'])
def create_task():
    entry = Task()
    data = get_data_from_json(request)

    entry.task_id = data["task_id"]
    entry.task_card_id = data["task_card_id"]
    entry.content = data["content"]
    
    add_entry_and_close_session(entry)

    latestData = Task.query.order_by(desc(Task.id)).first()   
    return redirect('/task/' + str(latestData.id))

@task_bp.route('/<uuid>', methods=['PUT'])
def update_task(uuid):
    entry = Task.query.filter_by(task_id=uuid).first()
    data = get_data_from_json(request)
    entry.order_index = data['order_index']
    
    add_entry_and_close_session(entry)

    return redirect('/task/' + str(id))

@task_bp.route('/<uuid>', methods=['DELETE'])
def delete_task(uuid):
    entry = Task.query.filter_by(task_id=uuid).first()
    delete_entry_and_close_session(entry)

    return jsonify({'message': 'Task card deleted successfully'})
