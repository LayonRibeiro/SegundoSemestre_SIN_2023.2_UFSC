from models.ModelMar import Mar
from views.ViewMar import ViewMar
                            

class ControllerMar:
    def __init__(self, controle_main):
        self.__mar_jogador = Mar(True)
        self.__mar_pc = Mar(False)
        self.__viewMar = ViewMar()
        self.__controlador_main =  controle_main
        self.__dificuldade = None


    def criar_mar(self, dificuldade: int):
        if dificuldade == 1:
            mar = [[0 for _ in range(5)] for _ in range(5)]
        if dificuldade == 2:
            mar = [[0 for _ in range(10)] for _ in range(10)]
        self.__dificuldade = dificuldade
        self.__mar_jogador.mar = [row[:] for row in mar]
        self.__mar_pc.mar = [row[:] for row in mar]
        self.__controlador_main.posiciona_embarcacoes_jogador()
        self.__controlador_main.posiciona_embarcacoes_pc()
        self.__controlador_main.jogar(self.__dificuldade, self.__mar_jogador.mar, self.__mar_pc.mar)

    def verifica_coordenadas(self, posicao, tamanho, letra, eh_jogador):
        colunas = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}

        if tamanho != 1:
            try:
                posicoes = posicao.split(',')
                coluna_inicial = int(colunas[posicoes[0][-1]])
                coluna_final = int(colunas[posicoes[1][-1]])
                linha_inicial = int(posicoes[0][0:-1])-1
                linha_final = int(posicoes[1][0:-1])-1
                if self.__dificuldade == 1:
                    if coluna_inicial > 4 or coluna_final > 4 or linha_inicial > 4 or linha_final > 4:
                        return False
            except:
                return False
            
            if abs(coluna_final - coluna_inicial) + 1 == tamanho:
                if coluna_final > coluna_inicial:
                    if eh_jogador:
                        mar = self.__mar_jogador.mar
                    else:
                        mar = self.__mar_pc.mar
                    for i in range(coluna_inicial, coluna_final + 1):
                        if mar[linha_inicial][i] != 0:
                            return False
                    for i in range(coluna_inicial, coluna_final + 1):
                        if mar[linha_inicial][i] == 0:
                            self.insere_coordenada(linha_inicial, i, letra, eh_jogador)
                        else:
                            return False
                else:
                    if eh_jogador:
                        mar = self.__mar_jogador.mar
                    else:
                        mar = self.__mar_pc.mar
                    for i in range(coluna_final, coluna_inicial + 1):
                        if mar[linha_inicial][i] != 0:
                            return False
                    for i in range(coluna_final, coluna_inicial + 1):
                        if mar[linha_inicial][i] == 0:
                            self.insere_coordenada(linha_inicial, i, letra, eh_jogador)
                        else:
                            return False

            elif abs(linha_final - linha_inicial) + 1 == tamanho:
                if linha_final > linha_inicial:
                    if eh_jogador:
                        mar = self.__mar_jogador.mar
                    else:
                        mar = self.__mar_pc.mar
                    for i in range(linha_inicial, linha_final + 1):
                        if mar[i][coluna_inicial] != 0:
                            return False
                    for i in range(linha_inicial, linha_final + 1):
                        if mar[i][coluna_inicial] == 0:
                            self.insere_coordenada(i, coluna_inicial, letra, eh_jogador)
                        else:
                            return False
                else:
                    if eh_jogador:
                        mar = self.__mar_jogador.mar
                    else:
                        mar = self.__mar_pc.mar
                    for i in range(linha_final, linha_inicial + 1):
                        if mar[i][coluna_inicial] != 0:
                            return False
                    for i in range(linha_final, linha_inicial + 1):
                        if mar[i][coluna_inicial] == 0:
                            self.insere_coordenada(i, coluna_inicial, letra, eh_jogador)
                        else:
                            return False
            else:
                return False
        else:
            coluna = int(colunas[posicao[-1]])
            linha = int(posicao[0:-1])-1
            if self.__dificuldade == 1:
                if coluna > 4 or linha > 4:
                    return False
            if eh_jogador:
                mar = self.__mar_jogador.mar
            else:
                mar = self.__mar_pc.mar
            if mar[linha][coluna] == 0:
                return self.insere_coordenada(linha, coluna, letra, eh_jogador)
            else:
                return False
            
        return True
                

    def insere_coordenada(self, linha, coluna, letra, eh_jogador):
        if eh_jogador:
            self.__mar_jogador.mar[linha][coluna] = letra
        else:
            self.__mar_pc.mar[linha][coluna] = letra
        return True
    
    def ve_mar_jogador(self):
        self.__viewMar.ver_mar(self.__mar_jogador.mar)

    def ve_mar_pc(self):
        self.__viewMar.ver_mar(self.__mar_pc.mar)
    