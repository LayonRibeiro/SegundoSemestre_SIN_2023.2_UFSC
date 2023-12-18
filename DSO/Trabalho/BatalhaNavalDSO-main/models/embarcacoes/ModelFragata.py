from models.ModelEmbarcacao import ModelEmbarcacao


class Fragata(ModelEmbarcacao):
    def __init__(self) -> None:
        super().__init__("FRAGATA",2, "BOIANDO")
        self.__tripulacao = 15

    @property
    def tripulacao(self):
        return self.__tripulacao