# Elabore uma função para calcular o volume (V) de uma esfera e a área (A) de sua superfície, dado o valor de seu raio (R). A fórmula do volume da esfera é V = 4/3 πR3 e A = 4πR2 .

import math

def funcao(x):
    y1 = 4/3 * math.pi * x ** 3
    y2 = 4 * math.pi * x ** 2
    return y1, y2

x = float(input(""))
y1,y2 = funcao(x)
print(f"{y1:.2f}")
print(f"{y2:.2f}")