import PySimpleGUI as sg

class ViewMar:
    def ver_mar(self, mar):
        layout = []

        for i, row in enumerate(mar):
            row_layout = []
            for j, cell in enumerate(row):
                if cell == 'O':
                    button = sg.Button('', key=(i, j), size=(3, 1), pad=(0, 0), button_color=('white', 'white'), border_width=0.5)
                elif cell == 'X':
                    button = sg.Button('', key=(i, j), size=(3, 1), pad=(0, 0), button_color=('white', 'red'), border_width=0.5)
                elif cell == 'B':
                    button = sg.Button('B', key=(i, j), size=(3, 1), pad=(0, 0), button_color=('white', 'blue'), border_width=0.5)
                elif cell == 'F':
                    button = sg.Button('F', key=(i, j), size=(3, 1), pad=(0, 0), button_color=('white', 'blue'), border_width=0.5)
                elif cell == 'S':
                    button = sg.Button('S', key=(i, j), size=(3, 1), pad=(0, 0), button_color=('white', 'blue'), border_width=0.5)
                elif cell == 'P':
                    button = sg.Button('P', key=(i, j), size=(3, 1), pad=(0, 0), button_color=('white', 'blue'), border_width=0.5)
                else:
                    button = sg.Button('', key=(i, j), size=(3, 1), pad=(0, 0), button_color=('white', 'white'), border_width=0.5)

                row_layout.append(button)

            layout.append(row_layout)

        layout.append([sg.Button("Fechar", key="-FECHAR-")])

        window = sg.Window("Estado Atual do Mar", layout, finalize=True)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "-FECHAR-":
                break

        window.close()
