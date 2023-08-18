from flask import Flask
from app_support.models import db
from app_support.controllers.task_controllers import task_controllers_bp
from app_support.controllers.user_controllers import user_controllers_bp
from flask_bcrypt import Bcrypt
import secrets
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SECRET_KEY'] = secrets.token_hex(16)
bcrypt = Bcrypt(app)
db.init_app(app)
app.register_blueprint(user_controllers_bp)
app.register_blueprint(task_controllers_bp)
migrate = Migrate(app, db)
toolbar = DebugToolbarExtension(app)


if __name__ == "__main__":
    app.run(debug=True)
