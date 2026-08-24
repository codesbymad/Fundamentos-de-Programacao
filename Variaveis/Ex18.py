#Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
saque = int(input())
nota100 = saque//100
rest = saque%100
nota50 = rest//50
rest = rest%50
nota20 = rest//20
rest = rest%20
nota10 = rest//10
rest = rest%10
nota5 = rest//5
rest = rest%5
nota2 = rest//2
nota1 = rest%2
print(nota100)
print(nota50)
print(nota20)
print(nota10)
print(nota5)
print(nota2)
print(nota1)