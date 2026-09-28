# Faça uma função para verificar se um número é um quadrado perfeito. Ex: 1, 4, 9...

def funcao(num):
    quad = num ** 0.5
    if quad % 1 == 0:
        return "True"
    else:
        return "False"

x = float(input(""))
y = funcao(x)
print(f"{y}")