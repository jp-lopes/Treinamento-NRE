#Faça uma lista de 10 alunos, então o usuário deve inserir uma 
#posição e o programa deve dizer qual aluno está naquela posição da lista.

alunos = ["João0", "João1", "João2", "João3", "João4", "João5", "João6", "João7", "João8", "João9"]
posicao = int(input("Insira uma posição: "))
if posicao < 0 or posicao > 9: print("Posição inválida.")
else: print(f"Aluno na posição {posicao}: {alunos[posicao]}")
