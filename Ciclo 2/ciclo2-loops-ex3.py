#Faça uma calculadora em Python com um menu no qual o usuário pode escolher o 
#tipo de operação que deseja realizar e se deseja encerrar o programa.

while(1):
    a = float(input("a: "))
    op = input("Operação: ")
    b = float(input("b: "))
    if op == "+":
        resultado = a+b
    elif op == "-":
        resultado = a-b
    elif op == "*":
        resultado = a*b
    elif op == "/":
        resultado = a/b
    else:
        print("ERRO: operação inválida.")
        continue
    print(f"{resultado}")
    if(input("Deseja encerrar o programa? (s/n) " ) == "s"): 
        break
    else:
        continue