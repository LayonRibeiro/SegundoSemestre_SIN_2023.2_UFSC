class OnibusJahDesligadoException(Exception):
    def __init__(self):
        super().__init__("O onibus está desligado!")
