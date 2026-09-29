# Faça uma função que retorne o maior fator primo de um número.

def funcao(n):
    num = 0
    for i in range(1, n+1):
        primo = True
        if n % i == 0:
            for j in range(1, i+1):
                result = i % j
                if j != 1:
                    if j != i:
                        if result == 0:
                            primo = False
            if primo == True:
                num = i
            
    return num