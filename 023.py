#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número: '))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero //100) % 10
milhar = (numero // 1000)



print(f'unidade: {unidade}')
print(f'dezena {dezena}')
print(f'centena {centena}')
print(f'milhar {milhar}')