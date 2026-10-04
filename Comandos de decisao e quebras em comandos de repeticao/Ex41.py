# Escreva um programa que substitui as ocorrências de um caractere 0 em uma string pelo caractere 1. Não use nenhuma funcionalidade do python que já faça isso.

string = input()
stringNova = ""
for i in range(0, len(string)):
    if string[i] == "0":
        stringNova = stringNova + "1"
    else:
        stringNova = stringNova + string[i]
print(stringNova)