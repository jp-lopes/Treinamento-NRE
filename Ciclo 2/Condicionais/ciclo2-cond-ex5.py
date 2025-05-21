#Faça um código para que o usuário insira 2 números e o programa diga qual o
#maior (ou se são iguais)

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))

if a>b: print(f"Maior: {a}")
elif b>a: print(f"Maior: {b}")
else: print("Iguais")

