# Faça uma função que receba um número inteiro positivo P e retorne a soma dos algarismos de P! . Exemplo: Se P = 4 , P! = 24 . Logo, a soma de seus algarismos é 2 + 4 = 6.

def funcao(p):
    fat = 1
    soma = 0
    for i in range(p, 0, -1):
        fat = fat * i
    for i in range(0, p):
        soma = soma + (fat%10)
        fat = fat//10
    return soma

x = int(input(""))
y = funcao(x)
print(f"{y}")