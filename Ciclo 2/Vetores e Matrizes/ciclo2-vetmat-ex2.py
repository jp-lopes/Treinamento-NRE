#Escreva um código em python que receba 2 vetores e pergunte ao usuário 
# qual operação ele deseja realizar (soma ou multiplicação).
tamvet = int(input("Tamanho dos vetores: "))
v1 = tamvet*[0]
v2 = tamvet*[0]
resultado = tamvet*[0]
print("Insira o Vetor 1: ")
for i in range(0,tamvet):
    v1[i] = int(input())
print("Insira o Vetor 2: ")
for i in range(0,tamvet):
    v2[i] = int(input())
operacao = input("Qual operação deve ser realizada? (+ ou *) ")
if operacao == "+":
    for i in range(0,tamvet):
        resultado[i] = v1[i]+v2[i]
elif operacao == "*":
    for i in range(0,tamvet):
        resultado[i] = v1[i]*v2[i]
print(f"Resultado : {resultado}")