'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
import random

print('''Escolha uma das opções a seguir:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
opcao = int(input('Qual sua escolha: '))

aleatorio = ['PEDRA', 'PAPEL', 'TESOURA']
lista = random.choice(aleatorio)

#condicionais
#PEDRA
if opcao == 1 and lista == 'PEDRA':
    print(f'o computador escolheu {lista}')
    print(f'Você escolheu {opcao}, deu IMPATE')
elif opcao == 1 and lista == 'TESOURA':
    print(f'o computador escolheu {lista}')
    print('Você ganhou !!!')
elif opcao == 1 and lista == 'PAPEL':
    print(f'o computador escolheu {lista}')
    print('Você perdeu')

#PAPEL
elif opcao == 2 and lista == 'PAPEL':
    print(f'o computador escolheu {lista}')
    print(f'Você escolheu {opcao}, deu IMPATE')
elif opcao == 2 and lista == 'PEDRA':
    print(f'o computador escolheu {lista}')
    print('Você ganhou !!!')
elif opcao == 2 and lista == 'TESOURA':
    print(f'o computador escolheu {lista}')
    print('Você perdeu')

#TESOURA
elif opcao == 3 and lista == 'TESOURA':
    print(f'o computador escolheu {lista}')
    print(f'Você escolheu {opcao}, deu IMPATE')
elif opcao == 3 and lista == 'PAPEL':
    print(f'o computador escolheu {lista}')
    print('Você ganhou !!!')
else:
    print(f'o computador escolheu {lista}')
    print('Você perdeu')