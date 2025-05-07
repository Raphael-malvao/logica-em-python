#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite o nome completo: ')
nome = nome.split()
primeiro = nome[0]
ultimo = nome[-1]
print(f'Seu nome completo é {" ".join(nome)}, o primeiro é {primeiro} e o ultimo é {ultimo}')