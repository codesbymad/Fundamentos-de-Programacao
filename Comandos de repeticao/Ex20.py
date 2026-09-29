'''Escreva uma função que gera um triângulo lateral de altura 2 × n − 1 e n de largura. Por exemplo, a saída para n = 4 seria:
*
**
***
****
***
**
* '''

def funcao(n):
    alt = (2*n)-1
    for i in range(1, n):
        for j in range(1, i+1):
            print("*", end="")
        print("")
    for i in range(n, 0, -1):
        for k in range(i, 0, -1):
            print("*", end="")
        print("")

x = int(input(""))
funcao(x)