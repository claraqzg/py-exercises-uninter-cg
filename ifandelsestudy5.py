nome = input("Digite seu nome: ")

if nome == "Vinicius":
    print("Olá Vinicius! Bem-vindo de volta!")
else:
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        print("Você é menor de idade.")
    elif idade >= 18 and idade <= 100:
        print("Você é maior de idade.")
    else:
        print("Você provavelmente não existe.")
        