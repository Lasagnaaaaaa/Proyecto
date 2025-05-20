from flask_login import UserMixin  # Para integración con Flask-Login
from werkzeug.security import generate_password_hash, check_password_hash  # Para manejo seguro de contraseñas
import enum  # Para enums de estado
from app import db  # Instancia de la base de datos

# Enum para el estado de los artículos
class EstadoEnum(enum.Enum):
    BORRADOR = 'Borrador'
    PUBLICADO = 'Publicado'

# Modelo de rol de usuario
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

# Modelo de usuario
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref='users')

    def set_password(self, password):
        # Guarda la contraseña encriptada
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Verifica la contraseña
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        # Retorna True si el usuario es administrador
        return self.role and self.role.name == 'Admin'

    def is_editor(self):
        # Retorna True si el usuario es editor
        return self.role and self.role.name == 'Editor'

    def is_author(self):
        # Retorna True si el usuario es autor
        return self.role and self.role.name == 'Autor'

# Modelo de artículo
class Articulo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(50), nullable=False, default='General')
    fecha_publicacion = db.Column(db.Date, default=db.func.current_timestamp())
    estado = db.Column(
        db.Enum(EstadoEnum, values_callable=lambda x: [e.value for e in x]),
        default=EstadoEnum.BORRADOR.value
    )
    autor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    autor = db.relationship('User', backref='articulos')
