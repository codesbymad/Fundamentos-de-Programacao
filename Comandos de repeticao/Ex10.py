#Faça uma função que receba um inteiro x e um inteiro não-negativo n e, usando laço de repetição, calcule xn e retorne o resultado.
import math
def funcao(x, n):
    result = 0
    for i in range(0, n+1):
        result = x**i
    return result

x1 = int(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y}")