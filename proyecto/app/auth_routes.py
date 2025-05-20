from flask import Blueprint, render_template, redirect, url_for, flash  # Funciones de Flask
from app.forms import LoginForm, RegisterForm  # Formularios personalizados
from app.models import db, User, Role  # Modelos de la base de datos
from flask_login import login_user, logout_user, current_user  # Funciones de autenticación

# Blueprint de autenticación: gestiona login, registro y logout
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Inicia sesión de un usuario existente si las credenciales son válidas.
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))  # Redirige al panel
        flash('Credenciales inválidas')
    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    # Registra un nuevo usuario
    form = RegisterForm()
    if form.validate_on_submit():
        role = Role.query.get(form.role.data)  # Asigna el rol seleccionado
        user = User(
            username=form.username.data,
            email=form.email.data,
            role=role
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Usuario registrado exitosamente.')
        return redirect(url_for('auth.login'))
    else:
        print(form.errors)  # Muestra errores de validación en consola
    return render_template('register.html', form=form)

@auth.route('/logout')
def logout():
    # Cierra sesión del usuario actual y redirige al login.
    logout_user()
    return redirect(url_for('auth.login'))
