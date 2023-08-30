from flask import render_template, redirect
from flask_app.models import db
from flask_app.models.user import User, RegisterForm, LoginForm
from flask import Blueprint
from flask_bcrypt import Bcrypt
from flask_login import login_user, LoginManager, login_required, logout_user
import user_controllers_utils

# Defining the user_controllers Blueprint
user_controllers_bp = Blueprint('user_controllers', __name__)

# Defining an instance of the Bcrypt class which will help in hashing passwords
bcrypt = Bcrypt()

# Defining an instance of the login manager class
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@user_controllers_bp.route('/')  # Loads login/register Page
def home():
    return render_template('auth/first.html')


@user_controllers_bp.route('/login', methods=['POST', 'GET'])
def login():  # Defining login page
    form = LoginForm()
    if form.validate_on_submit():
        # Getting username from helper function
        user = user_controllers_utils.select_user(username=form.username.data)
        if user:
            # Logging the user by referencing helper function
            if user_controllers_utils.password_check_for_login(user=user, bcrypt=bcrypt,
                                                               entered_password=form.password.data):
                login_user(user)
                return redirect("/home")
            else:
                # Handling errors with helper function
                form.username.errors = user_controllers_utils.error_handling(type='password')
                return render_template("/auth/login.html", form=form)
        else:
            # Handling errors with helper function
            form.username.errors = user_controllers_utils.error_handling(type='user')
            return render_template("/auth/login.html", form=form)
    return render_template("/auth/login.html", form=form)


@user_controllers_bp.route('/register', methods=['POST', 'GET'])
def register():  # Defining Registration page

    form = RegisterForm()

    if form.validate_on_submit():
        # Handling registration process using helper function
        user_controllers_utils.create_user(bcrypt, form, db)
        return redirect('/login')

    return render_template("/auth/register.html", form=form)


@user_controllers_bp.route('/logout')
@login_required
def logout():  # Handles logout
    logout_user()
    return redirect('/')
