import pickle


def leitura(clientes):
    arq_clientes = open('clientes.pkl', 'rb')
    clientes = pickle.load(arq_clientes)
    print(clientes)
    arq_clientes.close()

def escrita(clientes):
    arq_clientes = open('clienets.pkl', 'wb')
    pickle.dump(clientes, arq_clientes)
    print(clientes)
    arq_clientes.close()

while True:
    leitura(clientes)
    cpf = int(input('Entre com o CPF: '))
    nome = input('Entre com o Nome: ')
    clientes[cpf] = nome


clientes[000] = 'Joao'
arq_clientes = open('clientes.pkl', 'wb')
pickle.dump(clientes, arq_clientes)
arq_clientes.close()