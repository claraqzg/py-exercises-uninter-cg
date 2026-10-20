def validate_input(n):
    '''
    Valida se o número é positivo.
    '''
    return n >= 0

def fatorial_Num(n):
    '''
    Calcula o fatorial de um número n.
    '''
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    return fatorial

while True:
    try:
        x = int(input("Digite um número para calcular o fatorial: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        continue

    if validate_input(x):
        print(f"{x}! = {fatorial_Num(x)}")
        break
    else:
        print("Número inválido. Por favor, digite um número positivo.")
        continue