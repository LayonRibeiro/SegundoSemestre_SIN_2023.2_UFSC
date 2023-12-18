from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException

from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):

    def __init__(self):
        self.__elevador = None

    def subir(self) -> str:
        self.__elevador.subir()

    def descer(self) -> str:
        self.__elevador.descer()

    def entra_pessoa(self) -> str:
        self.__elevador.entra_pessoa()

    def sai_pessoa(self) -> str:
        self.__elevador.sai_pessoa()

    @property
    def elevador(self) -> Elevador:
        return self.__elevador
    def inicializar_elevador(self, andar_atual: int, total_andares_predio: int,
                             capacidade: int, total_pessoas: int):
        if not isinstance(andar_atual, int) \
                or not isinstance(total_andares_predio, int) \
                or not isinstance(capacidade, int) \
                or not isinstance(total_pessoas, int) \
                or total_pessoas > capacidade \
                or total_andares_predio < 0 or total_pessoas < 0 \
                or capacidade < 0 or andar_atual < 0 \
                or total_pessoas > capacidade \
                or andar_atual > total_andares_predio:
            raise ComandoInvalidoException
        else:
            self.__elevador = Elevador(andar_atual=andar_atual,
                                       total_andares_predio=
                                       total_andares_predio,
                                       capacidade=capacidade,
                                       total_pessoas=total_pessoas)
