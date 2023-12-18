from cliente import Cliente
from categoriaProduto import CategoriaProduto
from produto import Produto

pessoa = Cliente("Marina","48999708246")
cat = CategoriaProduto("Frutas")
elemento = Produto(123,"verde",cat.titulo, 4, 2.5, pessoa.nome)



print(pessoa.nome)
print(elemento.preco_total())
              