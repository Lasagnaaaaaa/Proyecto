# Sistema de Gestión de Artículos

Aplicación web desarrollada con Flask para la gestión de artículos, con autenticación de usuarios, roles y permisos.

## Características

- Registro e inicio de sesión de usuarios (roles: Admin, Autor, Editor)
- Creación, edición y eliminación de artículos
- Control de acceso basado en roles
- Administración de usuarios (solo Admin)
- API REST para gestión de artículos

## Estructura del Proyecto

```
proyecto/
  app/
    __init__.py
    models.py
    routes.py
    auth_routes.py
    forms.py
    config.py
    test_routes.py
  templates/
    ...
  pruebas/
    create_demo_users.py
    create.rest
    read.rest
    update.rest
    delete.rest
  run.py
  requirements.txt
  README.md
```

## Instalación y Puesta en Marcha

1. **Clona el repositorio** y navega al directorio `proyecto`.

2. **Instala las dependencias**  
   ```
   pip install -r requirements.txt
   ```

3. **Configura la base de datos**  
   Edita `app/config.py` si es necesario. Por defecto usa MySQL:
   ```
   mysql+pymysql://root:root@localhost/publicacion_articulos
   ```

4. **Crea la base de datos y las tablas**  
   ```
   python create_db.py
   ```

5. **Crea los usuarios demo**  
   ```
   python -m pruebas.create_demo_users
   ```

6. **Ejecuta la aplicación**  
   ```
   python run.py
   ```

7. **Accede a la app**  
   Abre [http://127.0.0.1:5000](http://127.0.0.1:5000) en tu navegador.

## Usuarios Demo

- **Admin:**  
  Correo: `admin@example.com`  
  Contraseña: `password`

- **Autor:**  
  Correo: `autor@example.com`  
  Contraseña: `password`

- **Editor:**  
  Correo: `editor@example.com`  
  Contraseña: `password`

## Endpoints de la API

- `GET /articulos` - Lista de artículos (JSON)
- `POST /articulos` - Crear artículo (JSON)
- `GET /articulos/<id>` - Obtener artículo por ID (JSON)
- `PUT /articulos/<id>` - Actualizar artículo (JSON)
- `DELETE /articulos/<id>` - Eliminar artículo

## Licencia

MIT License

---

Para más detalles, revisa el código fuente en la carpeta [`proyecto`](proyecto).
