# adicionar importacao
from models import db

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String(500), nullable=False)
    alternativas = db.Column(db.PickleType, nullable=False)
    resposta_correta = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
