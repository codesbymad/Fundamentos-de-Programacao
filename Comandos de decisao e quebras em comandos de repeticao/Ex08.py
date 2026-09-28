''' Faça um programa que receba dois números e execute as operações listadas a seguir de acordo com a escolha do usuário:
◦ 1: Média entre os números digitados
◦ 2: Diferença do maior pelo menor
◦ 3: Produto entre os números digitados
◦ 4: Divisão do primeiro pelo segundo
Se a opção digitada for inválida, mostrar uma mensagem de erro e terminar a execução do programa. Dica do Brother: Na operação 4 o segundo número deve ser diferente de 0.'''

n1 = float(input())
n2 = float(input())
oprc = int(input())
resp = 0
if oprc <= 0:
    print("Erro")
elif oprc > 4:
    print("Erro")
elif oprc == 1:
    resp = (n1 + n2)/2
    print(f"{resp:.2f}")
elif oprc == 2:
    if n1 > n2:
        resp = n1 - n2
        print(resp)
    else:
        resp = n2 - n1
        print(resp)
elif oprc == 3:
    resp = n1 * n2
    print(f"{resp:.2f}")
else:
    if n2 != 0:
        resp = n1 / n2
        print(f"{resp:.2f}")
    else:
        print("Erro")