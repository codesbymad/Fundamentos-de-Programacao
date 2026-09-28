# Faça uma função que receba dois números e retorne qual deles é o maior.

def funcao(n1, n2):
    if n1 > n2:
        return n1
    if n2 > n1:
        return n2
    if n1 == n2:
        return n1

x1 = float(input(""))
x2 = float(input(""))
y = funcao(x1, x2)
print(f"{y:.2f}")