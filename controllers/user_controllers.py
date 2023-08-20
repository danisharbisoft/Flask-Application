from flask import render_template, redirect
from flask_app.models import db
from flask_app.models.user import User, RegisterForm, LoginForm
from flask import Blueprint
from flask_bcrypt import Bcrypt
from flask_login import login_user, LoginManager, login_required, logout_user

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
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect("/home")
            else:
                form.username.errors = "Incorrect Password"
                return render_template("/auth/login.html", form=form)
        else:
            form.username.errors = "User Does not Exist!"
            return render_template("/auth/login.html", form=form)
    return render_template("/auth/login.html", form=form)


@user_controllers_bp.route('/register', methods=['POST', 'GET'])
def register():  # Defining Registration page

    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')

    return render_template("/auth/register.html", form=form)


@user_controllers_bp.route('/logout')
@login_required
def logout():  # Handles logout
    logout_user()
    return redirect('/')
