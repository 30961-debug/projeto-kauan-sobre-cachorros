from models.cachorro_model import Cachorro
from database.db import db

def criar_cachorro(data):
    cachorro = Cachorro(
        nome=data['nome'],
        raca=data['raca'],
        idade=data['idade']
    )

    db.session.add(cachorro)
    db.session.commit()

    return cachorro.to_dict()


def listar_cachorros():
    cachorros = Cachorro.query.all()
    return [c.to_dict() for c in cachorros]