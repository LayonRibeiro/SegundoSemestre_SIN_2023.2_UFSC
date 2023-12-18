from abc import ABC, abstractmethod
from figura import Figura

class Circulo(Figura):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.raio = raio
    
    def desenhe(self):
        print(super().desenhe(), "raio", str(self.raio))
