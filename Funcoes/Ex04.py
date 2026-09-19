# Faça uma função que, dado um número inteiro e retorne o seu antecessor e o seu sucessor.

def funcao(x):
    ant = x-1
    suc = x+1
    return ant, suc

x = int(input(""))
y1,y2 = funcao(x)
print(f"{y1}")
print(f"{y2}")