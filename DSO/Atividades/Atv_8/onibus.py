from abstractOnibus import AbstractOnibus
from onibusJahCheioException import OnibusJahCheioException
from onibusJahVazioException import OnibusJahVazioException
from onibusJahLigadoException import OnibusJahLigadoException
from onibusJahDesligadoException import OnibusJahDesligadoException


class Onibus(AbstractOnibus):
    def __init__(self, capacidade: int, total_de_passageiros : int, ligado: bool):
        self.__capacidade = capacidade
        self.__total_de_passageiros = total_de_passageiros
        self.__ligado  = ligado

    def ligar(self):
        if self.__ligado == True:
            raise OnibusJahLigadoException
        else:
            self.__ligado = True
        return "Onibus Ligado!"

    def desligar(self):
        if self.__ligado == False:
            raise OnibusJahDesligadoException
        else:
            self.__ligado = False
        return "Onibus Desligado!"

    def embarca_pessoa(self):
        if self.__total_de_passageiros + 1 > self.__capacidade:
            raise OnibusJahCheioException
        else:    
            self.__total_de_passageiros += 1
        return "Passageiro Entrou"

    def desembara_pessoa(self):
        if self.__total_de_passageiros - 1 < 0:
            raise OnibusJahVazioException
        else:    
            self.__total_de_passageiros -= 1
        return "Passageiro Saiu"
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    @property
    def total_de_passageiros(self):
        return self.__total_de_passageiros
    
    @property
    def ligado(self):
        return self.__ligado
    
    @capacidade.setter
    def capacidade(self, capacidade: int):
        if capacidade > 0 and isinstance(capacidade, int):   
            self.__capacidade = capacidade