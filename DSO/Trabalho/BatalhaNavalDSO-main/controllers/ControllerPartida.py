import random

from views.ViewPartida import ViewPartida
from models.ModelPartida import Partida

class ControllerPartida:
    def __init__(self, controle_main):
        self.__partida = Partida()
        self.__view_partida = ViewPartida()
        self.__controlador_main =  controle_main
        self.__lista_de_barcos =    [
                                        { 'tipo': 'PORTA-AVIÕES', 'quantidade': 1, 'tamanho': 4 },
                                        { 'tipo': 'FRAGATAS'    , 'quantidade': 2, 'tamanho': 3 },
                                        { 'tipo': 'SUBMARINOS'  , 'quantidade': 2, 'tamanho': 2 },
                                        { 'tipo': 'BOTES'       , 'quantidade': 3, 'tamanho': 1 }
                                    ]

    def cria_partida(self, jogador):
        self.__partida = Partida()
        self.__partida.lista_de_disparos = []
        self.__partida.pontuacao = [0,0]
        self.__partida.jogador = jogador
        dificuldade = self.__view_partida.tamanho_mar()
        self.__controlador_main.tamanho_mar(dificuldade)
       
    def posiciona_embarcacoes_jogador(self):
        self.__view_partida.observacoes()

        for barcos in self.__lista_de_barcos:
            tipo = barcos['tipo']
            qntd = barcos['quantidade']
            tamanho = barcos['tamanho']

            i = 1
            while i <= qntd:
                posicao = self.__view_partida.pegar_coordenadas(i, qntd, tipo, tamanho)
                if self.__controlador_main.verifica_coordenadas(posicao, tamanho, tipo[0], True):
                    i += 1
                    self.__controlador_main.ve_mar_jogador()
                    continue
                else:
                    self.__view_partida.erro_inserir_coordenadas_embarcacao()
                    continue

    def posiciona_embarcacoes_pc(self):
        for barco in self.__lista_de_barcos:
            tipo = barco['tipo']
            qntd = barco['quantidade']
            tamanho = barco['tamanho']

            i = 1
            while i <= qntd:
                if tamanho == 1:
                    numero_aleatorio = random.randint(1, 10)
                    letra_aleatoria = random.choice("ABCDEFGHIJ")
                    posicao = str(numero_aleatorio) + letra_aleatoria
                else:
                    numero_aleatorio1 = random.randint(1, 10)
                    letra_aleatoria1 = random.choice("ABCDEFGHIJ")
                    numero_aleatorio2 = random.randint(1, 10)
                    letra_aleatoria2 = random.choice("ABCDEFGHIJ")
                    posicao = str(numero_aleatorio1) + letra_aleatoria1 + ',' + str(numero_aleatorio2) + letra_aleatoria2
                if self.__controlador_main.verifica_coordenadas(posicao, tamanho, tipo[0], False):
                    i += 1
                    continue
                else:
                    continue

    def jogar(self, dificuldade, mar_jogador, mar_pc):
        colunas = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}
        acertos_jogador = 0
        acertos_computador = 0
        vez = 1
        continua = True
        if dificuldade == 1:
            mar = [[0 for _ in range(5)] for _ in range(5)]
        if dificuldade == 2:
            mar = [[0 for _ in range(10)] for _ in range(10)]
        mar_exibicao_computador = [row[:] for row in mar]   
        mar_exibicao_jogador = [row[:] for row in mar]
        while continua:
            try:
                # JOGADOR
                if vez == 1: 
                    posicao = self.__view_partida.fazer_jogada()
                    coluna = int(colunas[posicao[-1]])
                    linha = int(posicao[0:-1])-1
                    if dificuldade == 1:
                        if coluna > 4 or linha > 4:
                            self.__view_partida.erro_ao_jogar()
                            continue
                    if 9 < linha < -1:
                        self.__view_partida.erro_ao_jogar()
                        continue
                    if mar_pc[linha][coluna] != 0:
                        letra = mar_pc[linha][coluna]
                        if mar_exibicao_computador[linha][coluna] == 0:
                            acertos_jogador += 1
                        mar_exibicao_computador[linha][coluna] = letra
                        self.__view_partida.acertou(posicao, letra, mar_exibicao_computador)
                        self.__partida.define_pontuacao(True, 1)
                        self.__partida.adicionar_disparo('JOGADOR ACERTOU ' + posicao)
                    else:
                        mar_exibicao_computador[linha][coluna] = 'X'
                        self.__view_partida.errou(posicao, mar_exibicao_computador)
                        self.__partida.define_pontuacao(True, -1)
                        self.__partida.adicionar_disparo('JOGADOR ERROU ' + posicao)
                        vez = 2
                    if acertos_jogador == 17:
                        self.__view_partida.ganhou()
                        continua = False
                        self.__partida.define_pontuacao(True, 50)
                        self.__view_partida.exibe_pontuacao(self.__partida.pontuacao)
                        self.__controlador_main.inclui_partida(self.__partida)
                        return
                
                if vez == 2:
                    # PC
                    if dificuldade == 1:
                        numero_aleatorio = random.randint(1, 5)
                        letra_aleatoria = random.choice("ABCDE")
                    else:
                        numero_aleatorio = random.randint(1, 10)
                        letra_aleatoria = random.choice("ABCDEFGHIJ")
                
                    posicao = str(numero_aleatorio) + letra_aleatoria
                    coluna = int(colunas[posicao[-1]])
                    linha = int(posicao[0:-1])-1
                    if mar_jogador[linha][coluna] != 0:
                        letra = mar_jogador[linha][coluna]
                        if mar_exibicao_jogador[linha][coluna] == 0:
                            acertos_computador += 1
                        mar_exibicao_jogador[linha][coluna] = letra
                        self.__view_partida.computador_acertou(posicao, letra)
                        self.__partida.define_pontuacao(False, 1)
                        self.__partida.adicionar_disparo('COMPUTADOR ACERTOU ' + posicao)
                    else:
                        mar_exibicao_jogador[linha][coluna] = 'X'
                        self.__view_partida.computador_errou(posicao)
                        self.__partida.define_pontuacao(False, -1)
                        self.__partida.adicionar_disparo('COMPUTADOR ERROU ' + posicao)
                        vez = 1
                    if acertos_computador == 17:
                        self.__view_partida.perdeu()
                        continua = False
                        self.__partida.define_pontuacao(False, 50)
                        self.__view_partida.exibe_pontuacao(self.__partida.pontuacao)
                        self.__controlador_main.inclui_partida(self.__partida)
                        return

            except Exception as e:
                print(f"Ocorreu um erro: {e}")
                self.__view_partida.erro_ao_jogar()
                continue

    def mensagens(self, mensagem):
        self.__view_partida.mensagens(mensagem)
