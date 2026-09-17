'''Escreva uma função que gera um triângulo de altura n e lados 2 × n − 1 . Por exemplo, a saída para n = 6 seria:
*
***
*****
*******
*********
***********
'''

def funcao(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "*" * ((2*i)-1))

x = int(input(""))
funcao(x)