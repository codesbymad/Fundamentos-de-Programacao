# Escreva um algoritmo que leia um conjunto de n números e mostre qual foi o menor e o maior valor fornecido.

n = int(input())
cont = 1
maior = -999
menor = 999
while cont != n+1:
    num = float(input())
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont = cont + 1
print(f"{menor:.2f}")
print(f"{maior:.2f}")