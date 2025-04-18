## Faça um programa que leia a altura e largura de uma parede em metros e calcule sua area e a quantidade de
## tinta nescessaria para pintar, sabendo que cada litro pinta 2m quadrados
h = float(input('Qual a altura da parede: '))
b = float(input('Qual a largura: '))
area = b * h
litros = 2
tinta = area / litros
print(f'A area da parede é {area:.3f} metros quadrados e a quantidade de tinta nescessaria é {tinta:.2f} litros')