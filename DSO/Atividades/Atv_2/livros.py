class Livro:
    def __init__(self):
        self.__titulo = ""
        self.__resumo = ""
        self.__autor = ""
        self.__personagemPrincipal = ""
        self.__genero = ""
        self.__faixaEtaria = ""
        self.__locadores = []
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
    
    def get_resumo(self):
        return self.__resumo
    
    def set_resumo(self, resumo):
        return self.__resumo = resumo
    
    def get_autoria(self):
        return self.__autor
    
    def set_autoria(self, autoria):
        self.__autor =  autoria
        
    def get_personagemPrincipal(self):
        return self.__personagemPrincipal
    
    def set_personagemPrincipal(self, personagem):
        self.__personagemPrincipal = personagem
        
    def get_genero(self):
        return self.__genero

livro = Livro()
livro.titulo = 'titulo'
    def set_genero(self, genero):
        self.__genero = genero
        
    def get_faixaEtaria(self):
        return self.__faixaEtaria
    
    def set_faixaEtaria(self, faixa):
        self.__faixaEtaria = faixa   