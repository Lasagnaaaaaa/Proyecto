from flask import Flask  # Importa Flask
from flask_sqlalchemy import SQLAlchemy  # Importa SQLAlchemy para la base de datos
from flask_login import LoginManager  # Importa LoginManager para autenticación
from app.config import Config  # Importa la configuración

db = SQLAlchemy()  # Instancia global de la base de datos
login_manager = LoginManager()  # Instancia global de LoginManager
login_manager.login_view = 'auth.login'  # Vista de login por defecto

def create_app():
    # Crea la aplicación Flask y configura la carpeta de plantillas
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(Config)  # Carga la configuración

    db.init_app(app)  # Inicializa la base de datos con la app
    login_manager.init_app(app)  # Inicializa el login manager

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.routes import main
    from app.auth_routes import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    # Registrar el plano de la API con un nombre único
    from app.test_routes import api
    app.register_blueprint(api)

    return app  # Devuelve la app configurada