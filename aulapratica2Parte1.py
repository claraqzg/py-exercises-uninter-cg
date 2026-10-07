print ('Calculadora de triângulo.')
lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))

if (lado1 >= lado2 + lado3) or (lado2 >= lado1 + lado3) or (lado3 >= lado1 + lado2) or (lado1 <= 0) or (lado2 <= 0) or (lado3 <= 0):
    print('Não é possível formar um triângulo com esses lados.')
    print('Não é possível formar um triângulo com esses lados.')
elif (lado1 == lado2) and (lado2 == lado3):
    print('O triângulo é equilátero.')
elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
    print('O triângulo é isósceles.')  
else:
    print('O triângulo é escaleno.')