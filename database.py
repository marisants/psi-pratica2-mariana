from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session


# TODO: crie a classe Base herdando de DeclarativeBase.
class Base(DeclarativeBase):
    pass

# TODO: crie a engine apontando para sqlite:///biblioteca.db.
engine = create_engine('sqlite:///biblioteca.db')

def criar_banco():
    # TODO: crie as tabelas usando Base.metadata.create_all(bind=engine).
    Base.metadata.create_all(bind=engine)


def nova_sessao():
    # TODO: devolva uma Session ligada à engine.
    session = Session(bind = engine)
    return session
    
