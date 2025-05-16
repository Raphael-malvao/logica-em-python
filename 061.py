'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10
primeiros termos da progressão usando a estrutura while.
'''
p1 = int(input('primeiro termo: '))
razao = int(input('razao: '))
c = 1
while c <= 10:
    termo = p1 + (c - 1) * razao
    print(termo)
    c = c+1