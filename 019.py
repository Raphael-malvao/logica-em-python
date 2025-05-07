#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# dos alunos e escrevendo na tela o nome do escolhido.
import random

aluno1 = input('Aluno 01: ')
aluno2 = input('Aluno 02: ')
aluno3 = input('Aluno 03: ')
aluno4 = input('Aluno 04: ')
escolhido = random.choice([aluno1, aluno2, aluno3, aluno4]) #função '.choice' precisa ser uma lista e não argumentos separados, cuidado com isso
print(escolhido)