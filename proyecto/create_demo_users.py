from app import create_app, db
from app.models import User, Role

app = create_app()
with app.app_context():
    # Busca los roles por nombre
    admin_role = Role.query.filter_by(name='Admin').first()
    autor_role = Role.query.filter_by(name='Autor').first()
    editor_role = Role.query.filter_by(name='Editor').first()

    # Crea usuarios demo solo si no existen
    if not User.query.filter_by(email='admin@example.com').first():
        admin = User(username='admin', email='admin@example.com', role=admin_role)
        admin.set_password('password')
        db.session.add(admin)

    if not User.query.filter_by(email='autor@example.com').first():
        autor = User(username='autor', email='autor@example.com', role=autor_role)
        autor.set_password('password')
        db.session.add(autor)

    if not User.query.filter_by(email='editor@example.com').first():
        editor = User(username='editor', email='editor@example.com', role=editor_role)
        editor.set_password('password')
        db.session.add(editor)

    db.session.commit()
    print("Usuarios demo creados exitosamente.")
    # Cierra la sesión de la base de datos