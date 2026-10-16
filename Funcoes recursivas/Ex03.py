# Escreva uma função recursiva que calcule a soma dos primeiros n cubos: S(n) = 13 + 23 + … + n3.

def funcao(n):
    if n == 0:
        s = 0
    elif n == 1:
        s = 1
    else:
        s = n ** 3 + funcao(n-1)
    return s