'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele
ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
#Todas as importaçoes
import datetime

#define o ano atual
anoAtual = datetime.datetime.now().year

anoNascimento = int(input('Ano de nascimento: '))

idade = anoAtual - anoNascimento
if idade < 18:
    print(f'Você ainda tem {idade} anos, faltam {18 - idade} anos para você servir')
elif idade == 18:
    print(f'Você JA TEM {idade} anos, esta no ano exato de voce servir')
else:
    print(f'Já passou {idade - 18} anos de voce se alistar')