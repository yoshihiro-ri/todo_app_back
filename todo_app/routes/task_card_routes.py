
from flask import Blueprint, jsonify, request,redirect
from todo_app.models import TaskCard, db,ma
from sqlalchemy import desc
from todo_app.routes.operate_db import add_entry_and_close_session
from todo_app.routes.request_utils import get_data_from_json

task_card_bp= Blueprint('task_card', __name__, url_prefix='/task_card')

class TaskCardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TaskCard
        fields = ("id", "user_id", "title")  
task_card_schema = TaskCardSchema(many=True)

@task_card_bp.route('/', methods=['GET'])
def get_all_task_cards():
    data = TaskCard.query.all()
    return jsonify(task_card_schema.dump(data))

@task_card_bp.route('/<int:id>', methods=["GET"])
def get_task_card(id):
    data = TaskCard.query.filter_by(id=id).all() 
    return jsonify(task_card_schema.dump(data))

@task_card_bp.route('/', methods=['POST'])
def create_task_card():
    entry = TaskCard()
    data = get_data_from_json(request)

    entry.user_id = data["user_id"]
    entry.title = data["title"]
    add_entry_and_close_session(entry)

    latestData = TaskCard.query.order_by(desc(TaskCard.id)).first()   
    return redirect('/task_card/' + str(latestData.id))

@task_card_bp.route('/<int:id>', methods=['PUT'])
def update_task_card(id):
    entry = TaskCard.query.get(id)
    data = get_data_from_json(request)
    
    entry.user_id = data["user_id"]
    entry.title = data["title"]
    add_entry_and_close_session(entry)

    return redirect('/task_card/' + str(id))

@task_card_bp.route('/<int:id>', methods=['DELETE'])
def delete_task_card(id):
    entry = TaskCard.query.get(id)
    add_entry_and_close_session(entry)

    return jsonify({'message': 'Task card deleted successfully'})
