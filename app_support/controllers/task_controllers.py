from flask import render_template, request, redirect
from ..models import db
from ..models.tasks import Todo, TaskInput
from flask import Blueprint


# Defining the task_controllers Blueprint
task_controllers_bp = Blueprint('task_controllers', __name__)


@task_controllers_bp.route("/home", methods=['GET', 'POST'])
def index():  # This function loads the homepage
    form2 = TaskInput()
    if request.method == "POST":
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/home')
        except:
            return render_template('tasks/Error.html')
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('tasks/index.html', tasks=tasks, form=form2)


@task_controllers_bp.route("/home/delete/<int:id>")
def delete(id):  # This function deletes entries
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/home')
    except:
        return render_template('tasks/Error.html')


@task_controllers_bp.route("/home/update/<int:id>", methods=['GET', 'POST'])
def update(id):  # This function updates the entries
    form2 = TaskInput()
    task_to_delete = Todo.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('tasks/update.html', task=task_to_delete, form=form2)

    else:
        updated_content = request.form['content']
        task_to_delete.content = updated_content
        try:
            db.session.commit()
            return redirect('/home')
        except:
            return render_template('tasks/Error.html')
