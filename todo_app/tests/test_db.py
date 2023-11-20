#models.pyからクラスをインポート
from todo_app.models import User, TaskCard, Task
#dbをインポート
from todo_app import db
# ユーザーデータの作成
user1 = User(name='User1', email='user1@example.com', password='password1')
user2 = User(name='User2', email='user2@example.com', password='password2')

# タスクカードデータの作成
task_card1 = TaskCard(user_id=user1.id, title='TaskCard1')
task_card2 = TaskCard(user_id=user2.id, title='TaskCard2')

# タスクデータの作成
task1 = Task(content='Task1', status=0, task_card_id=task_card1.id)
task2 = Task(content='Task2', status=0, task_card_id=task_card2.id)

# データベースにデータを追加
def init():
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # ユーザーがデータベースに追加された後にタスクカードを作成
    task_card1 = TaskCard(user_id=user1.id, title='TaskCard1')
    task_card2 = TaskCard(user_id=user2.id, title='TaskCard2')

    db.session.add(task_card1)
    db.session.add(task_card2)
    db.session.commit()

    # タスクカードがデータベースに追加された後にタスクを作成
    task1 = Task(content='Task1', status=0, task_card_id=task_card1.id)
    task2 = Task(content='Task2', status=0, task_card_id=task_card2.id)

    db.session.add(task1)
    db.session.add(task2)
    db.session.commit()

