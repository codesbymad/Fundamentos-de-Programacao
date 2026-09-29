# Escreva um programa que gera todos os números entre 1000 − 1999 e mostra aqueles que divididos por 11 dão resto 5.

cont = 1000
while cont != 1999:
    if cont % 11 == 5:
        print(cont)
    cont = cont + 1