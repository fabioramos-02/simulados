from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    profile = db.Column(db.String(20), nullable=False)
    institution = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<User {self.name}>"
