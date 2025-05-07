"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo sem considerar espaços
Quantas letras tem o primeiro nome.
"""
nome= input('Digite o nome: ')
print(f'Nome maisculo: {nome.upper()} \nnome com todas minuscuas {nome.lower()}')
print(f'o nome tem {len(nome.replace(" ", ""))} letras')
print(f'O primeiro nome é {(nome.split()[0])} ')
print(f'O primeiro nome tem {len(nome.split()[0])} letras')