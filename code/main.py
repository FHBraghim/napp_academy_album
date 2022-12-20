from album import Album
import csv
import os

meu_album = Album()

while True:
    os.system("clear")
    print("\nÁlbum de figurinhas da Copa do Mundo de 2022\n")
    opc = input("""
    Escolha uma das opções:

    1 - Abrir pacote com 5 figurinhas
    2 - Ver as figurinhas coladas no álbum
    3 - Ver as figurinhas repetidas
    4 - Ver as figurinhas faltantes
    5 - Remover figurinhas repetidas
    6 - Exportar os dados para um arquivo CSV
    7 - Carregar dados salvos
    8 - Sair

    Sua opção: """)

    if opc == '1':
        os.system("clear")
        pacote = meu_album.open_package()
        print(pacote)
        input()

    elif opc == '2':
        meu_album.show_figures_added()
        input()

    elif opc == '3':
        meu_album.show_figures_repeated()
        input()

    elif opc == '4':
        meu_album.show_figures_missing()
        input()

    elif opc == '5':
        os.system("clear")
        figura = input("Digite a figurinha repetida que deseja excluir: ")
        meu_album.remove_figure(figura)
        input()

    elif opc == '6':
        os.system("clear")
        try:
            meu_album.gravar_figurinhas_coladas()
            meu_album.gravar_figurinhas_repetidas()
            meu_album.gravar_figurinhas_faltantes()
        except FileNotFoundError:
            print("Houve um erro! Verifique o caminho do arquivo")
        else:
            print("Dados salvos com sucesso!")
        input()

    elif opc == '7':
        os.system("clear")
        print('Tem certeza que deseja recuperar os dados de um arquivo antigo?')
        print('Isso apagará todos os dados gerados na última execução.')
        confirma = input(str('[s] - Sim      [n] - Não: ')).casefold()
        if confirma == ('s').casefold():
            os.system("clear")
            try:            
                meu_album._figurinhas_coladas_album = meu_album.ler_figurinhas_coladas()
                meu_album._figurinhas_repetidas = meu_album.ler_figurinhas_repetidas()
                meu_album._figurinhas_faltantes = meu_album.ler_figurinhas_faltantes()
                print("Dados recuperados com sucesso!")
            except FileNotFoundError:
                print("Houve um erro! Verifique o caminho do arquivo")
        else:
            os.system("clear")
            print("Recuperação de arquivo cancelada!")
        input()       

    elif opc == '8':
        break

    else:        
        print("Opção inválida")
        input()
