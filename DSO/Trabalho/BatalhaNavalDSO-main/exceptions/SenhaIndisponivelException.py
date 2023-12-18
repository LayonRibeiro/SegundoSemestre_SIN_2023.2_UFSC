

class SenhaIndiponivelExecption(Exception):
    def __init__(self):
        super().__init__("ATENÇÂO. Senha Indisponível.")