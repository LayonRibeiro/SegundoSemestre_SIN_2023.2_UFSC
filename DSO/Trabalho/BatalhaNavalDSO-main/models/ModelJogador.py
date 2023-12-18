from models.ModelPartida import Partida
from datetime import date as Date

class Jogador:
    def __init__(self, nome: str, nascimento: Date, senha: str):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__senha = senha
        self.__historico = []
        self.__pontuacao_total = 0
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @property
    def nascimento(self):
        return self.__nascimento
    
    @nascimento.setter
    def nascimento(self, nascimento: Date):
        self.__nascimento = nascimento
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def historico(self):
        return self.__historico
    
    @property
    def pontuacao_total(self):
        return self.__pontuacao_total
    
    def incluir_partida(self, partida: Partida):
        if isinstance(partida, Partida):
            self.__historico.append(partida)
            self.add_pontuacao_total_jogador(partida)

    def add_pontuacao_total_jogador(self, partida: Partida):
        self.__pontuacao_total += partida.pontuacao[0]
        print(self.__pontuacao_total)

    def incluir_historico(self, historico: list):
        if isinstance(historico, list):
            self.__historico = historico

    def incluir_pontuacao_total(self, pontuacao: int):
        self.__pontuacao_total = pontuacao