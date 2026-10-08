from consultas import (
    buscar_livros,
    detalhes_livro,
    listar_autores_com_quantidade,
    listar_livros,
    livros_por_autor,
    listar_livros_disponiveis,
    emprestar_livro,
    devolver_livro
)
from database import criar_banco, nova_sessao
from seed import popular_banco


criar_banco()

with nova_sessao() as session:
    popular_banco(session)

    print("\nTodos os livros:")
    listar_livros(session)

    print("\nLivros de um autor:")
    livros_por_autor(session, "Franz Kafka")

    print("\nBusca por parte do título:")
    buscar_livros(session, "pequeno")

    print("\nAutores e quantidades:")
    listar_autores_com_quantidade(session)

    print("\nDetalhes de um livro:")
    detalhes_livro(session, "A metamorfose")
    
    print("\nlivros disponíveis:")
    listar_livros_disponiveis(session)
    
    print("\nemprestar livro:")
    emprestar_livro(session, 'A Metamorfose')
    
    print("\n devolver livro:")
    devolver_livro(session, 'A Metamorfose')
    
