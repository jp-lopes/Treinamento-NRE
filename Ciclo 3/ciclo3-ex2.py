#Crie uma classe chamada "Aluno" que tenha três atributos: nome, nota1 e nota2. 
#Crie um método que calcule a média das duas notas. 
#Depois, crie um segundo método que verifique se o aluno foi aprovado (média maior ou igual a 6). 
#O método deve imprimir "Aprovado" ou "Reprovado", dependendo da média. 
#Crie dois alunos diferentes e verifique a situação de cada um.

class Aluno:
    nome = "."
    nota1 = 0.0
    nota2 = 0.0

    def __init__(self,nome,nota1,nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    
    def media(self):
        media = (self.nota1 + self.nota2) /2
        return media
    
    def situacao(self):
        media = self.media()
        if media >= 6: 
            situacao = "Aprovado"
        else: 
            situacao = "Reprovado"
        print(f"Nome: {self.nome}\nMédia: {media}\nSituação: {situacao}")

A1 = Aluno("João",10,0)
A2 = Aluno("Maria",9,3)

print("Situação do aluno 1: ")
A1.situacao()
print("Situação do aluno 2: ")
A2.situacao()