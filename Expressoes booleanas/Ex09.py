# Faça uma função que receba 2 números inteiros positivos e calcule o Mínimo Múltiplo Comum (MMC).

def funcao(num1, num2):
    mmc = 0
    cont = 2
    if num1 > 0 and num2 > 0:
        while mmc == 0:
            if cont % num1 == 0 and cont % num2 == 0:
                mmc = cont
                break
            else:
                cont = cont + 1
    return mmc