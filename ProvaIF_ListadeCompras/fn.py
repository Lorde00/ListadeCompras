# Adicionar produtos a lista, ver produtos, atualizar atualizar informaçoes de produto, remover produtos, calcula o valor de todos os itens

carrinho = []
produto = {}

def ad_Items(nome,valor,qtd):
    produto = {
        'Nome': nome,
        'Valor': valor,
        'Quantidade': qtd,
        'Valor total': valor * qtd
    }
    carrinho.append(produto)
    return f'\nO produto {nome}, foi adicionado ao carrinho de compras.\n'

def show_items():
    if not carrinho:
        return 'Você não tem nenhum item adicionado ao carrinho de compras!\n'
    
    while True:
        
        for produto in carrinho:
            print(f'\nNome: {produto['Nome']}, Valor: R${produto['Valor']}, Quantidade: {produto['Quantidade']}, Valor total: R${produto['Valor total']}\n')
        return 'Essa é sua lista de compras!\n'
        
        
    
   
        

def att_Items(carrinho, valor, qtd):
    for produto in carrinho:
        print(f'{produto}\n')
    
    change = int(input('Digite a posição do produto: (0 é o primeiro)\n'))
    att_item = carrinho[change]
    while True:
        change_spc = input('Oque você quer mudar no produto? (Digite 0 para sair)\n').upper()
        if change_spc == 'NOME':
            nome = str(input('Diga o novo nome do item:\n'))
            att_item.update({'Nome': nome})
            print(f'O nome do item foi atualizado para {nome}\n')

        elif change_spc == 'VALOR':
            valor = float(input('Digite o novo valor do item:\n'))
            att_item.update({'Valor': valor})
            att_item.update({'Valor total': qtd * valor})
            print(f'O valor do item foi atualizado para {valor}\n')

        elif change_spc == 'QUANTIDADE':
            qtd = int(input('Digite a nova quantidade do item:\n'))
            att_item.update({'Quantidade': qtd})
            att_item.update({'Valor total': qtd * valor})
            print(f'A quantidade do item foi atualizada para {qtd}\n')
        
        elif change_spc == 0:
            break

        else:
            return '\nPor favor insira uma opção válida!\n'
        
def remove_Items(carrinho):
    for produto in carrinho:
        print(f'{produto}\n')

    while True:
        change = int(input('Digite a posição do produto: (0 é o primeiro, digite 999 para parar)\n'))
        if change == 999:
            break
        
        elif change > len(carrinho):
            print('Não existe nenhum item nesta posição!')

        else:
            carrinho.pop(change)
            return 'O item foi removido com sucesso'
    
    
        


