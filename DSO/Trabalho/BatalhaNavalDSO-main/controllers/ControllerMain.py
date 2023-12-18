import sys
from controllers.ControllerJogador import ControllerJogador
from controllers.ControllerPartida import ControllerPartida
from controllers.ControllerMar import ControllerMar
from controllers.ControllerEmbarcacao import ControllerEmbarcacao
from views.ViewMain import ViewMain

class ControllerMain:
    def __init__(self):
        self.__viewMain = ViewMain()
        self.__controllerJogador = ControllerJogador(self)
        self.__controllerPartida = ControllerPartida(self)
        self.__controllerMar = ControllerMar(self)
        self.__controllerEmbarcacao = ControllerEmbarcacao(self)
        
    # Parte de Jogador/Login/Cadastro
    def inicializa_sistema(self):
        if self.__controllerJogador.existe_jogador_cadastrado():
            self.mostra_tela_main()
        else:
            self.__controllerJogador.cadastrar(False)
            self.__controllerJogador.abre_tela()

    def logar(self):
        if self.__controllerJogador.existe_jogador_cadastrado():
            if self.__controllerJogador.logar():
                self.__controllerJogador.abre_tela()
        else:
            self.inicializa_sistema()
    
    def cadastra_jogador(self):
        self.__controllerJogador.cadastrar(False)

    def exclui_cadastro(self):
        player = self.__controllerJogador.seleciona_jogador()
        self.__controllerJogador.excluir_jogador(player, True)

    def exibe_ranking(self):
        ranking = self.__controllerJogador.exibe_ranking()
        self.__viewMain.exibe_ranking(ranking)
      
    #Parte de Criacao da Partida
    def criar_partida(self, jogador):
        self.__controllerPartida.cria_partida(jogador)

    def tamanho_mar(self, dificuldade):
        self.__controllerMar.criar_mar(dificuldade)

    def posiciona_embarcacoes_jogador(self):
        self.__controllerPartida.posiciona_embarcacoes_jogador()

    def posiciona_embarcacoes_pc(self):
        self.__controllerPartida.posiciona_embarcacoes_pc()

    def mensagens_mar_para_partida(self, msg : str): 
        self.__controllerPartida.mensagens(msg)

    def mensagem(self, mensagem):
        self.__viewMain.msg(mensagem)

    def verifica_coordenadas(self, posicoes, tamanho, letra, eh_jogador):
        return self.__controllerMar.verifica_coordenadas(posicoes, tamanho, letra, eh_jogador)
    
    def jogar(self, dificuldade, mar_jogador, mar_pc):
        return self.__controllerPartida.jogar(dificuldade, mar_jogador, mar_pc)
    
    def ve_mar_jogador(self):
        self.__controllerMar.ve_mar_jogador()

    def ve_mar_pc(self):
        self.__controllerMar.ve_mar_pc()

    def encerra_sistema(self):
        sys.exit()

    def inclui_partida(self, partida):
        self.__controllerJogador.incluir_partida(partida)
    
    def add_pontuacao_ranking(self, partida):
        self.__ranking.add(partida)
            
    def mostra_tela_main(self):
        self.__viewMain
        lista_opcoes = {1: self.logar, 2: self.cadastra_jogador, 3: self.exclui_cadastro,
                        4: self.exibe_ranking, 0: self.encerra_sistema}
        
        try:
            while True:
                lista_opcoes[self.__viewMain.tela_opcoes()]()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            self.__viewMain.erro_tela()
