#Construa um programa que leia duas strings fornecidas pelo usuário e verifique se a segunda string lida está contida no final da primeira, retornando o resultado da verificação.
string1 = input()
string2 = input()
result = string1.endswith(string2)
print(result)