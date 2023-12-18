from autor import Autor
from editora import Editora
from capitulo import Capitulo
from livro import Livro
from biblioteca import Biblioteca

autor1 = Autor(1, "Machado de Assis")
editora1 = Editora(5, "Aurora")
capitulo1 = Capitulo(1, "Aquele que não sei")
biblioteca1 = Biblioteca()


livro1 = Livro(123, "Memórias Póstumas de Brás Cubas", 1881, editora1)
livro1.incluir_autor(autor1)
livro1.incluir_capitulo(capitulo1)
print(livro1.capitulos)
biblioteca1.incluir_livro(livro1)
print(livro1.autores)
print(biblioteca1.livros)
biblioteca1.excluir_livro(livro1)
print(biblioteca1.livros)

livro1.find_capitulo_by_titulo("Aquele que não sei")
