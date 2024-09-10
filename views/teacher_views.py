from flask import Blueprint, request, jsonify
from controllers.teacher_controller import criar_questao

teacher_blueprint = Blueprint('teacher_blueprint', __name__)

@teacher_blueprint.route('/professor/questoes', methods=['POST'])
def adicionar_questao():
    data = request.json
    questao = criar_questao(
        enunciado=data['enunciado'],
        alternativas=data['alternativas'],
        resposta_correta=data['resposta_correta'],
        ano=data['ano'],
        categoria=data['categoria']
    )
    return jsonify({'message': 'Questão criada com sucesso!', 'id': questao.id})
