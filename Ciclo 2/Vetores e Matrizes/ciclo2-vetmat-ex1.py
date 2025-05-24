##Escreva um código em python que receba um vetor e um escalar, 
# multiplique aquele vetor pelo escalar e printe o resultado.

tamvetor = int(input("Tamanho do vetor: "))
vetor = []
print("Insira o vetor: ")
for i in range(0,tamvetor):
    vetor.append(int(input()))
escalar = int(input("Insira o escalar: "))
for i in range(0,tamvetor):
    vetor[i] *= escalar
print(f"Vetor*escalar: {vetor}")