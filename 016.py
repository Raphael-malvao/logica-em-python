##Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

n1 = float(input('Digite o número: '))
print(f'O número digitado foi {n1}, sua porção inteira é {math.trunc(n1)}')