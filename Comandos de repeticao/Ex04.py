#Faça um programa que leia 10 inteiros e imprima sua média.
inteiro = 0
soma = 0
for i in range(0, 10):
    inteiro = int(input())
    soma = soma + inteiro
media = soma/10
print(f"{media:.2f}")