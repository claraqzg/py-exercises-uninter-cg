valor = int(input("Digite o valor em reais: "))

cedulas = [200, 100, 50, 20, 10, 5, 2, 1]

for cedula in cedulas:
    quantidade = valor // cedula
    valor = valor % cedula
    print(f"{quantidade} cédulas de R$ {cedula}")