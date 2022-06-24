

def comparaListas(listaA, listaB, comparaListas = False):
	noaA = 0
	noaB = 0
	noaA = listaA.head

	while noaA != listaA.tail:
		noaB = listaB.head
		while noaA != noaB:
			noaB = noaB.next
			if noaB == listaB.tail:
				return False

		noaA = noaA.next	

	return True

# mudado para uma lista vazia
lista1 = list()
lista1.insertHead(5)
lista1.insertHead(9)
lista1.insertHead(3)
lista1.insertHead(4)

lista2 = list()
lista2.insertHead(9)
lista2.insertTail(3)

lista3 = list()
lista3.insertHead(5)
lista3.insertTail(3)
lista3.insertTail(4)

res1 = comparaListas(lista2, lista1)
res2 = comparaListas(lista3, lista1)
res3 = comparaListas(lista1, lista2)

print('Comparando resultados:')
print('\tLista2 está contida em lista1: ', res1)
print('\tLista3 está contida em lista1: ', res2)
print('\tLista1 está contida em lista2: ', res3)

print('\n', '-'*100)

print('\nResultado esperado:')
print('\tLista2 está contida em lista1: ', True)
print('\tLista3 está contida em lista1: ', True)
print('\tLista1 está contida em lista2: ', False)

