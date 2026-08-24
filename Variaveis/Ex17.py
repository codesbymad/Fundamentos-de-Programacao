#Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.
apos1 = float(input())
apos2 = float(input())
apos3 = float(input())
valpr = float(input())
valrp = valpr/(apos1 + apos2 + apos3)
val1 = valrp*apos1
val2 = valrp*apos2
val3 = valrp*apos3
print(f"{val1:.2f}")
print(f"{val2:.2f}")
print(f"{val3:.2f}")