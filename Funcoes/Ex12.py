# Faça uma função que receba o salário de um funcionário e calcule o valor do novo salário, sabendo que ele recebeu um aumento de 21,37 %.

def funcao(x):
    n_s = x + (x * (21.37/100))
    return n_s

x = float(input(""))
y = funcao(x)
print(f"{y:.2f}")