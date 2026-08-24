#Faça um programa que receba um valor em R$ que será dividido entre três ganhadores de um concurso. Sendo que da quantia total:
#◦ O primeiro ganhador receberá 46%;
#◦ O segundo ganhador receberá 32%;
#◦ O terceiro receberá o restante;
#Calcule e imprima a quantia ganha por cada um dos ganhadores.
prem = float(input())
gan1 = prem * (46/100)
gan2 = prem * (32/100)
gan3 = prem - (gan1 + gan2)
print(f"{gan1:.2f}")
print(f"{gan2:.2f}")
print(f"{gan3:.2f}")