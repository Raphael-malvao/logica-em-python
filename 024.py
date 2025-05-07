#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
nome = input('Digite o nome da cidade: ')
nome = nome.lower().strip()
print(nome.startswith('santo'))