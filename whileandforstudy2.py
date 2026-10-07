print ('Lanchonete')
print ('Cardápio')
print ('1 - Coxinha - R$ 5,00')
print ('2 - Pastel - R$ 7,00')
print ('3 - Café - R$ 4,00')
print ('4 - Suco - R$ 6,00')
print ('5 - Sair')

valor_total = 0
while True:
    item = int(input('Escolha o item desejado: '))
    if item == 5:
        break
    else:
        qtd = int(input('Digite a quantidade desejada: '))
        if item == 1:
            valor_total += 5 * qtd
        elif item == 2:
            valor_total += 7 * qtd
        elif item == 3:
            valor_total += 4 * qtd
        elif item == 4:
            valor_total += 6 * qtd
        else:
            print('Opção inválida. Tente novamente.')
            continue

print(f'Valor total da compra: R$ {valor_total:.2f}')