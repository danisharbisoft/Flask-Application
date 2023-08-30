from . import db
from flask_wtf import FlaskForm
from flask_login import UserMixin
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


class User(db.Model, UserMixin):  # Table with user info
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    todos = db.relationship('Todo', backref='user', lazy=True)

    def __str__(self):
        return f"{self.username} {self.password}"


class RegisterForm(FlaskForm):  # Defining registration form
    username = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=20)
        ],
        render_kw={"placeholder": "Username"}
    )

    password = PasswordField(
        validators=[
            InputRequired(),
            Length(min=4, max=20)
        ],
        render_kw={"placeholder": "Password"}
    )

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_name = User.query.filter_by(username=username.data).first()

        if existing_user_name:
            raise ValidationError('Username already exists!')


class LoginForm(FlaskForm):  # Defining login form
    username = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=20)
        ],
        render_kw={"placeholder": "Username"}
    )

    password = PasswordField(
        validators=[
            InputRequired(),
            Length(min=4, max=20)
        ],
        render_kw={"placeholder": "Password"}
    )

    submit = SubmitField('Log In')

