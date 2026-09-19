# Escreva uma função que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.

def funcao(x):
    cem = x // 100
    reg = x % 100
    cinq = reg //50
    reg = reg % 50
    vin = reg//20
    reg = reg % 20
    dez = reg//10
    reg = reg % 10
    cinc = reg//5
    reg = reg % 5
    doi = reg//2
    reg = reg % 2
    return cem, cinq, vin, dez, cinc, doi, reg

x = int(input(""))
y1,y2,y3,y4,y5,y6,y7 = funcao(x)
print(f"{y1}")
print(f"{y2}")
print(f"{y3}")
print(f"{y4}")
print(f"{y5}")
print(f"{y6}")
print(f"{y7}")