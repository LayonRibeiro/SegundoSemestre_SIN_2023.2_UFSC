from ModelJogadorDao import JogadorDao
from models.ModelJogador import Jogador

jogador_dao = JogadorDao()

jogador_1 = Jogador('layon', '24/06/2002', '123')
jogador_2 = Jogador('pedro', '24/06/2002', '456')
jogador_3 = Jogador('maria', '24/06/2002', '789')

jogador_dao.add(jogador_1)
jogador_dao.add(jogador_2)
jogador_dao.add(jogador_3)