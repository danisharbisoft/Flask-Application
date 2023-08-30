import secrets
import os
import sys
from flask import Flask
from flask_app.models import db
from flask_app.controllers.task_controllers import task_controllers_bp
from flask_app.controllers.user_controllers import user_controllers_bp, bcrypt, login_manager
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension

# Setting up python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Registering current project as a flask app
app = Flask(__name__)

# Registering current app within bcrypt
bcrypt.init_app(app)

# Registering the current app with the login manager
login_manager.init_app(app)

# Configuring the project with SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

# Configuring the app using a secret key for security for protection against CSRF attacks
app.config['SECRET_KEY'] = secrets.token_hex(16)

# Registering current app in db
db.init_app(app)

# Registering blueprints
app.register_blueprint(user_controllers_bp)
app.register_blueprint(task_controllers_bp)

# Running migrations
migrate = Migrate(app, db)
toolbar = DebugToolbarExtension(app)

if __name__ == "__main__":
    app.run(debug=True)
