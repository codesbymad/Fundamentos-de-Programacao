# Faça um programa que receba um valor inteiro n ≥ 0 e imprima se esse número é primo ou não.

n = int(input())
prim = "Primo"
if n <= 0:
    print("Nao primo")
elif n == 1:
    print("Nao primo")
else:
    for i in range(1, n+1):
        result = n % i
        if i != 1:
            if i != n:
                if result == 0:
                    prim = "Nao primo"
    print(prim)