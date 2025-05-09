'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a
base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

# Leitura do número inteiro
num = int(input('Digite um número inteiro: '))

# Menu de opções
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

# Leitura da opção
opcao = int(input('Sua opção: '))

# Conversão de acordo com a escolha
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Escolha entre 1, 2 ou 3.')