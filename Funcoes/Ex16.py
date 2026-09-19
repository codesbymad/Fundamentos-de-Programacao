# Faça uma função que receba um valor inteiro positivo em segundos, e retorne-o em horas, minutos e segundos.

def funcao (x):
    hora = x // 3600
    minu = (x % 3600)//60
    segu = x - ((hora * 3600) + (minu * 60))
    return hora, minu, segu

x = int(input(""))
y1,y2,y3 = funcao(x)
print(f"{y1}")
print(f"{y2}")
print(f"{y3}")