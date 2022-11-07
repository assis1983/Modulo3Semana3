if __name__ == '__main__':
    print('Sistema de Estoque\n')
    opcao = 0
    while opcao != 1:
        print('Menu de Opções')
        print('==============')
        print('1 - Sair\n')

        opcao = int(input('Selecione uma opção:\n '))
        
        if opcao == 1:
            print('Obrigado por usar o programa')
        else:
            print('Opção Inválida\n')