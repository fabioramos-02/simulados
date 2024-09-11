from flask import render_template, request, redirect, url_for, flash
from models.user import User, db
from werkzeug.security import generate_password_hash

def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        birth_date = request.form['birth_date']
        profile = request.form['profile']
        institution = request.form.get('institution', None)

        # Hash da senha para segurança
        hashed_password = generate_password_hash(password, method='sha256')

        # Verificação para evitar duplicados
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email já registrado')
            return redirect(url_for('register'))

        # Cria um novo usuário
        new_user = User(name=name, email=email, password=hashed_password, birth_date=birth_date, profile=profile, institution=institution)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    
    return render_template('login/register.html')
