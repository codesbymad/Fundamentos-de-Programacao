# Faça um programa que receba uma palavra e a imprima de trás-para-frente.

plv = input()
for i in range((len(plv))-1, -1, -1):
    print(plv[i], end="")
print()

