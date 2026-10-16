# Faça uma função que receba 2 números inteiros positivos e calcule o Máximo Divisor Comum (MDC).

def funcao(num1, num2):
    mdc = 0
    cont = 1
    if num1 > 0 and num2 > 0:
        if num1 > num2:
            while cont <= num2 :
                if num1 % cont == 0 and num2 % cont == 0:
                    mdc = cont
                cont = cont + 1
        else:
            while cont <= num1 :
                if num1 % cont == 0 and num2 % cont == 0:
                    mdc = cont
                cont = cont + 1
    return mdc