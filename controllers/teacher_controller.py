from models.question import Question
from models import db

def criar_questao(enunciado, alternativas, resposta_correta, ano, categoria):
    # Lógica para o professor criar uma nova questão
    nova_questao = Question(
        enunciado=enunciado,
        alternativas=alternativas,
        resposta_correta=resposta_correta,
        ano=ano,
        categoria=categoria
    )
    db.session.add(nova_questao)
    db.session.commit()
    return nova_questao
