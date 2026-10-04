# Escreva um programa que leia a idade e o primeiro nome de várias pessoas. Seu programa deve terminar quando uma idade negativa for digitada. Ao terminar, seu programa deve escrever o nome e a idade das pessoas mais jovens e mais velhas.

idade = 0
idadeMaior = 0
idadeMenor = 99
nomeMaior = ""
nomeMenor = ""
while idade >= 0:
    nome = input()
    idade = int(input())
    if idade >= 0:
        if idade > idadeMaior:
            nomeMaior = nome
            idadeMaior = idade
        if idade < idadeMenor:
            nomeMenor = nome
            idadeMenor = idade
    else:
        continue
print(nomeMenor)
print(idadeMenor)
print(nomeMaior)
print(idadeMaior)