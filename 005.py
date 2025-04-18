#Faça um programa que leia um número inteiro e mostre o seu sucessor e seu antecessor
from math import floor

n1 = int(input('Digite um valor: '))
menos = n1 - 1
mais = n1 + 1
print(f'O antecessor de {n1} é {menos} e o sucessor é {mais}')