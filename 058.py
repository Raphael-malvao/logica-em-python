'''
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
'''
import random

contador = 1

print('Vou pensar em um número aleatorio entre 1 e 10, quero que você descubra qual')
escolhido = random.randint(0,10)
usuario = int(input('Qual número voce acha que foi digitado: '))
while usuario != escolhido:
    print('Ainda não, tente novamente')
    usuario = int(input('Novo palpite: '))
    contador += 1

print(f'Voce acertou, o número escolhido foi {escolhido}')
print(f'Foram nescerarias {contador} tentativas pra conseguir')