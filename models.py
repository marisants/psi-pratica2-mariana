from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


# TODO: crie o modelo Autor.
class Autor(Base):
  __tablename__ = 'autor'
  id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
  nome: Mapped[str]
  pais: Mapped[str]
  livros: Mapped[List['Livro']] = relationship(back_populates = 'autor')
# Campos: id, nome, pais.
# Relacionamento: livros.


# TODO: crie o modelo Livro.
class Livro(Base):
  __tablename__ = 'livros'
  id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
  titulo: Mapped[str]
  ano: Mapped[int]
  autor_id: Mapped[int] = mapped_column(ForeignKey('autor.id'))
  autor: Mapped['Autor'] = relationship(back_populates = 'livros')
# Campos: id, titulo, ano, autor_id.
# Relacionamento: autor.
