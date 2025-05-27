#Crie uma classe chamada "Retângulo" que tenha dois atributos: largura e altura. 
#Depois, crie um método que calcule a área (largura vezes altura) e outro que calcule o perímetro 
#(soma de todos os lados, ou seja: 2 vezes a largura mais 2 vezes a altura). 
#Crie um retângulo, e use os métodos para mostrar a área e o perímetro.

class Retangulo:
    largura = 0.0
    altura = 0.0

    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return (self.largura * self.altura)

    def perimetro(self):
        return (2*self.largura + 2*self.altura)

R = Retangulo(10,5.6)
print(f"Altura: {R.altura:.2f}, Largura: {R.largura:.2f}")
area = R.area()
print(f"Área: {area:.2f}")
perimetro = R.perimetro()
print(f"Perímetro: {perimetro:.2f}")
