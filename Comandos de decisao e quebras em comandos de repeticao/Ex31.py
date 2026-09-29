''' Faça um programa que receba dois números. Calcule e mostre:
◦ A soma dos números pares desse intervalo de números (intervalo incluindo os números dados);
◦ A multiplicação dos números ímpares desse intervalo (intervalo incluindo os números dados) '''

n1 = int(input())
n2 = int(input())
soma = 0
prod = 1
if n1 < n2:
    for i in range(n1, n2+1):
        if i%2==0:
            soma = soma + i
        else:
            prod = prod * i
else:
    for i in range(n1, n2-1, -1):
        if i%2==0:
            soma = soma + i
        else:
            prod = prod * i
print(soma)
print(prod)