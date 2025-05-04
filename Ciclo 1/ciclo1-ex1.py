#1.Faça um código que resolva qualquer equação de segundo grau
import math
print("Insira os coeficientes (ax^2+bx+c):")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
print(f"EQUAÇAO: f(x)={a}x^2+{b}x+{c}")
delta = b*b - 4*a*c
#print(f"Delta: {delta}")
i = 0
if delta > 0:
    raiz1 = (-1*b - math.sqrt(delta))/(2*a)
    raiz2 = (-1*b + math.sqrt(delta))/(2*a)
elif delta == 0:
    raiz1 = (-1*b)/(2*a)
    raiz2 = raiz1
else:
    raiz1 = raiz2 = (-1*b)/(2*a)
    i = (math.sqrt(abs(delta)))/(2*a)
    
if i == 0: 
    print(f"RAIZES:\nx1: {raiz1:.2f}\nx2: {raiz2:.2f}")
else:
    print(f"RAIZES:\nx1: {raiz1:.2f} + {i:.2f}i\nx2: {raiz2:.2f} - {i:.2f}i")