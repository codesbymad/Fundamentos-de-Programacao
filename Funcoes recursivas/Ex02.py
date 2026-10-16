# Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro n.

def funcao(n):
    if n == 0:
        result = 1
    else:
        result = n * funcao(n-1)
    return result