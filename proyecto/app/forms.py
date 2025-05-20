from flask_wtf import FlaskForm  # Base para formularios WTForms integrados con Flask
from wtforms import StringField, PasswordField, SelectField, SubmitField, TextAreaField  # Tipos de campos
from wtforms.validators import DataRequired, Email, Length, EqualTo  # Validadores para los campos
from app.models import Role  # Modelo de roles para el registro
from flask_wtf.file import FileField, FileAllowed  # Para campos de archivos (si los usas)

# Formulario de inicio de sesión
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])  # Campo de email
    password = PasswordField('Contraseña', validators=[DataRequired()])  # Campo de contraseña
    submit = SubmitField('Iniciar sesión')  # Botón de envío

# Formulario de registro de usuario
class RegisterForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar contraseña', validators=[
        DataRequired(), EqualTo('password', message='Las contraseñas deben coincidir')
    ])
    role = SelectField('Rol', coerce=int, choices=[])  # Selección de rol
    submit = SubmitField('Registrarse')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Carga los roles disponibles desde la base de datos
        try:
            self.role.choices = [(role.id, role.name) for role in Role.query.all()]
        except:
            self.role.choices = []

# Formulario para crear o editar un artículo
class ArticleForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(), Length(max=150)])
    categoria = StringField('Categoría', validators=[DataRequired(), Length(max=50)])
    contenido = TextAreaField('Contenido', validators=[DataRequired()])
    submit = SubmitField('Guardar artículo')

# Formulario para cambiar la contraseña
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Contraseña actual', validators=[DataRequired()])
    new_password = PasswordField('Nueva contraseña', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar nueva contraseña', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Cambiar contraseña')
