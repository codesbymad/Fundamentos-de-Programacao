# Ler uma frase e contar quantos caracteres são brancos. Não use nenhuma funcionalidade do python que já faça isso.

frase = input()
cont = 0
for i in range(0, len(frase)):
    if frase[i] == " ":
        cont = cont + 1
print(cont)