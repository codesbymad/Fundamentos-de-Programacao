# Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário então imprima: "Emprestimo nao concedido", caso contrário imprima: "Emprestimo concedido".

sal_trab = float(input())
val_emp = float(input())
porc = sal_trab * (20/100)
if val_emp > porc :
    print("Emprestimo nao concedido")
else:
    print("Emprestimo concedido")