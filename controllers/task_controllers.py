from flask import render_template, request, redirect
from flask_app.models import db
from flask_app.models.tasks import TaskInput
from flask import Blueprint
from flask_login import current_user, login_required
import task_controllers_utils

# Defining the task_controllers Blueprint
task_controllers_bp = Blueprint('task_controllers', __name__)


@task_controllers_bp.route("/home", methods=['GET', 'POST'])
@login_required
def index():  # This function loads the homepage
    form2 = TaskInput()
    if request.method == "POST":
        task_content = request.form['content']
        try:
            # using helper functions to add to database
            task_controllers_utils.add_to_database(task_content, current_user.id)
            return redirect('/home')
        except:
            return render_template('tasks/error.html')
    else:
        # using helper functions to query database
        ordered_tasks = task_controllers_utils.order_tasks(current_user.id)
        return render_template('tasks/index.html', tasks=ordered_tasks, form=form2)


@task_controllers_bp.route("/home/delete/<int:id>")
def delete(id: int):  # This function deletes entries
    try:
        # Deleting using helper functions
        task_controllers_utils.delete_task(id)
        return redirect('/home')
    except:
        return render_template('tasks/error.html')


@task_controllers_bp.route("/home/update/<int:id>", methods=['GET', 'POST'])
def update(id: int):  # This function updates the entries
    form2 = TaskInput()

    # Querying database using helper functions
    task_to_update = task_controllers_utils.select_task(id)
    if request.method == 'GET':
        form2.content.data = task_to_update.content
        return render_template('tasks/update.html', task=task_to_update, form=form2)

    else:
        updated_content = request.form['content']
        task_to_update.content = updated_content
        try:
            db.session.commit()
            return redirect('/home')
        except:
            return render_template('tasks/error.html')
