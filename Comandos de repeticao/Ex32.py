# Faça um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da palavra. Imprima a string resultante.

plv = input()
for i in range(0, len(plv)):
    asc = ord(plv[i])
    asc = asc + 1
    car = chr(asc)
    print(car , end="")
print()