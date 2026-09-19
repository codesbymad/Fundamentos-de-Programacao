# Faça uma função que receba um número inteiro positivo de três dígitos (de 100 a 999). Retorne outro número formado pelos dígitos invertidos do número lido. Exemplo: Entrada = 123, Saída = 321. Não utilize strings.

def funcao(x):
    cen = x % 10
    dez = (x // 10) % 10
    uni = x // 100
    mostre = (cen * 100) + (dez * 10) + uni
    return mostre

x = int(input(""))
y = funcao(x)
print(f"{y:0}")
print(type(y))