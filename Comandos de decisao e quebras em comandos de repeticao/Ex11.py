# Faça um programa que simule uma calculadora com as 4 operações básicas. O usuário digita o primeiro número, escolhe a operação e em seguida digita o segundo número, exatamente nessa ordem. O programa deve mostrar o resultado da operação.

n1 = float(input())
oper_bas = input()
n2 = float(input())
resp = 0
if oper_bas == "+":
    resp = n1 + n2
    print(resp)
elif oper_bas == "-":
    resp = n1 - n2
    print(resp)
elif oper_bas == "*":
    resp = n1 * n2
    print(f"{resp:.2f}")
elif oper_bas == "/":
    resp = n1 / n2
    print(f"{resp:.2f}")