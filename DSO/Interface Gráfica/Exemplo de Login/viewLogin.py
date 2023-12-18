import PySimpleGUI as sg

class ViewLogin:
    def __init__(self):
        self.__window = None
        self.init_componenetes()

    def init_componenetes(self):
        layout = [
            [sg.Text('Insira o nome do Jogador')],
            [sg.Text('NOME', size=(15,1)), sg.InputText('nome', key='nome')],
            [sg.Text('Insira a senha')],
            [sg.Text('SENHA', size=(15,1)), sg.InputText('senha', key='senha')],
            [sg.Submit(), sg.Cancel()]
                ]

        self.__window = sg.Window('Login').Layout(layout)

    def open(self):
        buttons, valores = self.__window.Read()
        return buttons, valores

    def close(self):
        self.__window.Close()

    def show_message(self, titulo, mensagem):
        sg.Popup(titulo, mensagem)