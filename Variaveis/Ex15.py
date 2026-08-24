#Leia um valor inteiro positivo em segundos, e imprima-o em horas, minutos e segundos.
segu = int(input())
hora = (segu//60)//60
minu = (segu//60)%60
segs = segu%60
print(hora)
print(minu)
print(segs)