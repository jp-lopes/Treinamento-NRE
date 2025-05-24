#Escreva agora um código em python onde o usuário insira os valores de duas matrizes (do tamanho que ele desejar) e 
#pergunte a ele qual operação entre elas deseja realizar (soma, subtração e multiplicação).
n = int(input("Tamanho das matrizes: "))
A = [[0]*(n) for i in range(n)]
B = [[0]*(n) for i in range(n)]
M = [[0]*(n) for i in range(n)]

print("Insira os valores da matriz A por linha: ")
for i in range(0,n):
    for j in range(0,n):
        A[i][j] = int(input())
print("Insira os valores da matriz B por linha: ")
for i in range(0,n):
    for j in range(0,n):
        B[i][j] = int(input())

operacao = input("Qual operação deve ser realizada? (+, - ou *) ")

if operacao == "+":
    for i in range(0,n):
        for j in range(0,n):
            M[i][j] = A[i][j]+B[i][j]
elif operacao == "-":
    for i in range(0,n):
        for j in range(0,n):
            M[i][j] = A[i][j]-B[i][j]
elif operacao == "*":
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                M[i][j] += A[i][k]*B[k][j]

print("Mat A:")
for i in range(0,n):
    for j in range(0,n):
        print(f"{A[i][j]} ",end="")
    print("\n",end="")
print("Mat B:")
for i in range(0,n):
    for j in range(0,n):
        print(f"{B[i][j]} ", end="")
    print("\n",end="")
print("Resultado:")
for i in range(0,n):
    for j in range(0,n):
        print(f"{M[i][j]} ",end="")
    print("\n",end="")