from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list :
        return self.__clientes
    
    @property
    def tecnicos(self) -> list:
        return self.__tecnicos
    
    def add_cliente(self, nome : str, codigo : int) -> Cliente:
        add = True
        for cliente in self.__clientes:
            if codigo ==  cliente.codigo:
                add= False
                break
        if add:
            new_cliente = Cliente(nome, codigo)
            self.__clientes.append(new_cliente)
            return new_cliente
        
    def add_tecnico(self, nome : str, codigo : int) -> Tecnico:
        add = True
        for tecnico in self.__tecnicos:
            if codigo == tecnico.codigo :
                add = False
                break
        if add: 
            new_tecnico = Tecnico(nome, codigo)
            self.__tecnicos.append(new_tecnico)
            return new_tecnico
        

    def codigos_clientes(self):
        for cliente in self.__clientes:
            return cliente.codigo()
    
    def codigos_tecnicos(self):
        for tecnico in self.__tecnicos:
            return tecnico.codigo()