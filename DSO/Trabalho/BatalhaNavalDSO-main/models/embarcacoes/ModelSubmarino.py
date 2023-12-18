from models.ModelEmbarcacao import ModelEmbarcacao


class Submarino(ModelEmbarcacao):
    def __init__(self) -> None:
        super().__init__("SUBMARINO", 4, "SUBMERGIDO")
        self.__pressao = "15000 atm"

    @property
    def pressao(self):
        return self.__pressao