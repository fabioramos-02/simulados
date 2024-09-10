from flask import Flask
from models import db
from views.student_views import student_blueprint
from views.teacher_views import teacher_blueprint

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

# Registrar as rotas
app.register_blueprint(student_blueprint)
app.register_blueprint(teacher_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

#criar uma rota para tela de login 
app.route('/login', methods=['GET', 'POST'])
#criar uma rota para tela de cadastro
