from abstractOnibus import AbstractOnibus
from onibusJahCheioException import OnibusJahCheioException
from onibusJahVazioException import OnibusJahVazioException
from onibusJahLigadoException import OnibusJahLigadoException
from onibusJahDesligadoException import OnibusJahDesligadoException


class Onibus(AbstractOnibus):

    def __init__(self, capacidade: int, total_passageiros: int, ligado: bool):
        self.__capacidade = capacidade
        self.__total_passageiros = total_passageiros
        self.__ligado = ligado

    def ligar(self):
        if self.__ligado:
            raise OnibusJahLigadoException
        else:
            self.__ligado = True
            return "Ligou"

    def desligar(self) -> str:
        if not self.__ligado:
            raise OnibusJahDesligadoException
        else:
            self.__ligado = False
            return "Desligou"

    def embarca_pessoa(self) -> str:
        if self.__total_passageiros == self.__capacidade:
            raise OnibusJahCheioException
        else:
            self.__total_passageiros += 1
            return "Embarcou"

    def desembarca_pessoa(self) -> str:
        if self.__total_passageiros == 0:
            raise OnibusJahVazioException
        else:
            self.__total_passageiros -= 1
            return "Desembarcou"

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def total_passageiros(self):
        return self.__total_passageiros

    @property
    def ligado(self):
        return self.__ligado

    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade
