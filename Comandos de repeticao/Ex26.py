# Faça uma função que receba como parâmetro o ângulo x (em radianos) e um valor inteiro positivo n . Calcule o valor do seno desse ângulo usando a respectiva série de Taylor: sin(x) = x – x3/3! + x5/5! - … + (-1)n (x2n+1)/(2n+1)!.

def funcao(x, n):
    taylor = x
    for i in range(1, n+1):
        fat = 1
        fatN = (2*i+1)
        for j in range(fatN, 0, -1):
            fat = fat*j
        taylor = taylor + ((-1)**i)*(x**((2*i)+1))/fat
    return taylor

x1 = float(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y:.8f}")