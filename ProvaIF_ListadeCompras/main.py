from fn import carrinho, produto, ad_Items, show_items, att_Items, remove_Items

print('\nBem-vindo(a) ao seu carrinho de compras virtual!\n'.center(150))

while True:
    op = int(input('Digite qual opção do menu você deseja seguir? \n(1)Adicionar itens\n(2)Listar itens\n(3)Atualizar itens\n(4)Remover itens\n(5)Sair\n\n'))
    match op:

        case 1:
            nome = str(input('\nDigite o nome do produto:\n'))
            valor = float(input('\nDigite o valor da unidade do protudo:\n'))
            qtd = int(input('\nDigite a quantidade do produto:\n'))
            print(ad_Items(nome,valor,qtd))

        case 2:
            print(show_items())

        case 3:
            print(att_Items(carrinho, valor, qtd))

        case 4:
            print(remove_Items(carrinho))

        case 5:
            print('\nObrigado por utilizar o programa!\n'.center(150))
            break