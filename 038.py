'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais
'''

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))

if a == b:
    print('OS DOIS VALORES SÃO IGUAIS')

if a > b:
    maior = a
    menor = b
    print('O primeiro valor é maior')
elif a < b:
    menor = a
    maior = b
    print('O segundo valor é maior')

print(f'maior valor foi {maior}')
print(f'menor valor foi {menor}')
