#Crie uma classe chamada Animal que tenha um atributo chamado nome e um método chamado falar, 
#que apenas imprime a mensagem: “Este animal faz algum som”.
  
#Depois, crie duas classes chamadas Cachorro e Gato que herdam da classe Animal. 
#Cada uma deve ter seu próprio método falar, que substitui (sobrescreve) o da classe base.
 
#Por fim, crie um objeto de cada classe (um cachorro e um gato), e chame o método falar para cada um deles.

class Animal:
    nome = "."

    def __init__(self,nome):
        self.nome = nome
    
    def falar(self):
        print("Este animal faz algum som.")

class Gato(Animal):
    def falar(self):
        print(f"Nome do animal: {self.nome}")
        print("Som: Miau")

class Cachorro(Animal):
    def falar(self):
        print(f"Nome do animal: {self.nome}")
        print("Som: AuAu")

A1 = Gato("Garfield")
A2 = Cachorro("Totó")

A1.falar()
A2.falar()