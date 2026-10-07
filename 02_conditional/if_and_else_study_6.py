operacao = input('Digite a operação (+, -, *, /) ou selecione qualquer tecla para sair: ')
if operacao not in ['+', '-', '*', '/']:
    print('Operação inválida. Encerrando o programa.')
else:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    if operacao == '+':
        resultado = num1 + num2
        print(f'O resultado da soma é: {resultado}')
    elif operacao == '-':
        resultado = num1 - num2
        print(f'O resultado da subtração é: {resultado}')
    elif operacao == '*':
        resultado = num1 * num2
        print(f'O resultado da multiplicação é: {resultado}')
    else:
        if num2 == 0 or num1 == 0:
            print('Erro: Divisão por zero não é permitida.')
        else:
            resultado = num1 / num2
            print(f'O resultado da divisão é: {resultado}')