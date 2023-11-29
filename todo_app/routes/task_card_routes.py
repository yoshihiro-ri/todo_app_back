from flask import Blueprint, jsonify, request,redirect
from todo_app.models import TaskCard, db,ma
from sqlalchemy import desc
from todo_app.routes.operate_db import add_entry_and_close_session,delete_entry_and_close_session
from todo_app.routes.request_utils import get_data_from_json
from flask_login import login_user, logout_user, login_required, current_user


task_card_bp= Blueprint('task_card', __name__, url_prefix='/task_card')

class TaskCardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TaskCard
        fields = ("id", "user_id", "title","card_id","order_index")  
task_card_schema = TaskCardSchema(many=True)

@task_card_bp.route('/', methods=['GET'])
def get_all_task_cards():
    user_id = current_user.id
    data = TaskCard.query.filter_by(user_id=user_id).order_by(TaskCard.order_index).all()
    return jsonify(task_card_schema.dump(data))

@task_card_bp.route('/<uuid>', methods=["GET"])
def get_task_card(uuid):
    data = TaskCard.query.filter_by(card_id=uuid).all() 
    return jsonify(task_card_schema.dump(data))

@task_card_bp.route('/', methods=['POST'])
def create_task_card():
    entry = TaskCard()
    data = get_data_from_json(request)

    entry.user_id = current_user.id
    entry.title = data["title"]
    entry.card_id = data["card_id"]

    add_entry_and_close_session(entry)

    latestData = TaskCard.query.order_by(desc(TaskCard.id)).first()   
    return redirect('/task_card/' + str(latestData.id))

@task_card_bp.route('/<uuid>', methods=['PUT'])
def update_task_card(uuid):
    entry = TaskCard.query.filter_by(card_id=uuid).first()
    data = get_data_from_json(request)
    
    if 'title' in data:
        entry.title = data['title']
    if 'order_index' in data:
        entry.order_index = data['order_index']
        
    add_entry_and_close_session(entry)

    return jsonify({'message': 'Task card updated successfully'})

@task_card_bp.route('/<uuid>', methods=['DELETE'])
def delete_task_card(uuid):
    entry = TaskCard.query.filter_by(card_id=uuid).first()
    delete_entry_and_close_session(entry)

    return jsonify({'message': 'Task card deleted successfully'})
