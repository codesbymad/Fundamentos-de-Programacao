# Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva, para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.

num = 1
while num > 0:
    num = float(input())
    if num <= 0:
        continue
    else:
        quad = num ** 2
        print(f"{quad:.2f}")
        cubo = num ** 3
        print(f"{cubo:.2f}")
        raiz = num ** 0.5
        print(f"{raiz:.2f}")