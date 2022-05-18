
print('='*75)
print('LOJA SUPER BARATÃO')
print('='*75)

continuar = ''
produtoMil = 0
total = 0
contador = 0
produtoBarato = 0

while True:
	nome = input('Nome do produto: ')
	preço = float(input('Preço: R$ '))
	total += preço

	if preço > 1000:
		contador += 1

	if preço < produtoBarato or produtoBarato == 0:
		produtoBarato = preço
		nomeBarato = nome

	continuar = input('Deseja continuar? [S/N]').strip().upper()[0]

	print(f'\n{"="*75}\nDebug\n{nomeBarato=} {produtoBarato=}\n{"="*75}\n')

	if continuar == 'N':
		break

print(f'\nO total das compras foi R${total:.2f}')
print(f'Temos {contador} produtos custando mais de R$1000.00')
print(f'O nome do produto mais barato é {nomeBarato} e custa R${produtoBarato}')
