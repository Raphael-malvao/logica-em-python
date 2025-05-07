#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o valor 01: '))
n2 = int(input('Digite o valor 02: '))
n3 = int(input('Digite o valor 03: '))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
elif n2 < menor:
    menor = n2

if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3

print(menor)
print(maior)