# Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo. O programa tem que retornar o maior e o menor número lido.

num = 0
maior = 0
menor = 9
while num >= 0:
    num = int(input())
    if num < 0:
        continue
    if num > maior:
        maior = num
    if num < menor:
        menor = num
if maior != 0:
    print(maior)
    print(menor)