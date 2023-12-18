import PySimpleGUI as sg

class ViewPartida:
    def tamanho_mar(self):
        layout = [
            [sg.Text("---------------- CRIANDO  PARTIDA ----------------", font=("Helvetica", 15))],
            [sg.Text("ESCOLHA A DIFICULDADE: ")],
            [sg.Button("FÁCIL [5x5]", key="-FACIL-"), sg.Button("DIFÍCIL [10x10]", key="-DIFICIL-")]
        ]

        window = sg.Window("Escolha a Dificuldade", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                opcao = None
                break
            elif event == "-FACIL-":
                opcao = 1
                break
            elif event == "-DIFICIL-":
                opcao = 2
                break

        window.close()
        return opcao
    
    def observacoes(self):
        layout = [
            [sg.Text("OBSERVAÇÕES", font=("Helvetica", 15), justification='center')],
            [sg.Text("AS EMBARCAÇÕES SERÃO POSICIONADAS NA DIREÇÃO HORIZONTAL OU VERTICAL")],
            [sg.Text("NÃO SERÁ PERMITIDO SOBREPOSIÇÃO DE EMBARCAÇÕES")],
            [sg.Text("BOTES(B)        → QNTD: 3 → OCUPA 1 POSIÇÃO(ÕES)")],
            [sg.Text("SUBMARINOS(S)   → QNTD: 2 → OCUPA 2 POSIÇÃO(ÕES)")],
            [sg.Text("FRAGATAS(F)     → QNTD: 2 → OCUPA 3 POSIÇÃO(ÕES)")],
            [sg.Text("PORTA AVIÕES(P) → QNTD: 1 → OCUPA 4 POSIÇÃO(ÕES)")],
            [sg.Button("OK", key="-OK-")]
        ]

        window = sg.Window("Observações", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "-OK-":
                break

        window.close()

    def texto_pega_coordenadas(self):
        layout = [
            [sg.Text("INDIQUE A POSIÇÃO INICIAL E A FINAL, RESPECTIVAMENTE")],
            [sg.Text("A VERIFICAÇÃO SE A EMBARCAÇÃO SERÁ DIRECIONADA NA VERTICAL OU HORIZONTAL, DEPENDE DA SUA ESCOLHA:")],
            [sg.Text("CASO OS NÚMEROS - LINHAS -  FOREM IGUAIS,  A EMBARCAÇÃO ESTARÁ NA HORIZONTAL")],
            [sg.Text("CASO AS LETRAS - COLUNAS - FOREM IGUAIS, A EMBARCAÇÃO ESTARÁ NA VERTICAL")],
            [sg.Text("EXEMPLO: 5A,7A")],
            [sg.Text("POSIÇÃO DESEJADA: "), sg.InputText(key="-POSICAO-")],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
        ]

        window = sg.Window("Escolha a Posição", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "-CANCELAR-":
                posicao = None
                break
            elif event == "-CONFIRMAR-":
                posicao = values["-POSICAO-"]
                break

        window.close()
        return posicao

    def pegar_coordenadas(self, i, qtd_embarcacoes, nome_embarcacao, qtd_posicoes):
        layout = [
            [sg.Text(f"POSICIONE O {i}° {nome_embarcacao} ({i}/{qtd_embarcacoes}) - OCUPA {qtd_posicoes} POSIÇÃO:")],
            [sg.Text("Posição desejada: "), sg.InputText(key="-POSICAO-")],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
        ]

        window = sg.Window("Posicionar Embarcação", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "-CANCELAR-":
                posicao = None
                break
            elif event == "-CONFIRMAR-":
                posicao = values["-POSICAO-"].upper()
                break

        window.close()

        return posicao
    
    def erro_inserir_coordenadas_embarcacao(self):
        sg.popup_error("ATENÇÃO: COORDENADAS INVÁLIDAS")
        self.observacoes()

    def mensagens(self, mensagem: str):
        sg.popup(mensagem)

    def erro_inserir_coordenada(self):
        sg.popup_error("ERRO AO INSERIR COORDENADA. TENTE NOVAMENTE!")

    def fazer_jogada(self):
        layout = [
            [sg.Text("FAÇA SUA JOGADA!")],
            [sg.Text("Posição desejada: "), sg.InputText(key="-POSICAO-")],
            [sg.Button("Confirmar", key="-CONFIRMAR-"), sg.Button("Cancelar", key="-CANCELAR-")]
        ]

        window = sg.Window("Faça sua Jogada", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "-CANCELAR-":
                posicao = None
                break
            elif event == "-CONFIRMAR-":
                posicao = values["-POSICAO-"].upper()
                break

        window.close()

        return posicao
    
    def erro_ao_jogar(self):
        sg.popup_error("JOGADA INVÁLIDA. TENTE NOVAMENTE.")

    def acertou(self, posicao, letra, mar_exibicao):
        embarcacoes = {'B': 'Bote', 'F': 'Fragata', 'S': 'Submarino', 'P': 'Porta-Aviões'}
        nome_embarcacao = embarcacoes.get(letra, 'Embarcação Desconhecida')
        
        mensagem = f'EM {posicao} VOCÊ ACERTOU UM(A) {nome_embarcacao}!\n\n'
        
        if mar_exibicao is not None:
            if isinstance(mar_exibicao, list):
                mensagem += '\n'.join([' '.join(map(str, row)) for row in mar_exibicao])
            else:
                mensagem += str(mar_exibicao)

        sg.popup("Acertou!", mensagem)

    def errou(self, posicao, mar_exibicao):
        mensagem = f'EM {posicao} NÃO HÁ NENHUMA EMBARCAÇÃO. VOCÊ ERROU!\n\n'
        
        if mar_exibicao is not None:
            if isinstance(mar_exibicao, list):
                mensagem += '\n'.join([' '.join(map(str, row)) for row in mar_exibicao])
            else:
                mensagem += str(mar_exibicao)

        sg.popup("Errou!", mensagem)

        sg.popup("Errou!", mensagem)

    def ganhou(self):
        sg.popup("Parabéns!", "VOCÊ AFUNDOU TODAS AS EMBARCAÇÕES INIMIGAS. VOCÊ GANHOU!")

    def perdeu(self):
        sg.popup_error("OPS... O COMPUTADOR AFUNDOU TODAS AS SUAS EMBARCAÇÕES. VOCÊ PERDEU!")

    def computador_acertou(self, posicao, letra):
        embarcacoes = {'B': 'Bote', 'F': 'Fragata', 'S': 'Submarino', 'P': 'Porta-Aviões'}
        nome_embarcacao = embarcacoes[letra]
        sg.popup("Acertou!", f'EM {posicao} O COMPUTADOR ACERTOU UM(A) {nome_embarcacao}!')

    def computador_errou(self, posicao):
        sg.popup("Errou!", f'EM {posicao} NÃO HÁ NENHUMA EMBARCAÇÃO. O COMPUTADOR ERROU!')

    def exibe_pontuacao(self, pontuacao):
        sg.popup("PONTUAÇÃO DA PARTIDA", f'JOGADOR {pontuacao[0]} X COMPUTADOR {pontuacao[1]}')