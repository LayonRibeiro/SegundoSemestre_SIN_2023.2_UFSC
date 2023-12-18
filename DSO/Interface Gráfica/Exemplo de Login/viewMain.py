import PySimpleGUI as sg
from enum import Enum
    

class ViewMain:
    def __init__(self) -> None:
        self.__window = None
        self.tela_opcoes()

    def tela_opcoes(self): 
        layout = [
            [sg.Button("LOGIN")],
            [sg.Button("CADASTRAR")],
            [sg.Button("EXCLUIR CADASTRO")],
            [sg.Button("RANKING JOGADORES")],
            [sg.Button("ENCERRAR")]
        ]

        self.__window = sg.Window('MENU PRICIPAL').Layout(layout)

    def open(self):
        button = self.__window.Read()
        return button
    
    def close(self):
        self.__window.Close()