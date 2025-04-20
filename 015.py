#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quanto KM você rodou: '))
dias = int(input('Quantos dias voce ficou com o carro: '))
preco = (km * 0.15) + (dias * 60)
print(f'o valor que deve ser pago é R$ {preco}')