from random import randint

sorteio = randint(1, 10)

if sorteio <= 5:
	print(f'Número {sorteio} - usuários normais')
	
else:

	print(f'Número {sorteio} - usuários da twitch')
