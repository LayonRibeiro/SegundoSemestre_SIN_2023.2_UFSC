from cliente import Cliente
from categoriaProduto import CategoriaProduto

class Produto:
    def __init__(self, codigo: int, descricao: str, categoria_produto: CategoriaProduto, qntd: int, preco_unidade: float, cliente : Cliente):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria_produto = categoria_produto
        self.__quantidade = qntd
        self.__preco_unitario = preco_unidade
        self.__cliente = cliente 

        @property
        def codigo(self):
            return self.__codigo
        
        @codigo.setter
        def codigo (self, codigo: int):
            self.__codigo = codigo
        
        @property
        def descricao(self):
            return self.__descricao
        
        @descricao.setter
        def descricao(self, descricao: str):
            self.__descricao = descricao
        
        @property
        def categoria_produto(self):
            return self.__categoria_produto
        
        @categoria_produto.setter
        def categoria_produto(self, categoria: CategoriaProduto):
            self.__categoria_produto = categoria

        @property
        def quantidade(self):
            return self.__quantidade
        @quantidade.setter

        def quantidade(self, qntd:int):
            self.__quantidade = qntd

        @property
        def preco_unitario(self):
            return self.__preco_unitario

        @preco_unitario.setter
        def preco_unitario(self, preco_unidade :float):
            self.__preco_unitario  = preco_unidade   

        @property
        def cliente(self, cliente: Cliente):
            return self.__cliente
        
        @cliente.setter
        def cliente(self, cliente: Cliente):
            self.__cliente = cliente

    
    def preco_total(self):
        return self.__quantidade * self.__preco_unitario