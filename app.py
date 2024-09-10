from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'chave_secreta'  # Defina uma chave secreta para a sessão

if __name__ == '__main__':
    app.run(debug=True)

# Rota principal que redireciona para a página de login ou dashboard dependendo da sessão
@app.route('/')
def index():
    if 'user_id' in session:  # Verifique se o usuário está logado
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))  # Se não estiver logado, redireciona para login

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Aqui você implementa a lógica de autenticação
    if request.method == 'POST':
        # Verificar as credenciais do usuário
        user_id = request.form['email']  # Supondo que o login seja feito por e-mail
        session['user_id'] = user_id  # Armazena o ID do usuário na sessão
        return redirect(url_for('dashboard'))

    return render_template('login.html')  # Exibe o formulário de login

# Rota de dashboard ou página inicial do usuário
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Se o usuário não estiver logado, redireciona para login
    return render_template('dashboard.html')  # Mostra o painel do usuário logado

# Rota de logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove o usuário da sessão
    return redirect(url_for('login'))  # Redireciona para o login
