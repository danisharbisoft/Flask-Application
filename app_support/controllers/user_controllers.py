from flask import render_template, request, redirect
from ..models import db
from ..models.user import User, RegisterForm, LoginForm
from flask_app.app import bcrypt
from flask import Blueprint

# Defining the user_controllers Blueprint
user_controllers_bp = Blueprint('user_controllers', __name__)


@user_controllers_bp.route('/')  # Loads Home Page
def home():
    return render_template('auth/first.html')


@user_controllers_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        pass
    else:
        form = LoginForm()
        return render_template("/auth/login.html", form=form)


@user_controllers_bp.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')

    return render_template("/auth/register.html", form=form)
