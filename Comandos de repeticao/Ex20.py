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
    for i in range(1, ((alt+1)//2)):
        print("*"*i)
    for i in range(((alt+1)//2), 0, -1):
        print("*"*i)

x = int(input(""))
funcao(x)