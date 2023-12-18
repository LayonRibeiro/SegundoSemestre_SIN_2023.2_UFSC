from cliente import Cliente
from controladorPessoas import ControladorPessoas


cliente1 = Cliente("Joao", 123)
cliente2 = Cliente("Joao", 123)

contolePessoas = ControladorPessoas()

contolePessoas.add_cliente(cliente1)
contolePessoas.add_cliente(cliente2)

print(contolePessoas.tecnicos)