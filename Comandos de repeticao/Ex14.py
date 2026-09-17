# Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmônica: H(n) = 1/1 + 1/2 + 1/3 … 1/n. Faça uma função que, dado um valor n inteiro positivo, calcule o valor de H(n).

def funcao(n):
    h = 0
    for i in range(1, n+1):
        h = h + 1/i
    return h

x = int(input(""))
y = funcao(x)
print(f"{y:.2f}")