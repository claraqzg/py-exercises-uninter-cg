# def borda (s1):
#     print ("+" + "-" * len(s1) + "+")
#     print (f"|{s1}|")
#     print ("+" + "-" * len(s1) + "+")

# borda ("Hello, World!")

def borda (s1):
    tam = len(s1)
    if tam:
        print ("+" + "-" * tam + "+")
        print (f"|{s1}|")
        print ("+" + "-" * tam + "+")

borda(input("Digite uma frase: "))