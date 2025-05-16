'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

total = 0

num = int(input('Digite: '))
for c in range(1, num + 1):
    if num % c ==0:
        total= total +1
    print(c, end=' ')
    print('')

if total <= 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')