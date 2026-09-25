from models import Autor, Livro


def popular_banco(session):
    # TODO: crie pelo menos 3 autores e 6 livros.
    # TODO: relacione os livros aos autores.
    # TODO: use session.add ou session.add_all e session.commit.
    
    livro1 = Livro('pequeno principe', 1943, 'Antoine')
    livro2 = Livro('dom casmurro', 1899, 'Machado de Assis')
    livro3 = Livro('A metamorfose', 1915, 'Franz Kafka')
    livro4 = Livro('o processo', 1925, 'Franz Kafka')
    livro5 = Livro('Noites brancas', 1848, 'Fiódor Dostoiévski')
    livro6 = Livro('a hora da estrela', 1977, 'Clarice Lispector')
    autor1= Autor('Antoine', 'França')
    autor2 = Autor('Franz Kafka', 'república theca')
    autor3 = Autor('Clarice Lispector', 'Brasil')
    