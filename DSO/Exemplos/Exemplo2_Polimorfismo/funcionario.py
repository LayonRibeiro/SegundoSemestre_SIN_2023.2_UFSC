from pessoa import Pessoa
from dependente import Dependente
from cargo import Cargo

class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, cargo: Cargo):
        super().__init__(nome, cpf)
        self.dependentes = []
        self.cargo = cargo

    def add_dependente (self, nome: str, cpf: str):
        self.dependentes.append(Dependente(nome, cpf))
    
    def rem_dependente(self, cpf: str):
        for dependente in self.dependentes:
            if dependente.cpf == cpf:
                self.dependentes.remove(dependente)

    def mostra_dados(self):
        return super().mostra_dados() + self.cargo.descricao
