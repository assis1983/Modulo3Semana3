itens_estoque = []
def adicionar_item_estoque():
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

def listar_itens_estoque():
    print(20 * '-')

    for item in itens_estoque:
        print(f'Nome: {item["nome"]}')
        print(f'Quantidade: {item["quantidade"]}')
        print(f'Descrição: {item["descricao"]}')
        
        print(20 * '-')
    print()

if __name__ == '__main__':
    print('Sistema de Estoque\n')
    opcao = 0
    while opcao != 3:
        print('Menu de Opções')
        print('==============')
        print('1 - Adicionar item no estoque')
        print('2 - Listar itens do estoque')
        print('3 - Sair\n')

        opcao = int(input('Selecione uma opção: '))
        
        if opcao == 1:
            adicionar_item_estoque()
        elif opcao == 2:
            listar_itens_estoque()    
        elif opcao == 3:
            print('Obrigado por usar o programa')
        else:
            print('Opção Inválida\n')