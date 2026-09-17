# Faça um programa que desenhe uma linha na tela usando vários símbolos de igual (Ex: ========). O programa deve ler quantos sinais de iguais serão mostrados.

qnt = int(input())
igual = ""
for i in range(0, qnt):
    igual = igual + "="
print(igual)