# Crie uma função recursiva que receba dois inteiros positivos n e k e calcule nk.

def funcao(n, k):
    if k == 0:
        nk = 1
    elif k == 1:
        nk = n
    else:
        nk = n * funcao(n, k - 1)
    return nk