# Faça uma função que receba um número inteiro de 4 dígitos (de 1000 a 9999) e retorne os 4 dígitos separados, cada um em uma variável diferente. Não utilize strings.

def funcao(x):
    mil = x // 1000
    cen = (x // 100) % 10
    dez = (x % 100) //10
    uni = x % 10
    return mil, cen, dez, uni

x = int(input(""))
y1,y2,y3,y4 = funcao(x)
print(f"{y1:0}")
print(f"{y2:0}")
print(f"{y3:0}")
print(f"{y4:0}")
print(type(y1))
print(type(y2))
print(type(y3))
print(type(y4))