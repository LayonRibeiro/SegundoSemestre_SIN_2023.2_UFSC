from autor import Autor
from editora import Editora
from capitulo import Capitulo


class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__autores = []

        if isinstance(editora, Editora):
            self.__editora = editora

        self.__capitulos = []

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo


    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.__editora = editora


    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and autor not in self.__autores:
            if len(self.__autores) > 0:
                cont = 0
                for i in range(len(self.__autores)):
                    if self.__autores[i].codigo == autor.codigo:
                        cont = 1
                        break
                if cont == 0:
                        self.__autores.append(autor)
                        print("Autor adicionado")
                else:
                        print("Não é possível cadastrar autor.")
            else:
                self.__autores.append(autor)
                print("Autor adicionado")

    def excluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            for i in range(len(self.__autores)):
                if self.__autores[i].codigo == autor.codigo:
                    self.__autores.pop(i)
                    break
    @property
    def autores(self):
        return self.__autores

    def incluir_capitulo(self, capitulo: Capitulo):
        if isinstance(capitulo, Capitulo) and capitulo not in self.__capitulos:
            self.__capitulos.append(capitulo)

    def excluir_capitulo(self, capitulo : Capitulo):
        if isinstance(capitulo, Capitulo):
            for i in range(len(self.__capitulos)):
                if self.__capitulos[i].titulo == capitulo:
                    self.__capitulos.pop(i)
                    break
    
    @property
    def capitulos(self):
        return self.__capitulos
    
    def find_capitulo_by_titulo(self, titulo: str):
            cont  = 0
            for i in range(len(self.__capitulos)):
                if self.__capitulos[i].titulo == titulo:
                    cont = 1
                    return print("O número do capítulo com este título é:" ,self.__capitulos[i].numero)
                    break
                
            if cont == 0:
                print("Não existe nenhum capítulo deste livro com este título")
    