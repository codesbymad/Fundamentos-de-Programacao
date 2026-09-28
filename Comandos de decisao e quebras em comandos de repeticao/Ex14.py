''' Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
◦ adição (opção 1)
◦ subtração (opção 2)
◦ multiplicação (opção 3)
◦ divisão (opção 4)
◦ saída (opção 5)
O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções. O programa só termina quando for escolhida a opção de saída (opção 5). '''

opc = 0

while opc != 5:
    print("1 - Adicao")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Saida")
    opc = int(input())
    resp = 0
    if opc == 5:
        continue
    else:
        n1 = float(input())
        n2 = float(input())
        if opc == 1:
            resp = n1 + n2
            print(f"{resp:.2f}")
        elif opc == 2:
            resp = n1 - n2
            print(f"{resp:.2f}")
        elif opc == 3:
            resp = n1 * n2
            print(f"{resp:.2f}")
        elif opc == 4:
            resp = n1 / n2
            print(f"{resp:.2f}")