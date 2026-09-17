#Faça uma função que, dado um valor N inteiro e positivo, calcule o valor de E, conforme a fórmula a seguir: E = 1 + 1/1! + 1/2! + 1/3! . . . 1/n!.

def funcao(n):
    e = 1
    for i in range(1, n+1):
        fat = 1
        for f in range(i, 0, -1):
            fat = fat*f
        e = e + (1/fat)
    return e

x = int(input(""))
y = funcao(x)
print(f"{y:.8f}")