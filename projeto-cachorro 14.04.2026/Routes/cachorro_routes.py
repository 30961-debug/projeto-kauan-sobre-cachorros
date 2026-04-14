from flask import Blueprint, request, jsonify
from Controllers.cachorro_controller import criar_cachorro, listar_cachorros

cachorro_bp = Blueprint('cachorro_bp', __name__)

@cachorro_bp.route('/cachorros', methods=['POST'])
def criar():
    data = request.json
    cachorro = criar_cachorro(data)
    return jsonify(cachorro), 201


@cachorro_bp.route('/cachorros', methods=['GET'])
def listar():
    cachorros = listar_cachorros()
    return jsonify(cachorros), 200