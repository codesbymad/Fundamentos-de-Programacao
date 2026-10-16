# Crie uma função recursiva que receba um número inteiro positivo n e calcule o somatório dos números de 1 até n.

def funcao(n):
    if n == 1:
        soma = 1
    else:
        soma = n + funcao(n-1)
    return soma