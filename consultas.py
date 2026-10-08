from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    # TODO: liste todos os livros com o nome do autor.
    livros = session.scalars(select(Livro)).all()

    for livro in livros:
        print(f'Livro: {livro.titulo} | Autor: {livro.autor.nome} | Status: {livro.disponivel}')
        
def listar_livros_disponiveis(session):
    # TODO: liste todos os livros com o nome do autor.
    livros = session.scalars(select(Livro).where(Livro.disponivel == True)).all()
    for livro in livros:
        print(f'Livro: {livro.titulo} | Autor: {livro.autor.nome}')
    

def livros_por_autor(session, nome_autor):
    autores = session.scalars(select(Autor)).all()

    for autor in autores:
        if autor.nome == nome_autor:
            print(f'Autor: {autor.nome}')

            for livro in autor.livros:
                print(f'Livro: {livro.titulo}')


def buscar_livros(session, trecho):
    # TODO: busque livros por parte do título.
    livros = session.scalars(select(Livro).where(Livro.titulo.like(f'%{trecho}%'))).all()
    for livro in livros:
        print(f'Livro: {livro.titulo} | Autor: {livro.autor.nome}')


def listar_autores_com_quantidade(session):
    # TODO: liste autores e a quantidade de livros de cada um.
    autores = session.scalars(select(Autor)).all()
    
    for autor in autores:
        print(f'Autor: {autor.nome} | livros: {len(autor.livros)}')



def detalhes_livro(session, titulo):
    livros = session.scalars(select(Livro).where(Livro.titulo.like(f'%{titulo}%'))).all()

    for livro in livros:
        print(f'Livro: {livro.titulo} | Ano: {livro.ano} | Autor: {livro.autor.nome} | País do autor: {livro.autor.pais}')
        
        
def emprestar_livro(session, titulo):
    livro = session.scalars(select(Livro).where(Livro.titulo == titulo)).first()

    if livro is None:
        print("Livro não encontrado.")
        return

    if not livro.disponivel:
        print("Livro não disponível.")
        return

    livro.disponivel = False
    print("livro emprestado com sucesso")
    session.commit()
    
def devolver_livro(session, titulo):
    livro = session.scalars(select(Livro).where(Livro.titulo == titulo)).first()

    if livro is None:
        print("Livro não encontrado.")
        return

    if livro.disponivel:
        print("Esse livro já está disponível.")
        return

    livro.disponivel = True
    session.commit()

    print("Livro devolvido com sucesso!")