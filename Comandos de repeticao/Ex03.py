#Faça um programa que peça ao usuário para digitar 10 valores e mostre a soma deles.
soma = 0
for i in range(0, 10):
    valor = float(input())
    soma = soma + valor
print(f"{soma:.2f}")