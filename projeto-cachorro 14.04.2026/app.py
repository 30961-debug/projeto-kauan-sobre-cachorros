from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from database.db import db
from Routes.cachorro_routes import cachorro_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

app.register_blueprint(cachorro_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)