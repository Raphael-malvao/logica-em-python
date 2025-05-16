'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''


primeiro_peso = float(input('Digite: '))
menor = primeiro_peso
maior = primeiro_peso

for c in range(4):
    peso = float(input('Digite: '))
    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print(menor)
print(maior)