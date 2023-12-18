from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipos_de_chamados = []

    @property
    def chamados(self):
        return self.__chamados
    
    @chamados.setter
    def chamados(self, chamados: Chamado):
        self.__chamados = chamados

    @property
    def tipos_de_chamados(self):
        return self.__tipos_de_chamados

    @tipos_de_chamados.setter
    def tipos_de_chamados(self, tipos_de_chamados):
        self.__tipos_de_chamados = tipos_de_chamados

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        cont = 0
        for chamado in self.__chamados:
            if chamado.tipo == tipo:
                cont +=1
        return cont
    
    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str,
                        descricao: str, prioridade: int, tipo: TipoChamado) -> Chamado:
        add = True
        if isinstance(data, Date) and isinstance(cliente,Cliente) and isinstance(tecnico, Tecnico) and isinstance(prioridade, int) and isinstance(tipo, TipoChamado):
            for chamado in self.__chamados:
                if chamado.data == data and \
                      chamado.cliente == cliente and \
                          chamado.tecnico == tecnico and \
                              chamado.tipo == tipo:
                    add = False
            if add:
                new_chamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
                self.__chamados.append(new_chamado)
                return(new_chamado)
        
    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        add = True
        if isinstance(codigo, int):
            for tipo in self.__tipos_de_chamados:
                if tipo.codigo == codigo:
                    add = False
                    break
        if add:
            new_tipo_de_chamado = TipoChamado(codigo, nome, descricao)
            self.__tipos_de_chamados.append(new_tipo_de_chamado)