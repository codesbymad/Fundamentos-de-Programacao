# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este numero. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

dia_sem = int(input())
if dia_sem == 1:
    print("Domingo")
elif dia_sem == 2:
    print("Segunda-feira")
elif dia_sem == 3:
    print("Terca-feira")
elif dia_sem == 4:
    print("Quarta-feira")
elif dia_sem == 5:
    print("Quinta-feira")
elif dia_sem == 6:
    print("Sexta-feira")
elif dia_sem == 7:
    print("Sabado")