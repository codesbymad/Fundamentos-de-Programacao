# O numero 3025 possui uma característica interessante, sendo a seguinte: 30 + 25 = 55 e 552 = 3025. Elaborar um algoritmo que verifique todos os números de quatro algarismos que apresentem essa propriedade. Não use operações com strings.

cont = 1000
while cont != 10000:
    primParte = cont // 100
    segnParte = cont % 100
    soma = primParte + segnParte
    quad = soma ** 2
    if quad == cont:
        print(cont)
    cont = cont + 1