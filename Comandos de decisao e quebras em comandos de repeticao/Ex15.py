# Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele próprio. Exemplo: a soma dos divisores de 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78.

num = int(input())
cont = 1
soma = 0
while cont != num:
    if num % cont == 0:
        soma = soma + cont
    cont = cont + 1
print(soma)