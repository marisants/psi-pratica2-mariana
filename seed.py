
from models import Autor, Livro



from models import Autor, Livro
from sqlalchemy import select


def popular_banco(session):
    # Verifica se já existem autores no banco
    if session.scalars(select(Autor)).first():
        return

    autor1 = Autor(nome='Antoine', pais='França')
    autor2 = Autor(nome='Franz Kafka', pais='República Tcheca')
    autor3 = Autor(nome='Clarice Lispector', pais='Brasil')
    autor4 = Autor(nome='Machado de Assis', pais='Brasil')
    autor5 = Autor(nome='Fiódor Dostoiévski', pais='Rússia')

    livro1 = Livro(titulo='O Pequeno Príncipe', ano=1943, autor=autor1)
    livro2 = Livro(titulo='Dom Casmurro', ano=1899, autor=autor4)
    livro3 = Livro(titulo='A Metamorfose', ano=1915, autor=autor2)
    livro4 = Livro(titulo='O Processo', ano=1925, autor=autor2)
    livro5 = Livro(titulo='Noites Brancas', ano=1848, autor=autor5)
    livro6 = Livro(titulo='A Hora da Estrela', ano=1977, autor=autor3)

    session.add_all([
        autor1, autor2, autor3, autor4, autor5,
        livro1, livro2, livro3, livro4, livro5, livro6
    ])

    session.commit()