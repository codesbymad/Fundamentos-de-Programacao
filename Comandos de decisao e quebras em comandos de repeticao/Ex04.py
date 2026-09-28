# Ler três valores e determinar o maior entre eles.

n1 = float(input())
n2 = float(input())
n3 = float(input())

if n1 > n2:
    if n1 > n3:
        print(n1)
    else:
        print(n3)
elif n2 > n1:
    if n2 > n3:
        print(n2)
    else:
        print(n3)
elif n3 > n1:
    if n3 > n2:
        print(n3)
    else:
        print(n2)
elif n1 == n2:
    if n1 == n3:
        print(n1)
    elif n1 < n3:
        print(n3)
    else:
        print(n2)
elif n2 == n3:
    if n2 == n1:
        print(n2)
    elif n1> n2:
        print(n1)
    else:
        print(n2)
elif n1 == n3:
    if n1 == n2:
        print(n1)
    elif n1 > n2:
        print(n1)
    else:
        print(n2)