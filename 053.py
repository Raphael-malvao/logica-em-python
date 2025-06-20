'''
 Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
'''
# Este código foi desenvolvido por outra pessoa.
# Ele lê uma frase, remove os espaços e verifica se é um palíndromo.

frase = input('Digite uma frase: ').strip().upper()  # Lê a frase e coloca em maiúsculas
frase_sem_espacos = ''.join(frase.split())           # Remove todos os espaços da frase
if frase_sem_espacos == frase_sem_espacos[::-1]:     # Compara a frase com ela invertida
    print('A frase é um palíndromo!')                # Se for igual, é palíndromo
else:
    print('A frase não é um palíndromo.')            # Se não, não é palíndromo
