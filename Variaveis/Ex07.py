#Faça um programa que leia a temperatura em graus Celsius e converta para Fahrenheit. Fórmula: F = C * (9.0/5.0) + 32.
cels = float(input())
fahr = cels*(9.0/5.0)+32
print(f"{fahr:.2f}")