#Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado pelos dígitos invertidos do número lido. Exemplo: Número Lido = 123, Número Gerado = 321. Não utilize strings.
num = int(input()) 
uni = num%10 
dez = (num//10)%10
cen = num//100
result = (uni*100) + (dez * 10) + cen
print(result)