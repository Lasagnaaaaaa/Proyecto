from flask import Blueprint, render_template, request, redirect, url_for, flash  # Importa funciones de Flask
from flask_login import login_required, current_user  # Importa decoradores de autenticación
from app.forms import ArticleForm, ChangePasswordForm  # Importa formularios personalizados
from app.models import Articulo, User  # Importa modelos de la base de datos
from app import db  # Importa la base de datos

main = Blueprint('main', __name__)  # Crea el blueprint principal

@main.route('/')
def home():
    # Página de inicio
    return render_template('home.html')

@main.route('/articles')
@login_required
def list_articles():
    # Lista todos los artículos
    articles = Articulo.query.all()
    return render_template('article_list.html', articles=articles)

@main.route('/articles/create', methods=['GET', 'POST'])
@login_required
def create_article():
    # Crea un nuevo artículo
    form = ArticleForm()
    if form.validate_on_submit():
        article = Articulo(
            titulo=form.title.data,
            categoria=form.category.data,
            contenido=form.content.data,
            autor_id=current_user.id
        )
        db.session.add(article)
        db.session.commit()
        flash('¡Artículo creado exitosamente!')
        return redirect(url_for('main.dashboard'))
    return render_template('create_article.html', form=form)

@main.route('/dashboard')
@login_required
def dashboard():
    # Muestra el panel con los artículos
    if current_user.is_admin() or current_user.is_editor():
        articles = Articulo.query.all()
    else:
        articles = Articulo.query.filter_by(autor_id=current_user.id).all()
    return render_template('dashboard.html', articles=articles)

@main.route('/cambiar_password', methods=['GET', 'POST'])
@login_required
def cambiar_password():
    # Permite cambiar la contraseña del usuario
    form = ChangePasswordForm()
    if form.validate_on_submit():
        # Lógica para cambiar la contraseña
        pass
    return render_template('cambiar_password.html', form=form)

@main.route('/articles/<int:id>')
@login_required
def article_detail(id):
    # Muestra el detalle de un artículo
    article = Articulo.query.get_or_404(id)
    return render_template('article_detail.html', article=article)

@main.route('/articles/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_article(id):
    # Edita un artículo existente
    article = Articulo.query.get_or_404(id)
    form = ArticleForm(obj=article)
    if form.validate_on_submit():
        article.titulo = form.title.data
        article.categoria = form.category.data
        article.contenido = form.content.data
        db.session.commit()
        flash('¡Artículo actualizado exitosamente!')
        return redirect(url_for('main.article_detail', id=article.id))
    return render_template('create_article.html', form=form, edit=True)

@main.route('/articles/<int:id>/delete', methods=['POST'])
@login_required
def delete_article(id):
    # Elimina un artículo
    article = Articulo.query.get_or_404(id)
    # Solo permite a admin o al autor eliminar
    if current_user.role.name == 'Admin' or article.autor_id == current_user.id:
        db.session.delete(article)
        db.session.commit()
        flash('¡Artículo eliminado exitosamente!')
    else:
        flash('No tienes permiso para eliminar este artículo.')
    return redirect(url_for('main.dashboard'))

@main.route('/usuarios')
@login_required
def listar_usuarios():
    # Lista todos los usuarios
    if not current_user.is_admin():
        flash('No tienes permiso para ver los usuarios.')
        return redirect(url_for('main.dashboard'))
    usuarios = User.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

@main.route('/usuarios/<int:id>')
@login_required
def ver_usuario(id):
    # Muestra el detalle de un usuario
    usuario = User.query.get_or_404(id)
    return render_template('usuario_detail.html', usuario=usuario)

@main.route('/usuarios/<int:id>/delete', methods=['POST'])
@login_required
def eliminar_usuario(id):
    # Elimina un usuario
    usuario = User.query.get_or_404(id)
    # Solo permite a admin eliminar usuarios
    if current_user.role.name == 'Admin':
        db.session.delete(usuario)
        db.session.commit()
        flash('¡Usuario eliminado exitosamente!')
    else:
        flash('No tienes permiso para eliminar este usuario.')
    return redirect(url_for('main.listar_usuarios'))



