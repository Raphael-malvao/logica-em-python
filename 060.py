'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''
n1 = int(input('Digite um número para calcular seu fatorial: '))
f = 1
for i in range(n1, 0, -1):
    print(i)
    f = f*i
print(f'O fatorial de {n1} é {f}')