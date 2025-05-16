'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
maior = 0
v1 = int(input('Valor 01: '))
v2 = int(input('Valor 02: '))
print('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
operacao = int(input('Qual sua opção: '))
while operacao != 5:
    if operacao == 1:
        soma = v1 + v2
        print(f'{v1} + {v2} = {soma}')
        print('''
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
        operacao = int(input('Qual sua opção: '))
    elif operacao == 2:
        mult = v1 * v2
        print(f'{v1} * {v2} = {mult}')
        print('''
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
        operacao = int(input('Qual sua opção: '))
    elif operacao == 3:
        if v1 > v2:
            maior = v1
        elif v1 < v2:
            maior = v2
        else:
            maior = v1
            print('Valores iguais')
            print('''
                    [ 1 ] somar
                    [ 2 ] multiplicar
                    [ 3 ] maior
                    [ 4 ] novos números
                    [ 5 ] sair do programa''')
            operacao = int(input('Qual sua opção: '))
        print(maior)
        print('''
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
        operacao = int(input('Qual sua opção: '))
    elif operacao == 4:
        v1 = int(input('Valor 01: '))
        v2 = int(input('Valor 02: '))
        print('''
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
        operacao = int(input('Qual sua opção: '))
