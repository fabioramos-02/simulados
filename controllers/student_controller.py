from models.question import Question

def listar_questoes():
    # Lógica para listar questões para o aluno
    return Question.query.all()

def responder_questao(questao_id, resposta):
    # Lógica para o aluno responder a uma questão
    questao = Question.query.get(questao_id)
    return questao.resposta_correta == resposta
