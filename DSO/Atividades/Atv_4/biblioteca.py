from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        if isinstance(livro, Livro):
            if len(self.__livros) > 0:
                cont = 0
                for i in range(len(self.__livros)):
                    if self.__livros[i].codigo == livro.codigo:
                        cont = 1
                        break
                if cont == 0:
                    self.__livros.append(livro)
                    print("Livro adicionado")
                else:
                    print("Livro já existe, não será adicionado")
            else:
                self.__livros.append(livro)
                print("Livro adicionado")

    def excluir_livro(self, livro:Livro):
        if isinstance(livro, Livro):
            for i in range(len(self.__livros)):
                if self.__livros[i].codigo == livro.codigo:
                    self.__livros.pop(i)
                    print("Livro removido")
                    break

    @property
    def livros(self):
        return self.__livros