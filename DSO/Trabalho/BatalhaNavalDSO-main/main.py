from controllers.ControllerMain import ControllerMain

if __name__ == "__main__":
    try:
        ControllerMain().inicializa_sistema()
    except:
        print('Encerrando sistema...')
