from models.ModelEmbarcacao import ModelEmbarcacao

class PortaAviao(ModelEmbarcacao):
    def __init__(self) -> None:
        super().__init__("PORTAS-AVIÕES", 4, "DE PÉ")
        self.__num_de_avioes = 20
    
    @property
    def num_de_avioes(self):
        return self.__num_de_avioes