import PySimpleGUI as sg


class ViewJogador:
    def tela_opcoes(self):
        layout = [
            [sg.Text("--------------------- OPÇÕES ---------------------")],
            [sg.Text("ESCOLHA ALGUMA OPÇÃO")],
            [sg.Button("JOGAR", key='1')],
            [sg.Button("VER HISTÓRICO DE PARTIDAS", key='2')],
            [sg.Button("ALTERAR CADASTRO", key='3')],
            [sg.Button("RETORNAR", key='0')],
        ]

        window = sg.Window("Opções", layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return 0

            try:
                opcao = int(event)
                window.close()
                return opcao
            except ValueError:
                sg.popup_error('Por favor, insira um número válido.')
                
    def login(self):
        layout = [
            [sg.Text("FAÇA O LOGIN", size=(20, 1), justification='center', font=('Helvetica', 14), relief=sg.RELIEF_RIDGE)],
            [sg.Text("")],
            [sg.Button("Iniciar Sessão", size=(20, 2), key='-LOGIN-')],
            [sg.Button("Sair", size=(20, 2), key='-SAIR-')]
        ]

        self.janela = sg.Window("Login", layout, size=(300, 200), element_justification='c')

    def cadastro(self):
        layout = [
            [sg.Text("CADASTRO", font=("Helvetica", 20), justification='center')],
            [sg.Button("Preencher Dados do Jogador", key="-PEGA_DADOS-")],
            [sg.Button("Cancelar", key="-CANCELAR-")]
        ]

        window = sg.Window("Cadastro", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "-CANCELAR-":
                break
            elif event == "-PEGA_DADOS-":
                dados_jogador = self.pega_dados_jogador()
                sg.popup("Dados do jogador:", dados_jogador)
        
        
    def pega_dados_jogador(self):
        layout = [
            [sg.Text("INSIRA OS SEGUINTES DADOS", font=("Helvetica", 15), justification='center')],
            [sg.Text("Nome do Player:"), sg.InputText(key="-NOME-")],
            [sg.Text("Data de nascimento do player (DD/MM/AAAA):"), sg.InputText(key="-NASCIMENTO-")],
            [sg.Text("Senha:"), sg.InputText(key="-SENHA-", password_char="*")],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
        ]

        window = sg.Window("Preencher Dados", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "-CANCELAR-":
                dados_jogador = None
                break
            elif event == "-CONFIRMAR-":
                nome = values["-NOME-"]
                nascimento = values["-NASCIMENTO-"]
                senha = values["-SENHA-"]
                dados_jogador = {"nome": nome, "nascimento": nascimento, "senha": senha}
                break

        window.close()
        return dados_jogador
    
    def mostrar_jogador(self, dados_jogador):
        layout = [
            [sg.Text("INFORMAÇÕES DO JOGADOR", font=("Helvetica", 20), justification='center')],
            [sg.Text(f"NOME DO PLAYER: {dados_jogador['nome']}")],
            [sg.Text(f"DATA DE NASCIMENTO: {dados_jogador['nascimento']}")],
            [sg.Button("OK", key="-OK-")]
        ]

        window = sg.Window("Informações do Jogador", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "-OK-":
                break

        window.close()
    
    def pega_nome_e_senha(self):
        layout = [
            [sg.Text("Digite o nome do Player:")],
            [sg.InputText(key='-NOME-')],
            [sg.Text("Digite a senha:")],
            [sg.InputText(key='-SENHA-', password_char='*')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]

        self.janela = sg.Window('Login - Insira Nome e Senha', layout)

        while True:
            event, values = self.janela.read()

            if event in (sg.WINDOW_CLOSED, 'Cancelar'):
                self.janela.close()
                return None, None

            if event == 'OK':
                nome = values['-NOME-']
                senha = values['-SENHA-']
                self.janela.close()
                return {"nome": nome, "senha": senha}
    
    def pega_senha(self):
        layout = [
            [sg.Text("DIGITE A SENHA", font=("Helvetica", 20), justification='center')],
            [sg.InputText(key="-SENHA-", password_char="*")],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
        ]

        window = sg.Window("Digite a Senha", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "-CANCELAR-":
                senha = None
                break
            elif event == "-CONFIRMAR-":
                senha = values["-SENHA-"]
                break

        window.close()
        return {"senha": senha}      
    
    def mensagem(self, mensagem: str):
        layout = [
            [sg.Text(mensagem, font=("Helvetica", 15), justification='center')],
            [sg.Button("OK", key="-OK-")]
        ]

        window = sg.Window("Mensagem", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "-OK-":
                break

        window.close()

    def exibe_historico(self, lista_disparos, n_partida):
        layout = [
            [sg.Text(f"--------------- PARTIDA {n_partida + 1} ---------------", font=("Helvetica", 15))],
            [sg.Multiline("\n".join(lista_disparos), size=(40, 10), key="-HISTORICO-", disabled=True)],
            [sg.Button("OK", key="-OK-")]
        ]

        window = sg.Window("Histórico da Partida", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "-OK-":
                break

        window.close()
    
    def exclusao_de_cadastro(self):
        layout = [
            [sg.Text("ATENÇÃO: O jogador possui dados salvos.", font=("Helvetica", 15))],
            [sg.Button("Sim", key="-SIM-"), sg.Button("Não", key="-NAO-")]
        ]

        window = sg.Window("Exclusão de Cadastro", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "-NAO-":
                resposta = False
                break
            elif event == "-SIM-":
                resposta = True
                break

        window.close()
        return {"resposta": resposta}

    def erro_data(self):
        sg.popup_error("Formato de data inválido. Certifique-se de que a data está no formato 'dd/mm/aaaa'.")

    def erro_nome(self):
        sg.popup_error("Nome vazio. Certifique-se de preencher o nome.")

    def erro_senha(self):
        sg.popup_error("Senha vazia. Certifique-se de preencher a senha.")

    def erro_tela(self):
        sg.popup_error("Erro ao acessar a tela. Certifique-se de escolher uma opção válida.")
