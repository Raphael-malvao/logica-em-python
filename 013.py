#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
original = float(input('Salario atual: '))
quantidade = (original * 15) / 100
final = original + quantidade
print(f'O salario original era de R$ {original} , o aumento deixou ele com R$ {final}')