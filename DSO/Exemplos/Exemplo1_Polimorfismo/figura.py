from abc import ABC, abstractmethod


class Figura:
    @abstractmethod
    def __init__(self, nome) :
        self.nome = nome 

    @abstractmethod
    def desenhe(self) -> str:
        return ("Desenhando " + self.nome)
