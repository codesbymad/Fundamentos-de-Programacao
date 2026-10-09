# Faça um programa que receba uma palavra e um caractere (vogal ou consoante) e imprima quantas vogais (a, e, i, o, u) possui essa palavra. Substitua todas as vogais da palavra dada pelo caractere dado, e imprima a nova palavra.

palavra = input()
caractere = input()
vogais = 0
palavraNova = ""
for letra in range(0, len(palavra)):
    if palavra[letra] == "a" or palavra[letra] == "e" or palavra[letra] == "i" or palavra[letra] == "o" or palavra[letra] == "u" or palavra[letra] == "A" or palavra[letra] == "E" or palavra[letra] == "I" or palavra[letra] == "O" or palavra[letra] == "U":
        vogais = vogais + 1
        palavraNova = palavraNova + caractere
    else:
        palavraNova = palavraNova + palavra[letra]
print(vogais)
print(palavraNova)