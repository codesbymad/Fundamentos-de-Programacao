# Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

import math
num = float(input())
if num > 0:
    raiz_qdd = math.sqrt(num)
    print(f"{raiz_qdd:.2f}")
else:
    print("Numero invalido")