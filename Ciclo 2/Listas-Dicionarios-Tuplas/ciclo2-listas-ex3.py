#Faça um dicionário associando 20 alunos e suas notas na P1 de cálculo 1 (valores e nomes imaginários), 
#então quando o usuário inserir um nome, o código deve dizer a nota do aluno.

notas = dict()
for i in range(0,20):
    nome = "Joao" + (str)(i)
    notas[nome] = i % 10
nome = input("Insira um nome: ")
print(f"Nota: {notas[nome]}")