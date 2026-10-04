# Crie uma função que diga se duas strings são iguais ou não, analisando caractere a caractere.

def funcao(str1, str2):
    iguais = True
    if len(str1) != len(str2):
        iguais = False
    else:
        for i in range(0, len(str1)):
            if str1[i] != str2[i]:
                iguais = False
    return iguais

x1 = input("")
x2 = input("")
y = funcao(x1, x2)
print(f"{y}")