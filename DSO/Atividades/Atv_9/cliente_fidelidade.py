from cliente import Cliente


class ClienteFidelidade(Cliente):
    def __init__(self, codigo_fidelidade: int, desconto: int,
                 cpf: int, nome: str, endereco: str, telefone: int):
        super().__init__(cpf, nome, endereco, telefone)

        self.__codigo_fidelidade = codigo_fidelidade
        self.__desconto = desconto

    @property
    def codigo_fidelidade(self):
        return self.__codigo_fidelidade

    @codigo_fidelidade.setter
    def codigo_fidelidade(self, codigo):
        self.__codigo_fidelidade = codigo

    @property
    def desconto(self):
        return self.__desconto

    @desconto.setter
    def desconto(self, desconto):
        self.__desconto = desconto
