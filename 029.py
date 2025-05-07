#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi
# multado. A multa vai custar R$7,00 por cada Km acima do limite.
multa = 0
v = int(input('Qual a velocidade: '))
if v > 80:
    multa = (v * 7) - 560
    print(f'Você foi multado, sua multa será de R$ {multa:.2f}')
else:
    print('Você não estava acima do limite de velocidade')