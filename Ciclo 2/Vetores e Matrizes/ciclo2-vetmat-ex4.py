#Escreva uma função que verifique se uma dada matriz é uma matriz identidade.
n = int(input("Tamanho da matriz: "))
M = [[0]*(n) for i in range(n)]
identidade = True
print("Insira os valores da matriz por linha: ")
for i in range(0,n):
    for j in range(0,n):
        M[i][j] = int(input())
        if (i<j or i>j) and M[i][j]!= 0: identidade = False
        if (i==j) and M[i][j]!= 1: identidade = False
print("A Matriz:")
for i in range(0,n):
    for j in range(0,n):
        print(f"{M[i][j]} ",end="")
    print("\n",end="")
if identidade: print("É uma matriz identidade.")
else: print("Não é uma matriz identidade")