from flask import Flask, render_template, request, redirect, url_for, flash
from models.user import db, User  # Importe o modelo User
from werkzeug.security import generate_password_hash, check_password_hash

# Inicializando a aplicação Flask
app = Flask(__name__)
app.secret_key = 'secret_key'  # Defina sua chave secreta para mensagens Flash
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simulados.db'  # Definindo o banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o SQLAlchemy
db.init_app(app)

# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Verificar se o usuário existe
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for('dashboard'))  # Exemplo de redirecionamento após login
        else:
            flash("Login ou senha inválidos", "error")
    
    return render_template('login.html')

# Rota para a página de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'], method='sha256')
        birth_date = request.form['birth_date']
        profile = request.form['profile']
        institution = request.form.get('institution', None)

        # Verificar se o email já existe no sistema
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email já cadastrado", "error")
            return redirect(url_for('register'))
        
        # Criar um novo usuário
        new_user = User(name=name, email=email, password=password, birth_date=birth_date, profile=profile, institution=institution)
        db.session.add(new_user)
        db.session.commit()

        flash("Registro realizado com sucesso! Faça login.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')

# Exemplo de uma página de dashboard (apenas como exemplo, pode ser personalizado)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  # Supondo que você tenha um arquivo dashboard.html

# Rota inicial (home page)
@app.route('/')
def home():
    return redirect(url_for('login'))  # Redireciona para a página de login

if __name__ == '__main__':
    # Garantindo que o banco de dados é criado antes da primeira execução
    with app.app_context():
        db.create_all()  # Cria o banco de dados na primeira execução
    app.run(debug=True)
