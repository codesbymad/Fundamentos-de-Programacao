# Faça uma função que, a partir das medidas dos lados de um retângulo, calcule a área e o perímetro deste retângulo.

def funcao(x1, x2):
    a = x1 * x2
    p = (x1 * 2) + (x2 *2)
    return a, p

x1 = float(input(""))
x2 = float(input(""))
y1, y2 = funcao(x1, x2)
print(f"{y1:.2f}")
print(f"{y2:.2f}")