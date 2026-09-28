''' Calcule as raízes da equação do 2o grau. Lembrando que: x = (−b± √∆)/(2a), onde ∆ = b2 − 4ac, e  ax2 + bx + c = 0 representa uma equação do 2o grau. A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Nao eh equacao do 2o grau".
◦ Se ∆ < 0 , não existe raiz real. Imprima a mensagem “Nao existe raiz real”.
◦ Se ∆ = 0 , existe uma raiz real. Imprima a raiz e a mensagem "Raiz unica".
◦ Se ∆ > 0 , Imprima as duas raízes reais. '''

def raizes(a, b, c):
    delta = (b**2) - (4 * a * c)
    if delta < 0:
        return "n", 0, 0
    elif delta == 0:
        x1 = (-b + delta**0.5)/(2*a)
        return "z", x1, 0 
    else:
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        return "p", x1, x2

a = float(input())
if a != 0:
    b = float(input())
    c = float(input())
    
    carac ,x1, x2 = raizes(a, b, c)
    if carac == "n":
        print("Nao existe raiz real")
    elif carac == "z":
        print(f"{x1:.2f}")
        print("Raiz unica")
    else:
        print(f"{x1:.2f}")
        print(f"{x2:.2f}")
else:
    print("Nao eh equacao do 2o grau")