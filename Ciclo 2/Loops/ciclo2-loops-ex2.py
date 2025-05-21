#Faça um código que, dado um número, conte quantos números primos existem até ele.
a = int(input("Insira um número: "))
i=1
j=1
cont=0
print("Primos: ",end="")
while i<=a:
    primo=1
    if i==1:
        primo = 1
    else:
        j=1
        while(j<i):
            if i%j==0 and i!=j and j!=1:
                primo = 0
            j+=1
    if primo==1:
        print(f"{i} ", end="")
        cont+=1
    i+=1
print(f"\nExistem {cont} primos entre 0 e {a}")