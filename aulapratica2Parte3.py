kWh = int(input("Digite a quantidade de kWh consumidos: "))
instalacao = input("Digite o tipo de instalação (R, C ou I): ").upper()

if instalacao == 'R':
    if kWh <= 500:
        valor = kWh * 0.40
    else:
        valor = kWh * 0.65
elif instalacao == 'C':
    if kWh <= 1000:
        valor = kWh * 0.55
    else:
        valor = kWh * 0.60
elif instalacao == 'I':
    if kWh <= 5000:
        valor = kWh * 0.55
    else:
        valor = kWh * 0.60
else:
    print("Tipo de instalação inválido. Encerrando o programa.")
    exit()

print(f"O valor a ser pago é: R$ {valor:.2f}")