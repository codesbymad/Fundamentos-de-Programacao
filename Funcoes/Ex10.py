# Crie uma função que, dado um ângulo em graus, retorne-o convertido em radianos. A fórmula de conversão é: R = G * π/180 , sendo G o ângulo em graus e R em radianos.

import math

def funcao(x):
    r = x * math.pi / 180
    return r

x = float(input(""))
y = funcao(x)
print(f"{y:.2f}")