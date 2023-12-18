from funcionario import Funcionario
from dependente import Dependente
from cargo import Cargo


cargo1 = Cargo(1000, "gerente")
cargo2 = Cargo(500, "peão")

funcionario1 = Funcionario("Joao", "123", cargo1)
funcionario2 = Funcionario("Maria", "456", cargo2)
funcionario3 = Funcionario("Andre", "789", cargo2)

funcionario1.add_dependente("Layon", "489")
funcionario1.add_dependente("Rafael", "568")


print(funcionario1.mostra_dados())