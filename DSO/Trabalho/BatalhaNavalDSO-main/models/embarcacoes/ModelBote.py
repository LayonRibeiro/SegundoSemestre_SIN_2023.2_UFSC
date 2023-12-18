from models.ModelEmbarcacao import ModelEmbarcacao


class Bote(ModelEmbarcacao):
    def __init__(self) -> None:
        super().__init__("BOTE", 1, "FUNCIONANDO")
        self.__num_de_pescadores = 3

    @property
    def num_de_pescadores(self):
        return self.__num_de_pescadores