def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while (tam < min or tam > max):
        s1 = input(pergunta)
        tam = len(s1)
    return s1

x = valida_string("Digite uma string:", 3, 10)
print(f"Você digitou: {x}. \nDado válido, encerrando o programa.")