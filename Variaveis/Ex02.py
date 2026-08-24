#Faça um programa que, a partir das medidas dos lados de um retângulo, lidos via teclado, calcule a área e o perímetro deste retângulo.
base = float(input())
altu = float(input())
area = base * altu
peri = (2*base) + (2*altu)
print(f"{area:.2f}")
print(f"{peri:.2f}")