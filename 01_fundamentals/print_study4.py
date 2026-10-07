# Exercício 2

kmPercorrido = float(input("Digite a quantidade de km percorridos: "))
diasUso = int(input("Digite a quantidade de dias de uso: "))
precoTotal = (diasUso * 60) + (kmPercorrido * 0.15)
print(f'O preço total do aluguel é: {precoTotal:.2f}')