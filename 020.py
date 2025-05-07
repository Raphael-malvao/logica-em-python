# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = input('Aluno 01: ')
aluno2 = input('Aluno 02: ')
aluno3 = input('Aluno 03: ')
aluno4 = input('Aluno 04: ')
todos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(todos)
print(todos)