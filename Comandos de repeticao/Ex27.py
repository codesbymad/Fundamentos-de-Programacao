# Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o fatorial exponencial desse número. Um fatorial exponencial é um inteiro positivo n elevado à potência de n − 1 , que por sua vez é elevado à potência de n − 2 e assim por diante. Ou seja: n(n−1)^(n−2)^···^1.

def funcao(n):
    pot = 1
    for i in range(0, n):
        pot = i ** pot
    fatExp = n**pot
    return fatExp

x = int(input(""))
y = funcao(x)
print(f"{y}")