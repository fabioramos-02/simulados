from flask import Blueprint, request, jsonify
from controllers.student_controller import listar_questoes, responder_questao

student_blueprint = Blueprint('student_blueprint', __name__)

@student_blueprint.route('/aluno/questoes', methods=['GET'])
def visualizar_questoes():
    questoes = listar_questoes()
    return jsonify([{
        'id': q.id,
        'enunciado': q.enunciado,
        'alternativas': q.alternativas,
        'ano': q.ano,
        'categoria': q.categoria
    } for q in questoes])

@student_blueprint.route('/aluno/questoes/<int:questao_id>/responder', methods=['POST'])
def responder(questao_id):
    data = request.json
    resposta = data['resposta']
    resultado = responder_questao(questao_id, resposta)
    return jsonify({'correto': resultado})
