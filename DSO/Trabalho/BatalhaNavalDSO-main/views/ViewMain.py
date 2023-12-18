import PySimpleGUI as sg

class ViewMain:
    def tela_opcoes(self):
        layout = [
            [sg.Text("----------------- MENU PRINCIPAL -----------------")],
            [sg.Button("1 - LOGIN")],
            [sg.Button("2 - CADASTRAR")],
            [sg.Button("3 - EXCLUIR CADASTRO")],
            [sg.Button("4 - RANKING MELHORES JOGADORES")],
            [sg.Button("0 - SAIR DO GAME")],
        ]

        window = sg.Window('Menu Principal', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return 0

            try:
                opcao = int(event.split(' ')[0])  # Extrai o número do botão clicado
                window.close()
                return opcao
            except ValueError:
                sg.popup_error('Por favor, insira um número válido.')

    def msg(self, mensagem):
        sg.popup(mensagem, title='Mensagem')

    def exibe_ranking(self, ranking):
        layout = [
            [sg.Text("----------------------------- RANKING ----------------------------")],
        ]

        cont = 1
        for player in ranking:
            layout.append([sg.Text(f'{cont} - Nome: {player.nome} | Pontuação Total: {player.pontuacao_total}')])
            cont += 1

        layout.append([sg.Text("------------------------------------------------------------------")])

        sg.Window('Ranking', layout).read(close=True)

    def erro_tela(self):
        sg.popup_error('Erro ao acessar tela. Certifique-se de escolher uma opção válida.')