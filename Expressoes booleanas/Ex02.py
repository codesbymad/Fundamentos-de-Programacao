# Faça um programa que receba do usuário uma string. O programa imprime a string sem suas vogais.

string = input()
for i in range(0, len(string)):
    if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u" or string[i] == "A" or string[i] == "E" or string[i] == "I" or string[i] == "O" or string[i] == "U":
        print(end="")
    else:
        print(string[i], end="")
print()