#Faça uma função que receba um valor inteiro n ≥ 0 e calcule o seu fatorial n!. Lembrete: 0! = 1.
def funcao(n):
    fat = 1
    for i in range(n, 0, -1):
        fat = fat*i
    return fat

x = int(input(""))
y = funcao(x)
print(f"{y}")