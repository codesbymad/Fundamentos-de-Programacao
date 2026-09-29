# Faça um algoritmo que, dados dois números inteiros, seja capaz de obter o quociente inteiro da divisão entre o maior e o menor deles. Não use a operação de divisão (/), nem a operação de divisão inteira (//) e nem a operação de resto da divisão inteira (%).

n1 = int(input())
n2 = int(input())
cont = 0
if n1 > n2:
    while n1 >= n2:
        n1 = n1 - n2
        cont = cont + 1
else:
    while n2 >= n1:
        n2 = n2 - n1
        cont = cont + 1
print(cont)