# Expressões algébricas

print (1 + 2 + 3 + 4 + 5)

media = (23 + 19 + 31) / 3
print (f'A média das notas é: {media:.2f}')

print (403//73)

print (403%73)

print (2**10)

print (abs(54-57))

menor = min(34, 29, 31)
print (f'O menor valor é: {menor}')

# Atribuição exercício 1

a = 3
b = 4
c = a*a + b*b
print (f'O valor de c é: {c}')

# Strigs exercício 1

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

res = s1 + ' ' + s2 + ' ' + s3
res2 = (s1 + ' ') * 10
res3 = (s1 + ' ') + (s2 + ' ') * 2 + (s3 + ' ') * 3
res4 = (s1 + ' ' + s2 + ' ') * 7
res5 = ((s2*2) + s3 + ' ') * 5
print (f'{res}')
print (f'{res2}')
print (f'{res3}')
print (f'{res4}')
print (f'{res5}')