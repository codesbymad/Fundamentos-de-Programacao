#Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores e o quadrado da soma dos três valores.
val1 = float(input())
val2 = float(input())
val3 = float(input())
res1 = (val1**2) + (val2**2) + (val3**2)
res2 = (val1+val2+val3)**2
print(f"{res1:.2f}")
print(f"{res2:.2f}")