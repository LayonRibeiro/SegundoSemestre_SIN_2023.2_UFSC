from tela import Tela
from tela_inicial import TelaInicial

telai = TelaInicial()
telai.open()

botao, valores = telai.open()

if botao == "Incluir":
    tela = Tela()
    tela.open()

print(botao)
print(valores)