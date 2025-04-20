#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

valor1 = float(input('Digite o angulo: '))
conversaoRadianos = math.radians(valor1) ##Converte a variavel 'valor1' que era originalmente graus em radianos
seno = math.sin(conversaoRadianos)
cosseno = math.cos(conversaoRadianos)
tangente = math.tan(conversaoRadianos)
print(f'O seno de {valor1} é {seno}')
print(f'O cosseno de {valor1} é {cosseno}')
print(f'A tangente de {valor1} é {tangente}')
