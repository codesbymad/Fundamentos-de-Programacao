# Faça uma função chamada de simplificada que receba como parâmetro o numerador e o denominador de uma fração. Esta função deve simplificar a fração recebida dividindo o numerador e denominador pelo maior fator possível. Por exemplo, a fração 36/60 simplificada para 3/5 dividindo o numerador e denominador por 12.

def simplificar(num, den):
    divisor = 0
    if num > den:
        for i in range(1, num+1):
            if num % i == 0:
                if den % i == 0:
                    divisor = i
    else:
        for i in range(1, den+1):
            if den % i == 0:
                if num % i == 0:
                    divisor = i
    numSimp = int(num/divisor)
    denSimp = int(den/divisor)
    return numSimp, denSimp

x1 = int(input(""))
x2 = int(input(""))
y1, y2 = simplificar(x1, x2)
print(f"{y1}")
print(f"{y2}")