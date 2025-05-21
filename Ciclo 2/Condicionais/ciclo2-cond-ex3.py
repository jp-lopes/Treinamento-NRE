#Faça um código que pergunte ao usuário seu Número USP e então diga em qual
#ano ele entrou na faculdade

#Assumindo que começo do nusp 15 => 024, 14 => 023 etc
nusp = input("Número USP: ")
doisdigitos = int(nusp[0]+nusp[1])
ano = doisdigitos + 9
print(f"{ano:03}")
