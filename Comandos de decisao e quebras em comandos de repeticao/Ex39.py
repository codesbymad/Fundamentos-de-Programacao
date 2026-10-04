# Escreva um programa que leia duas palavras e diga qual delas vem primeiro na ordem alfabética. Não use nenhuma funcionalidade do python que já faça isso. Dica: ‘a’ é menor do que ‘b’.

palavra1 = input()
palavra2 = input()
iguais = True
if len(palavra1) > len(palavra2):
    for i in range(0, len(palavra2)):
        if palavra1[i] != palavra2[i]:
            if ord(palavra1[i]) < ord(palavra2[i]):
                print(palavra1)
                iguais = False
                break
            else:
                print(palavra2)
                iguais = False
                break
    if iguais == True:
        print(palavra2)
if len(palavra1) < len(palavra2):
    for i in range(0, len(palavra1)):
        if palavra1[i] != palavra2[i]:
            if ord(palavra1[i]) < ord(palavra2[i]):
                print(palavra1)
                iguais = False
                break
            else:
                print(palavra2)
                iguais = False
                break
    if iguais == True:
        print(palavra2)
if len(palavra1) == len(palavra2):
    for i in range(0, len(palavra1)):
        if palavra1[i] != palavra2[i]:
            if ord(palavra1[i]) < ord(palavra2[i]):
                print(palavra1)
                iguais = False
                break
            else:
                print(palavra2)
                iguais = False
                break
    if iguais == True:
        print(palavra1)