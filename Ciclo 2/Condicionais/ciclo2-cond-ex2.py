#Faça um código que, dado o valores dos 3 lados de um triângulo, diga se ele é
#equilátero, isósceles ou escaleno (Para isso, utiliza as estruturas condicionais if,
#elif e else)

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a==b==c: print("Equilátero.")
elif a==b or a==c or b==c: print("Isósceles.")
else: print("Escaleno.")
