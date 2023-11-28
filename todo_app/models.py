from todo_app import app
from todo_app import db
from todo_app import ma
from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, desc
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'User'
    id = db.Column(Integer, primary_key=True) 
    name = db.Column(String(32),nullable=False) 
    email = db.Column(String(32),nullable=False,unique=True) 
    password = db.Column(String(8),nullable=False) 
    task_cards = db.relationship('TaskCard', backref='user', cascade="all,delete")

class TaskCard(db.Model):
    __tablename__ = 'TaskCard'
    id = db.Column(Integer, primary_key=True) 
    user_id = db.Column(Integer, db.ForeignKey('User.id'), nullable=False)
    title = db.Column(String(32),nullable=False)
    tasks = db.relationship('Task', backref='task_card', cascade="all,delete")

class Task(db.Model):
    __tablename__ = 'Task'
    id = db.Column(Integer, primary_key=True) 
    content = db.Column(String(32),nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    task_card_id = db.Column(Integer, db.ForeignKey('TaskCard.id'), nullable=False)

def init():
    with app.app_context():
        db.create_all()
        #テストコードの実行
        # from todo_app.tests import test_db
        # test_db.init()

init()

