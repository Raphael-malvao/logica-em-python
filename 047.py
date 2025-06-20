'''
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''
c = 0
par = c % 2
for c in range (1, 51, 1):
    par = c % 2
    if par == False:
        print(c, end=' -> ')