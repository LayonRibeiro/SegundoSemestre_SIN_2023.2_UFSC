import PySimpleGUI as sg

class TelaInicial:
    def __init__(self) -> None:
        self.__window = None
        self.init_componentes()

    def init_componentes(self):
        layout = [
            [sg.Button("Incluir")],
            [sg.Button("Alterar")],
            [sg.Button("Executar")]
        ]

        self.__window = sg.Window('Cadastro de Clientes').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()

    def show_message(self, titulo, mensagem):
        sg.Poput(titulo, mensagem)