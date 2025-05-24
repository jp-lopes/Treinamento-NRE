#Crie uma função chamada “calcular média” que receba 
#três notas (valores do tipo float) como parâmetros e retorne a média aritmética dessas notas.

def calcularmedia(n1,n2,n3):
    media = (n1+n2+n3)/3
    return media

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = calcularmedia(n1,n2,n3)
print(f"Média: {media:.2f}")