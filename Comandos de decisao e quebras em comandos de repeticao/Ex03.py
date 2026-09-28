# Ler 4 números inteiros e calcular a soma dos que forem par.

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
soma = 0

if n1 % 2 == 0:
    soma = soma + n1
if n2 % 2 == 0:
    soma = soma + n2
if n3 % 2 == 0:
    soma = soma + n3
if n4 % 2 == 0:
    soma = soma + n4
    
print(soma)