# questãoFaça um programa que receba uma frase e imprima-a de maneira invertida, trocando as letras A (maiúsculas ou minúsculas) por *. Não use nenhuma funcionalidade do python que já faça isso.

frase = input()
fraseNova = ""
for i in range(len(frase)-1, -1, -1):
    if frase[i] == "a":
        fraseNova = fraseNova + "*"
    elif frase[i] == "A":
        fraseNova = fraseNova + "*"
    else:
        fraseNova = fraseNova + frase[i]
print(fraseNova)