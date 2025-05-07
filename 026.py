#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela
# aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite a palavra: ')
frase = frase.lower().strip()

vezes = frase.count('a')
p1 = frase.find('a')
pf = frase.rfind('a')

print(f'A letra A apareceu {vezes} vezes')
print(f'A primeira vez foi na {p1} posição')
print(f'A ultima vez foi na {pf} posição')