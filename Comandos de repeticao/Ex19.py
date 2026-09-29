''' Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas como pontos de exclamação, conforme o exemplo abaixo (para n = 5).
!
!!
!!!
!!!!
!!!!!
'''

def funcao(n):
    exc = "!"
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(exc, end="")
        print("")

x = int(input(""))
funcao(x)