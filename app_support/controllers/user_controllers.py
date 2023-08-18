from flask import render_template, request, redirect
from ..models import db
from ..models.user import User, RegisterForm, LoginForm

from . import user_controllers_bp


@user_controllers_bp.route('/')  # Loads Home Page
def home():
    return render_template('auth/first.html')


@user_controllers_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "Post":
        pass
    else:
        form = LoginForm()
        return render_template("/auth/login.html", form=form)


@user_controllers_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        return redirect('/login')

    else:
        form = RegisterForm()
        return render_template("/auth/register.html", form=form)
