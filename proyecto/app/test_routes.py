from flask import Blueprint, request, jsonify
from app.models import db, Articulo

# Change blueprint name from 'main' to 'api'
api = Blueprint('api', __name__)

@api.route('/')  # Ambas rutas llevan al mismo lugar
@api.route('/dashboard')
def index():
    
    #Página de inicio pública (home).
    
    return '<h1>Corriendo en Modo de Prueba.</h1>'

@api.route('/articulos', methods=['GET'])
def listar_articulos():
    
    #Retorna una lista de artículos (JSON).
    
    articulos = Articulo.query.all()

    data = [
        {'id': articulo.id, 'titulo': articulo.titulo, 'contenido': articulo.contenido, 'categoria': articulo.categoria, 'fecha_publicacion': articulo.fecha_publicacion}
        for articulo in articulos
    ]
    return jsonify(data), 200


@api.route('/articulos/<int:id>', methods=['GET'])
def listar_un_articulo(id):
    
    #Retorna un solo artículo por su ID (JSON).
    
    articulo = Articulo.query.get_or_404(id)

    data = {
        'id': articulo.id,
        'titulo': articulo.titulo,
        'contenido': articulo.contenido,
        'categoria': articulo.categoria,
        'fecha_publicacion': articulo.fecha_publicacion
    }

    return jsonify(data), 200


@api.route('/articulos', methods=['POST'])
def crear_articulo():
    
    #Crea un artículo sin validación.
    #Espera JSON con 'titulo', 'contenido', 'categoria', 'fecha_publicacion'.
    
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    articulo = Articulo(
        titulo=data.get('titulo'),
        contenido=data.get('contenido'),
        categoria=data.get('categoria'),
        fecha_publicacion=data.get('fecha_publicacion')
    )

    db.session.add(articulo)
    db.session.commit()

    return jsonify({'message': 'Artículo creado', 'id': articulo.id}), 201

@api.route('/articulos/<int:id>', methods=['PUT'])
def actualizar_articulo(id):
    
    #Actualiza un artículo sin validación de permisos.
    
    articulo = Articulo.query.get_or_404(id)
    data = request.get_json()

    articulo.titulo = data.get('titulo', articulo.titulo)
    articulo.contenido = data.get('contenido', articulo.contenido)
    articulo.categoria = data.get('categoria', articulo.categoria)
    articulo.fecha_publicacion = data.get('fecha_publicacion', articulo.fecha_publicacion)

    db.session.commit()

    return jsonify({'message': 'Artículo actualizado', 'id': articulo.id}), 200

@api.route('/articulos/<int:id>', methods=['DELETE'])
def eliminar_articulo(id):
    
    #Elimina un artículo sin validación de permisos.
    
    articulo = Articulo.query.get_or_404(id)
    db.session.delete(articulo)
    db.session.commit()

    return jsonify({'message': 'Artículo eliminado', 'id': articulo.id}), 200
