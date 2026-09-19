# Faça uma função que converta a temperatura de graus Celsius para Fahrenheit. Fórmula: F = C * (9.0/5.0) + 32.

def funcao(x):
    f = x * 9/5 + 32
    return f

x = float(input(""))
y = funcao(x)
print(f"{y:.2f}")