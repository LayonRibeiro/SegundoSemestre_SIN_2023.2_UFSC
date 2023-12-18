class Mar:
    def __init__(self, de_jogador):
        self.__mar = []
        self.__de_jogador = de_jogador
        
    @property
    def mar(self):
        return self.__mar
    
    @mar.setter
    def mar(self, mar):
        self.__mar = mar