#Faça um programa em que troque todas as ocorrências de uma letra L1 pela letra L2 em uma string. A string e as letras L1 e L2 devem ser fornecidas pelo usuário.
string = input()
l1 = input()
l2 = input()
troca = string.replace(l1, l2)
print(troca)