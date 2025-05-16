'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''
p1 = int(input('primeiro termo: '))
razao = int(input('razao: '))

for c in range(10):
    termo = p1 + c * razao
    print(termo)