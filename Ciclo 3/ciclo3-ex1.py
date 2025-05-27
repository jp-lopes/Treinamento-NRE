#Crie uma classe chamada "Pessoa" que tenha dois atributos: nome e idade.
#Em seguida, crie um método chamado "apresentar" que exiba uma mensagem apresentando o nome e a idade.
#Depois disso, crie duas pessoas diferentes e utilize o método "apresentar" para cada uma delas.

class Pessoa:
    nome = "."
    idade = 0

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}")

P1 = Pessoa("João",20)
P2 = Pessoa("Maria",26)

print("Apresentando a primeira pessoa: ")
P1.apresentar()
print("Apresentando a segunda pessoa: ")
P2.apresentar()