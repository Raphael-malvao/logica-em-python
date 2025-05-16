'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual
é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

contadorMulheres = 0
homemVelho = ''
idadeHomemVelho = 0
somaIdades = 0

# Primeira pessoa (fora do loop)
primeiroNome = input('Digite o seu nome: ')
primeiraIdade = int(input('Digite sua idade: '))
primeiroSexo = input('Sexo [M/F]: ')

somaIdades += primeiraIdade

if primeiroSexo == 'M':
    homemVelho = primeiroNome
    idadeHomemVelho = primeiraIdade

if primeiroSexo == 'F' and primeiraIdade < 20:
    contadorMulheres += 1

# Próximas 3 pessoas (loop)
for c in range(3):
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Sexo [M/F]: ')

    somaIdades += idade

    if sexo == 'M' and idade > idadeHomemVelho:
        homemVelho = nome
        idadeHomemVelho = idade

    if sexo == 'F' and idade < 20:
        contadorMulheres += 1

# Resultados
print(f'Média de idade: {somaIdades/4}')
print(f'Homem mais velho: {homemVelho}')
print(f'Mulheres com menos de 20 anos: {contadorMulheres}')