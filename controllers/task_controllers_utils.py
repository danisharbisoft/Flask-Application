from flask_app.models import db
from flask_app.models.tasks import Todo, TaskInput


def order_tasks(current_user: int):
    return Todo.query.filter_by(user_id=current_user).order_by(Todo.date_created).all()


def create_new_task(task_content: str, current_user: int):
    return Todo(content=task_content, user_id=current_user)


def add_to_database(task_content: str, current_user: int):
    new_task = create_new_task(task_content, current_user)
    db.session.add(new_task)
    db.commit()


def delete_task(id: int):
    task_to_delete = select_task(id)
    db.session.delete(task_to_delete)
    db.session.commit()


def select_task(id: int):
    return Todo.query.get_or_404(id)
