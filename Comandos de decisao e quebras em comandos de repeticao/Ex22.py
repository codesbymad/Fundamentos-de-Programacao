# Elabore uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra for A, a função deverá calcular a média aritmética das notas do aluno; se for P, deverá calcular a média ponderada, com os pesos 5, 3, 2.

def funcao(n1, n2, n3, carac):
    media = 0
    if carac == "A":
        media = (n1 + n2 + n3)/3
        return media
    if carac == "P":
        media = ((n1 * 5) + (n2 * 3) + (n3 * 2))/ (5 + 3 + 2)
        return media

x1 = float(input(""))
x2 = float(input(""))
x3 = float(input(""))
x4 = input("")
y = funcao(x1, x2, x3, x4)
print(f"{y:.2f}")