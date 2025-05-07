#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.
distancia = int(input('Qual a distancia: '))
passage = 0
if distancia <= 200:
    passagem = (distancia * 0.50)
    print(f'O valor a pagar pelas passagens é de {passagem}')
else:
    passagem = (distancia * 0.45)
    print(f'O valor a pagar pelas passagens é de {passagem}')