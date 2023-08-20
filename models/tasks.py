from datetime import datetime
from . import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class Todo(db.Model):  # Initialising Todo table model
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=True)
    date_created = db.Column(db.String(5), default=datetime.utcnow().strftime('%Y-%m-%d | %H:%M'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id


class TaskInput(FlaskForm):  # form model
    content = StringField(
        validators=[
            InputRequired()
        ],
        render_kw={"placeholder": "Type Task here"}
    )

    submit = SubmitField()
