def adicionar_item_estoque():
    itens_estoque = []
    nome = input('Nome do item: ')
    descricao = input('Descrição do item: ')
    quantidade = int(input('Quantidade do item: '))

    item = {
        'nome': nome,
        'descricao': descricao,
        'quantidade': quantidade
    }
    itens_estoque.append(item)
    print(f'O item {nome} foi adicionado no estoque\n')

if __name__ == '__main__':
    print('Sistema de Estoque\n')
    opcao = 0
    while opcao != 2:
        print('Menu de Opções')
        print('==============')
        print('1 - Adicionar item no estoque')
        print('2 - Sair\n')

        opcao = int(input('Selecione uma opção: '))
        
        if opcao == 1:
            adicionar_item_estoque()
        elif opcao == 2:
            print('Obrigado por usar o programa')
        else:
            print('Opção Inválida\n')