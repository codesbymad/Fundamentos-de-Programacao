'''Escreva uma função que gera um triângulo de altura n e lados 2 × n − 1 . Por exemplo, a saída para n = 6 seria:
*
***
*****
*******
*********
***********
'''

def funcao(n):
    for i in range(0, n):
        for j in range(1, n-i):
            print(" ", end="")
        for j in range(1, (i+1)*2):
            print("*", end="")
        print()

x = int(input(""))
funcao(x)