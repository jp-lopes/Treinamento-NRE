#Faça uma lista de caracteres com o gabarito das 10 questões de uma prova, 
#então insira uma nova lista com as respostas do aluno. Imprima então quantas questões o aluno acertou.

gabarito = ["a","e","c","d","b","b","a","e","e","d"]
respostas = []
acertos = 0
for i in range(0,10):
    respostas.append(input(f"Resposta da questão {i+1}: "))
    if respostas[i] == gabarito[i]: acertos+=1
print(f"Acertos: {acertos}")

