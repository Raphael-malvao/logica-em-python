'''
 Desenvolva um programa que leia seis números inteiros e
 mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''
soma = 0
for c in range(0,6):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        soma = soma + valor

print(soma)