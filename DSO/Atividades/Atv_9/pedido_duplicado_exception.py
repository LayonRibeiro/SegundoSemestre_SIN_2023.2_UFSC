

class PedidoDuplicadoException(Exception):
    def __init__(self):
        super().__init__("Error: Pedido Duplicado !!!")
