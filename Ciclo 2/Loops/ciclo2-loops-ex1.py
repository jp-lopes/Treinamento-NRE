#1.Faça um código que imprima na tela os números de 0 até o número que o usuário inserir.
a = int(input("Digite um valor: "))
for i in range(0,a+1):
    print(f"{i} ", end = "")