#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
# número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

escolhido = random.randint(0,5)
print('Vou pensar em um número aleatorio e quero que você descubra qual')

usuario = int(input('Qual número voce acha que foi digitado: '))
if usuario == escolhido:
    print(f'Voce acertou, eu pensei em {escolhido}')

else:
    print(f'Voce errou, eu pensei em {escolhido}')