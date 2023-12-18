from abc import ABC, abstractmethod;

class ModelEmbarcacao(ABC):
    @abstractmethod
    def __init__(self, nome, tamanho, estado) -> None:
        self.__nome = nome
        self.__tamannho = tamanho
        self.__estado = estado
        self.__posicoes_ocupadas = []
    
    @property
    def nome(self):
         return self.__nome
    
    @property
    def estado(self):
         return self.__estado
    
    @estado.setter
    def estado(self, estado : str):
         self.__estado = estado
    
    @property
    def tamanho(self):
         return self.__tamannho
    
    @property
    def posicoes_ocupadas(self):
        return self.__posicoes_ocupadas
    
    def inserir_posicao(self, posicoes):
        self.__posicoes_ocupadas.append(posicoes)

    def retirar_posicao(self, posicao):    
        self.__posicoes_ocupadas.remove(posicao)

    def verifica_se_existe_embarcacao(self):
         if len(self.__posicoes_ocupadas) == 0:
              return True
         else:
              return False
         
    def afunda_embarcacao(self):
         if self.verifica_se_existe_embarcacao() == False:
            self.__estado = "Destruído"
            
    def mensagem(self):
         return