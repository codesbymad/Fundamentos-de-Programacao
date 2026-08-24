#Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha. Não utilize strings.
num = int(input()) 
mil = num//1000
cen = (num//100)%10
dez = (num//10)%10
uni = num%10
print(mil)
print(cen)
print(dez)
print(uni)