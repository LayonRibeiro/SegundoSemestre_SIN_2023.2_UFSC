from abc import ABC, abstractmethod;
from operator import itemgetter
import pickle

class DAO(ABC):
    @abstractmethod
    def __init__ (self, datasource = ''):
        self.__datasource = datasource
        print(self.__datasource)
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))
    
    def add(self, key, value): # o value aqui pode ser um obejto(Jogador) ou um valor (pontuação)
        self.__cache[key] = value
        self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass
    
    def remove(self, key):
        try:
            del self.__cache[key]
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.__cache.values()
    
    def armazenamento(self):
        if len(self.__cache) > 0:
            return True
    
    def atualiza_ranking(self):
        self.__cache = dict(sorted(self.__cache.items(), key=itemgetter(1), reverse=True))
        self.__dump()