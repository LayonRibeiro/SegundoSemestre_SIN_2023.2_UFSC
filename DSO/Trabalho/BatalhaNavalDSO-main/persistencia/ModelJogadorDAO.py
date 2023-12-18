from persistencia.dao import DAO
from models.ModelJogador import Jogador

class JogadorDao(DAO):
    def __init__(self):
        super().__init__('jogador.pkl')

    def add(self, jogador: Jogador): #definimos que a chave seria o nome do jogador
        super().add(jogador.nome, jogador)

    def get(self, jogador: Jogador):
        return super().get(jogador.nome)
    
    def remove(self, jogador: Jogador):
        return super().remove(jogador.nome)

    def exibe_ranking(self):
        ranking = self.get_all()
        ranking = sorted(ranking, key = lambda x: x.pontuacao_total, reverse = True)
        return ranking