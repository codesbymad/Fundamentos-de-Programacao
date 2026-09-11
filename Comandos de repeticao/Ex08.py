#Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.
n = int(input())
impar = 1
for i in range(0, n):
    print(impar)
    impar = impar+2