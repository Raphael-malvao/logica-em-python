#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite o seu nome completo: ')

nome = nome.lower().strip()
procura = 'silva' in nome
print(f'Seu nome tem silva: {procura}')