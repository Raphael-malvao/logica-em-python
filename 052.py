'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
num = int(input('Digite: '))



if num > 1:  # Números menores ou iguais a 1 não são primos
    for divisor in range(2, int(num ** 0.5) + 1):  # Testa até a raiz quadrada
        if num % divisor == 0:  # Se achar um divisor, não é primo
            print(f"{num} não é primo")
            break
    else:  # Se o loop terminar sem break, é primo
        print(f"{num} é primo")
else:
    print(f"{num} não é primo")