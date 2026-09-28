# Faça um programa que leia 3 notas, verifique se as notas são válidas e exiba na tela a média destas notas com duas casas decimais. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.00 e 10.00, onde caso a nota não possua valor válido, este fato deve ser informado ao usuário e o programa termina.

nota1 = float(input())
if nota1 < 0.0:
    print("Nota invalida")
elif nota1 > 10.0:
    print("Nota invalida")
else:
    nota2 = float(input())
    if nota2 < 0.0:
        print("Nota invalida")
    elif nota2 > 10.0:
        print("Nota invalida")
    else:
        nota3 = float(input())
        if nota3 < 0.0:
            print("Nota invalida")
        elif nota3 > 10.0:
            print("Nota invalida")
        else:
            media = (nota1 + nota2 + nota3)/3
            print(f"{media:.2f}")