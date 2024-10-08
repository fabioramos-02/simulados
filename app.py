from flask import Flask, render_template, request, redirect, url_for, flash
from models.user import db, User  # Importe seu modelo User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secret_key'  # Defina sua chave secreta para o Flash messages
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simulados.db'

db.init_app(app)

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            return redirect(url_for('templates/login'))  # Exemplo de redirecionamento após login
        else:
            flash("Login ou senha inválidos", "error")
    
    return render_template('login.html')

# Rota de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'], method='sha256')
        birth_date = request.form['birth_date']
        profile = request.form['profile']
        institution = request.form.get('institution', None)

        # Verifique se o email já existe
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email já cadastrado", "error")
            return redirect(url_for('register'))
        
        new_user = User(name=name, email=email, password=password, birth_date=birth_date, profile=profile, institution=institution)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria o banco de dados na primeira execução
    app.run(debug=True)
