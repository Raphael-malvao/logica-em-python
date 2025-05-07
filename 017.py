#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot

catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimeto do cateto Adjacente: '))
hipotnusa = hypot(catetoOposto, catetoAdjacente)
print(f'A hipotnusa é {hipotnusa:.2f}')