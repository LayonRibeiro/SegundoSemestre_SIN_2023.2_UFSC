

class NomeJahUtilizadoException(Exception):
    def __init__(self):
        super().__init__("ATENÇÃO. Nome já em uso.")