#Faça um programa que calcule e escreva o valor de S = 1/1 + 3/2 + 5/3 + 7/4 + … + 99/50.

s = 0
n = 1
d = 0
for d in range(1, 51):
    s = s + (n/d)
    n = n + 2
print(f"{s:.10f}")
