#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n1 = int(input('Digite o número: '))

if n1 / 2 != (n1 / 2).__trunc__():
    print(f'O valor {n1} é impar')
else:
    print(f'O número {n1} é par')