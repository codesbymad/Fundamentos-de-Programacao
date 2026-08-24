#Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo). A fórmula de conversão é: M = K/3.6 , sendo K a velocidade em km/h e M em m/s.
velK = float(input())
velM = velK/3.6
print(f"{velM:.2f}")