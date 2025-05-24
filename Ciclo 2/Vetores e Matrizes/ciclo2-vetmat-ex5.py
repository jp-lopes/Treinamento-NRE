#Escreva um código em python que dada uma matriz quadrada, calcule seu determinante.

import numpy as np
n = int(input("Tamanho da matriz: "))
M = [[0]*(n) for i in range(n)]
for i in range(0,n):
    for j in range(0,n):
        M[i][j] = int(input())
M = np.array(M)
det = np.linalg.det(M)
print(f"Determinante: {det:.2f}")