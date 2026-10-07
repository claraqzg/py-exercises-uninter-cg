print ('Digite o número de qual fruta você quer comprar:')
print ('1 - Maçã')
print ('2 - Laranja')
print ('3 - Banana')
opcao = int(input('Opção: '))

if opcao > 3:
    print("Opção inválida!")
else:
    print('Digite a quantidade que você quer comprar:')
    quantidade = int(input('Quantidade: '))

    if opcao == 1:
        preco = 2.30
        total = preco * quantidade
    elif opcao == 2:
        preco = 3.60
        total = preco * quantidade
    elif opcao == 3:
        preco = 1.85
        total = preco * quantidade

    print(f"Total a pagar: R$ {total:.2f}")