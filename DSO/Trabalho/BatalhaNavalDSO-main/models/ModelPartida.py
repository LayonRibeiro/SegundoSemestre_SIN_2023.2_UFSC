class Partida:
    def __init__(self):
        self.__jogador = None
        self.__pontuacao = [0,0]
        self.__lista_de_disparos = []

    @property
    def pontuacao(self):
        return self.__pontuacao
    
    @pontuacao.setter
    def pontuacao(self, pontuacao):
       self.__pontuacao = pontuacao   
    
    def define_pontuacao(self, eh_jogador, ponto):
        if eh_jogador:
            self.__pontuacao[0] += ponto
        else:
            self.__pontuacao[1] += ponto

    @property
    def jogador(self):
        return self.__jogador
    
    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador   

    @property
    def lista_de_disparos(self):
        return self.__lista_de_disparos

    @lista_de_disparos.setter
    def lista_de_disparos(self, lista_de_disparos):
        self.__lista_de_disparos = lista_de_disparos   

    def adicionar_disparo(self, disparo):
        self.__lista_de_disparos.append(disparo)