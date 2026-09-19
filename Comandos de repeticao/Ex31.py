# Implemente um programa que leia duas strings, str1 e str2, e um valor inteiro positivo N. Concatene N vezes a string str2 ao final da string str1.

str1 = input()
str2 = input()
n = int(input())
conc = ""
print(str1, end="")
for i in range(1, n+1):
    conc = conc + str2
print(conc)