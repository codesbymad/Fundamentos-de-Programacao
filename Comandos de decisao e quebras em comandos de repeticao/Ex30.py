# Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.

qntd = int(input())
cont = 1
contNum = 0
maior = -999999
while cont != qntd+1:
    num = int(input())
    if num > maior:
        maior = num
        contNum = 0
    if num == maior:
        contNum = contNum + 1
    cont = cont + 1
print(maior)
print(contNum)