# Faça um algoritmo que leia um número inteiro e imprima seus divisores.

num = int(input())
cont = 1
while cont != num + 1:
    if num % cont == 0:
        print(cont)
    cont = cont + 1