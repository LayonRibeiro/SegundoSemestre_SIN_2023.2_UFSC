from datetime import datetime

from views.ViewJogador import ViewJogador
from models.ModelJogador import Jogador
from exceptions.NomeJahUtilizadoException import NomeJahUtilizadoException
from exceptions.SenhaIndisponivelException import SenhaIndiponivelExecption
from exceptions.LoginIvalidoException import LoginInvalidoException
from persistencia.ModelJogadorDAO import JogadorDao

class ControllerJogador:
    def __init__(self, controle_main):
        self.__jogador_dao = JogadorDao()
        self.__view_jogador = ViewJogador()
        self.__controlador_main =  controle_main
        self.__jogador1 = None

    @property
    def jogadores(self):
        return self.__jogador_dao.get_all()
    
    def existe_jogador_cadastrado(self):
        return self.__jogador_dao.armazenamento()
        
    @property
    def jogador1(self):
        return self.__jogador1
    
    def logar(self):
        self.__view_jogador.login()
        dados_jogador = self.__view_jogador.pega_nome_e_senha()
        jogador = self.pega_jogador_por_nome_e_senha(dados_jogador["nome"], dados_jogador["senha"])
        try:
            if jogador is not None:
                self.__jogador1 = jogador
                self.__view_jogador.mensagem("Bem-Vindo " + self.__jogador1.nome)
                return True
            else:
                raise LoginInvalidoException
        except LoginInvalidoException:
            self.__controlador_main.mensagem("Login Inváldio")
            self.__controlador_main.mostra_tela_main()

    def lista_de_jogadores(self):
        for  jogador in self.__jogador_dao.get_all():
            self.__view_jogador.mostrar_jogador({"nome": jogador.nome, "nascimento": jogador.nascimento})
    
    def pega_jogador_por_nome_e_senha(self, nome: str, senha: str):
        for  jogador in self.__jogador_dao.get_all():
            if jogador.nome == nome and jogador.senha == senha:
                return jogador
        return None
    
    def compara_nomes_e_senhas(self, nome: str, senha: str):
        for  jogador in self.__jogador_dao.get_all():
            try:
                if jogador.nome == nome:
                    raise NomeJahUtilizadoException
                elif jogador.senha == senha:
                    raise SenhaIndiponivelExecption
            except NomeJahUtilizadoException:
                self.__view_jogador.mensagem("ATENÇÃO: Nome já em uso. Por favor, escolha outro nome.")
                self.__controlador_main.cadastra_jogador()
            except SenhaIndiponivelExecption:
                self.__view_jogador.mensagem("ATENÇÃO: Senha indisponível. Tente outra senha")
                self.__controlador_main.cadastra_jogador()
        return True         

    def jogar(self):
        self.__controlador_main.criar_partida(self.__jogador1)

    def historico(self):
        for indice, partida in enumerate(self.__jogador1.historico):
            self.__view_jogador.exibe_historico(partida.lista_de_disparos, indice)

    def cadastrar(self, recadastro: bool):
        dados_jogador = self.__view_jogador.pega_dados_jogador()
        data_string = dados_jogador['nascimento']
        formato_data = '%d/%m/%Y'
        try:
            datetime.strptime(data_string, formato_data)
            if dados_jogador['nome'] == '':
                self.__view_jogador.erro_nome()
                self.cadastrar()
            if dados_jogador['senha'] == '':
                self.__view_jogador.erro_senha()
                self.cadastrar()
        except ValueError:
            self.__view_jogador.erro_data()
            self.__controlador_main.cadastra_jogador()
        validacao_cadastro = self.compara_nomes_e_senhas(dados_jogador["nome"], dados_jogador["senha"])
        try:
            if validacao_cadastro:
                novo_jogador= Jogador(dados_jogador["nome"], dados_jogador["nascimento"], dados_jogador["senha"])
                self.__jogador_dao.add(novo_jogador)
                self.__jogador1 = novo_jogador
        except validacao_cadastro:
            self.__controlador_main.cadastra_jogador()
        if recadastro:
            return
        else:
            self.abre_tela()

    def seleciona_jogador(self):
        self.lista_de_jogadores()
        dados_player =  self.__view_jogador.pega_nome_e_senha()
        player = self.pega_jogador_por_nome_e_senha(dados_player["nome"], dados_player["senha"])
        if player is not None: 
            return player
        else:
            self.__view_jogador.mensagem("Jogador não cadastrado")
            self.retornar_main()
    
    def pede_senha(self):
        senha = self.__view_jogador.pega_senha()
        if senha["senha"] == self.__jogador1.senha:
            return True
        return False   

    def alterar_cadastro(self):
        if self.pede_senha():
            self.excluir_jogador(self.__jogador1, False)
            self.abre_tela()
        else:
            self.__view_jogador.mensagem("SENHA INCORRETA")
            self.abre_tela()

    def excluir_jogador(self, player: Jogador, vem_do_main : bool):
            dados_antigos = self.__jogador_dao.get(player)
            if vem_do_main:
                if dados_antigos is not None:
                    if len(dados_antigos.historico) > 0:
                        if self.__view_jogador.exclusao_de_cadastro():
                            self.__jogador_dao.remove(player)
                            self.__view_jogador.mensagem("Jogador Removido")
                        else:
                            self.__controlador_main.mostra_tela_main()

            else:
                self.cadastrar(True)
                self.__jogador1.incluir_historico(dados_antigos.historico)
                self.__jogador1.incluir_pontuacao_total(dados_antigos.pontuacao_total)
                self.__jogador_dao.add(self.__jogador1)
                self.__jogador_dao.remove(dados_antigos)
                self.__view_jogador.mensagem("Cadastro Atualizado")
            self.lista_de_jogadores()
      
    def incluir_partida(self, partida):
        dados_player = self.__jogador_dao.get(self.__jogador1)
        dados_player.incluir_partida(partida)
        self.__jogador_dao.add(dados_player)

    def exibe_ranking(self):
        return self.__jogador_dao.exibe_ranking()

    def retornar_main(self):
        self.__controlador_main.mostra_tela_main()

    def abre_tela(self):
        lista_opcoes = {1: self.jogar, 2: self.historico, 3: self.alterar_cadastro, 0: self.retornar_main}

        continua = True
        try:
            while continua:
                lista_opcoes[self.__view_jogador.tela_opcoes()]()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            self.__view_jogador.erro_tela()