from datetime import datetime
from . import db


class Todo(db.Model):  # Initialising model
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=True)
    date_created = db.Column(db.String(5), default=datetime.utcnow().strftime('%Y-%m-%d | %H:%M'))


def __repr__(self):
    return '<Task %r>' % self.id
