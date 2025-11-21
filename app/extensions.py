from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()
MAX_ID_LENGTH = 50

# table format
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iden = db.Column(db.String(MAX_ID_LENGTH))
    pw = db.Column(db.String(255))
    # registereed_date = db.Column(db.String(255))