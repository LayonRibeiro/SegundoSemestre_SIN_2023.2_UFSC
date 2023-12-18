from cliente import Cliente
from tipo_pedido import TipoPedido
from item_pedido import ItemPedido
from cliente_fidelidade import ClienteFidelidade


class Pedido():
    def __init__(self, numero: int, cliente: Cliente, tipo: TipoPedido):
        self.__numero = numero
        self.__cliente = cliente
        self.__tipo = tipo
        self.__itens = []

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def tipo(self):
        return self.__tipo

    @property
    def itens(self):
        return self.__itens

    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    '''
    Inclui um novo item na lista de itens do pedido.
    Nao deve ser possivel incluir itens duplicados (com o mesmo codigo).
    Retornar o item incluido em caso de sucesso e None em caso
    de item duplicado.
    '''
    def inclui_item_pedido(self, codigo, descricao, preco):
        for item in self.__itens:
            if item.codigo == codigo:
                return None
        item_novo = ItemPedido(codigo, descricao, preco)
        self.__itens.append(item_novo)
        return item_novo

    '''
    Exclui um item do pedido e retorna o item excluido
    Caso o item nao exista, retorne None
    '''
    def exclui_item_pedido(self, codigo):
        for item in self.__itens:
            if item.codigo == codigo:
                self.__itens.remove(item)
                return item
        return None

    '''
    Deve calcular o valor total do pedido, considerando um custo
    adicional pela distancia e fator por distancia percorrida.
    O fator da distancia varia de acordo com o tipo de pedido.
    O fator_distancia do TipoPedido deve ser multiplicado pela distancia
    e acrescido ao valor total dos itens.
    Por exemplo, se o fator_distancia for 2 e a distancia for 5,
    o total do pedido deve ser acrescido em 10.
    '''
    def calcula_valor_pedido(self, distancia: float):
        preco_itens = 0
        for item in self.__itens:
            preco_itens += item.preco_unitario

        preco_dist = self.__tipo.fator_distancia * distancia
        preco = preco_itens + preco_dist

        if isinstance(self.__cliente, ClienteFidelidade):
            preco_final = preco - (preco * self.__cliente.desconto)
            return preco_final
        else:
            return preco
