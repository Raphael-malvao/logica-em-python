#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorcasa = int(input('Valor da casa: '))
salario = int(input('Salário: '))
tempo = int(input('Quantos anos de financiamneto: '))

meses = tempo * 12

prestacao = (salario * 30) / 100
financiamento = valorcasa / meses

if financiamento > prestacao:
    print('negado')
else:
    financiamento = valorcasa / meses
    print(f'O financiamento da casa ficaria em R$ {financiamento}')