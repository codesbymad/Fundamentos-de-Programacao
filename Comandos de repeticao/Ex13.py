''' O número de Fibonacci Fn para n > 0 é definido da seguinte maneira:
◦ F1 = 1
◦ F2 = 1
◦ Fn = Fn−1 + Fn−2 para n> 2
Faça uma função que receba um valor inteiro n e calcule e Fn.'''

def funcao(n):
    a = 1
    b = 1
    for i in range(1, n-1):
        f = a + b
        a = b
        b = f
    return b

x = int(input(""))
y = funcao(x)
print(f"{y}")