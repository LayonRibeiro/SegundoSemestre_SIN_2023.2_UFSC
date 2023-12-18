from dao_persistencia.dao import DAO
from models.ModelJogador import Jogador

class JogadorDao(DAO):
    def __init__(self):
        super().__init__('jogador.pkl')

    def add(self, jogador: Jogador): #definimos que a chave seria o nome do jogador
        super().add(jogador.nome)

    def get(self, key: str):
        return super().get(key)
    
    def remove(self, key):
        return super().remove(key)