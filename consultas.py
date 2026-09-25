from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    # TODO: liste todos os livros com o nome do autor.
    pass


def livros_por_autor(session, nome_autor):
    # TODO: liste os livros de um autor informado pelo nome.
    pass


def buscar_livros(session, trecho):
    # TODO: busque livros por parte do título.
    pass


def listar_autores_com_quantidade(session):
    # TODO: liste autores e a quantidade de livros de cada um.
    pass


def detalhes_livro(session, titulo):
    # TODO: mostre título, ano, autor e país do autor.
    pass
