#Faça uma função que calcule e retorne a soma dos N primeiros números pares (considere o 0 como o primeiro número par).
def funcao(n):
    soma = 0
    somaTotal = 0
    for i in range(0, n):
        somaTotal = somaTotal + soma
        soma = soma + 2
    return somaTotal

x = int(input(""))
y = funcao(x)
print(f"{y}")