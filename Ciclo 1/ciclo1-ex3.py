#3.Faça um código que, ao colocar uma temperatura em graus, calcule quanto que vale essa temperatura em kelvin e fahrenheit
c = float(input("Insira a temperatura em graus celsius: "))
k = c + 273.15
f = (c*(9/5))+32
print(f"Temperatura em Kelvin: {k:.2f}K\nTemperatura em Fahrenheit: {f:.2f}F")