from flask import Flask
from app_support.models import db
from app_support.controllers import user_controllers_bp, task_controllers_bp
import secrets
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SECRET_KEY'] = secrets.token_hex(16)
db.init_app(app)
app.register_blueprint(user_controllers_bp)
app.register_blueprint(task_controllers_bp)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
