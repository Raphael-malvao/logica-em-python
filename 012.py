##Faça um algoritimo que leia o preço de um produto x e mostre seru novo preço com 5% de desconto
p1 = float(input('preço original: '))
desconto = (p1 * 5) / 100
final = p1 - desconto
print(f'o preço original é R$ {p1}, com desconto fica R$ {final:.2f}')