#Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: R = G * π/180 , sendo G o ângulo em graus e R em radianos.
ang = float(input())
pi = 3.14159265359
rad = ang * pi/180
print(f"{rad:.2f}")