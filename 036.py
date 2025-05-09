#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorcasa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
tempoAnos = int(input('Quantos anos de financiamneto: '))

meses = tempoAnos * 12

prestacao = (salario * 30) / 100
financiamento = valorcasa / meses

if financiamento > prestacao:
    print('negado')
else:
    print(f'O financiamento da casa ficaria em R$ {financiamento:.2f}')