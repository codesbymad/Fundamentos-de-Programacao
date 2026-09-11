#Escreva uma função que receba n e k tais que n ≥ k ≥ 0 e calcule o coeficiente binomial Cn,k = n!/(k!*(n-k)!)
def funcao(n, k):
    fatN = 1
    fatK = 1
    lm = n-k
    fatLm = 1
    for i in range(n, 0, -1):
        fatN = fatN * i
    for i in range(k, 0, -1):
        fatK = fatK * i
    for i in range(lm, 0, -1):
        fatLm = fatLm * i
    c_n_k = fatN/(fatK*fatLm)
    return c_n_k

x1 = int(input())
x2 = int(input())
y = funcao(x1, x2)
print(f"{y}")