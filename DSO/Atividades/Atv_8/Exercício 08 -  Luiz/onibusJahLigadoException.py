class OnibusJahLigadoException(Exception):
    def __init__(self):
        super().__init__("O onibus ja está ligado!")
