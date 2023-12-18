from circulo import Circulo
from quadrado import Quadrado
from figura import Figura

figuras = []

um_circulo =  Circulo("Circulo", 10)
um_quadrado = Quadrado("Quadrado", 25)

figuras.append(um_circulo)
figuras.append(um_quadrado)
figuras.append("Eu sou uma Figura")

for figura in figuras:
    if isinstance(figura, Figura):
        figura.desenhe()