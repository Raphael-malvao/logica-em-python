'''
 Crie um programa que leia o ano de nascimento de sete pessoas. No final,
 mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
import datetime
import time

maiores = 0
menores = 0
for c in range(7):
    ano = int(input('ANO: '))
    atual = datetime.date.today().year
    nascimento = atual - ano
    if nascimento >= 18:
        maiores += 1
    else:
        menores += 1

print(f'A {maiores} maior de idade')
print(f'A {menores} menor de idade')