'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros
'''
from pydoc import describe

#Leitura do valor a ser pago
produto = int(input('Digite o valor a ser pago: '))

#Menu de interação para descobrir qual forma de pagamento
print('''Escolha uma das formas de pagamento:
[ 0 ] à vista dinheiro/cheque: 10% de desconto
[ 1 ] à vista no cartão: 5% de desconto
[ 2 ] em até 2x no cartão: preço formal
[ 3 ] 3x ou mais no cartão: 20% de juros''')

#separe a opcao de escolha do texto que aparece para o usuario para facilitar
opcao = int(input('Sua escolha: '))

#condicinais
if opcao == 0:
    desconto = produto - ((produto * 10) / 100 )
    print(f'{desconto:.2f}')

elif opcao == 1:
    desconto = produto - ((produto * 5) / 100)
    print(f'o valor final ficará: R$ {desconto:.2f}')

elif opcao == 2:
    desconto = produto / 2
    print(f'O valor final ficará em duas parcelas de R$ {desconto:.2f}')

else:
    parcela = produto / 3
    adicional = ((produto * 20) / 100) + produto
    print(f'O valor a ser pago será de tres parcelas de R$ {parcela:.2f} com o preço final sendo de {adicional:.2f}')