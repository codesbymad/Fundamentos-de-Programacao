# Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou por 5, mas não simultaneamente pelos dois.

numInt = int(input())
div = False
if (numInt % 3 == 0 and numInt % 5 != 0) or (numInt % 5 == 0 and numInt % 3 != 0):
    div = True
print(div)