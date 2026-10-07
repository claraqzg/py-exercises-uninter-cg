total_pessoas = 0 
valor_total = 0 
soma_idades = 0
media_idades = 0
preco = 0

while True:
    idade = int(input("Digite a idade da pessoa (ou 0 para sair): "))
    if idade == 0:
        break
    if idade < 0:
        print("Idade inválida. Digite uma idade válida.")
        continue
    if idade < 3:
        print ("O valor do ingresso é gratuito.")
        preco = 0
    elif idade <= 12:
        print ("O valor do ingresso é de R$ 15,00.")
        preco = 15
    else:
        print ("O valor do ingresso é de R$ 30,00.")
        preco = 30
    total_pessoas += 1
    valor_total += preco
    soma_idades += idade

if total_pessoas > 0:
    media_idades = soma_idades / total_pessoas
    print(f"\nTotal de pessoas: {total_pessoas}")
    print(f"Valor total arrecadado: R$ {valor_total:.2f}")
    print(f"Média de idades: {media_idades:.2f}")
else:
    print("Nenhuma pessoa foi registrada.")