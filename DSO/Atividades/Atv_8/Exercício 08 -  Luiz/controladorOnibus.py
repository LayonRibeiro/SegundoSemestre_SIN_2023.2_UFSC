from abstractControladorOnibus import AbstractControladorOnibus
from comandoInvalidoException import ComandoInvalidoException
from onibus import Onibus


class ControladorOnibus(AbstractControladorOnibus):
    def __init__(self):
        self.__onibus = Onibus(0, 0, False)

    def ligar(self):
        self.__onibus.ligar()

    def desligar(self):
        self.__onibus.desligar()

    def embarca_pessoa(self):
        self.__onibus.embarca_pessoa()

    def desembarca_pessoa(self):
        self.__onibus.desembarca_pessoa()

    @property
    def onibus(self) -> Onibus:
        return self.__onibus

    def inicializar_onibus(self, capacidade: int, total_passageiros: int, ligado: bool):
        if (isinstance(capacidade, int)
                and isinstance(total_passageiros, int)
                and isinstance(ligado, bool)
                and capacidade >= 0
                and 0 <= total_passageiros <= capacidade):
            self.__onibus = Onibus(capacidade, total_passageiros, ligado)
        else:
            raise ComandoInvalidoException
