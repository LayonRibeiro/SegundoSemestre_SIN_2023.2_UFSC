from abc import ABC, abstractmethod
from figura import Figura


class Quadrado(Figura):
    def __init__(self, nome, lado):
        super().__init__(nome)
        self.lado = lado

    def desenhe(self):
        print(super().desenhe(), "lado x lado", str(self.lado * self.lado))
