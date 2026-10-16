# Faça uma função recursiva que receba um número inteiro positivo n e imprima todos os números naturais de 0 até n em ordem decrescente.

def funcao(n):
    print(n)
    if n == 0:
        mostre = 0
    else:
        mostre = n - funcao(n-1)
    return mostre