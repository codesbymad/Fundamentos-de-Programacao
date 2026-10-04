# Faça um programa que conte o número de 1’s que aparecem em uma string. Exemplo: 0011001 -> 3. Não use nenhuma funcionalidade do python que já faça isso.

string = input()
quant = 0
for i in range(0, len(string)):
    if string[i] == "1":
        quant = quant + 1
print(quant)