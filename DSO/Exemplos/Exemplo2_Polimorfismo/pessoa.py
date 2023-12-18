from abc import ABC, abstractmethod

class Pessoa:
    @abstractmethod
    def __init__(self, nome: str, cpf: str) :
        self.nome =  nome
        self.cpf = cpf

    def mostra_dados(self):
        return 'CPF:' + self.cpf + 'Nome: ' + self.nome
