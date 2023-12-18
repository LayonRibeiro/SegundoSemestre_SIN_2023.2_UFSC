import PySimpleGUI as sg


class Tela:
    def __init__(self) -> None:
        self.__window = None
        self.init_componentes()

    def init_componentes(self):
        layout = [
            [sg.Text('Incluir novo Cliente')],
            [sg.Text('Nome', size=(15,1)), sg.InputText('nome', key='nome')],
            [sg.Text('Incluir novo Cliente')],
            [sg.Text('Cadastro', size=(15,1)), sg.InputText('CADASTRO', key='cadastro')],
            [sg.Submit(), sg.Cancel()]
                ]

        self.__window = sg.Window('Cadastro de Clientes').Layout(layout)

    def open(self):
        button, values = self.__window.Read()

    def close(self):
        self.__window.Close()

    def show_message(self, titulo, mensagem):
        sg.Popup(titulo, mensagem)
