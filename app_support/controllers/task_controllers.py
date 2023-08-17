from flask import Blueprint, render_template, request, redirect

from ..models import db
from ..models.tasks import Todo

bp = Blueprint('controllers', __name__)  # Using Blueprint for controller file


@bp.route("/", methods=['GET', 'POST'])
def index():  # This function loads the homepage
    if request.method == "POST":
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return render_template('Error.html')
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@bp.route("/delete/<int:id>")
def delete(id):  # This function deletes entries
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return render_template('Error.html')


@bp.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):  # This function updates the entries
    task_to_delete = Todo.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('update.html', task=task_to_delete)

    else:
        updated_content = request.form['content']
        task_to_delete.content = updated_content
        try:
            db.session.commit()
            return redirect('/')
        except:
            return render_template('Error.html')
