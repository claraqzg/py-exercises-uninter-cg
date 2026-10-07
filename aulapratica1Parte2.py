# Exercício 1

precoProd = float(input("Digite o preço do produto: "))
print((' '))
desconto = float(input("Digite o valor da porcentagem do desconto (0 a 100): "))
print((' '))
valorDesconto = precoProd * (desconto / 100)
precoFinal = precoProd - valorDesconto
print(f'O valor do desconto é: {valorDesconto:.2f}')
print((' '))
print(f'O preço final é: {precoFinal:.2f}')
