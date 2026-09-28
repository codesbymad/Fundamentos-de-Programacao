# Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.

soma = 0
div = 0
while div != 10:
    num = int(input())
    if num > 0:
        soma = soma + num
        div = div + 1
if div != 0:
    media = soma / div
    print(f"{media:.2f}")