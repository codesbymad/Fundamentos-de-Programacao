# Faça uma função que, dado o tamanho do lado de um quadrado e retorne a sua área.

import math

def funcao(x):
    y = math.pow(x,2)
    return y

x = float(input(""))
y = funcao(x)
print(f"{y:.2f}")