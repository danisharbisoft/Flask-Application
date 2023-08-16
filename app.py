from flask import Flask
from app_support.models.models import db
from app_support.controllers.controllers import bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db.init_app(app)
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)
