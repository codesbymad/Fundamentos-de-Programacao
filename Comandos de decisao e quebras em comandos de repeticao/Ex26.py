# Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

cont = 1
maior = 0
menor = 99
while cont <= 10:
    num = int(input())
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont = cont + 1
print(f"{menor:.2f}")
print(f"{maior:.2f}")