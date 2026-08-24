#Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule sua distância da origem (0, 0).
cordx = float(input())
cordy = float(input())
x = cordx**2
y = cordy**2
resul = (x + y)**0.5
print(f"{resul:.2f}")