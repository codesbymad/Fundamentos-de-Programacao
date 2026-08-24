#Crie um programa que permita fazer a conversão cambial entre Dólares e Reais. Considere como taxa de câmbio US$ 1,00 = R$5,27. Leia um valor em Dólares pelo teclado e mostre o correspondente em Reais.
dolar = float(input())
real = 5.27
conv = dolar * real
print(f"{conv:.2f}")