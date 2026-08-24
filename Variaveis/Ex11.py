#Faça um programa que receba o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 21,37 %.
salA = float(input())
salN = salA + (salA * (21.37/100))
print(f"{salN:.2f}")