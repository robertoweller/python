from sklearn import tree
# Retorna o número se for um número, ou retorna False se não for 
def veri(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:    
        return False

# Compara e exibe qual fruta, se 5 é Limão e 10 é Maça
def analiza(peso, q='boa'):
    x = [[110, 0], [150, 1], [200, 0], [240, 1]]
    y = [5, 5, 10, 10]

    c = tree.DecisionTreeClassifier()
    c = c.fit(x, y)
    if peso:
        fruta = 'Limão' if c.predict([[peso, q]]) == 5 else 'Maça'
        return fruta

peso = veri(input('Digite a gramatura da fruta: ').rstrip('g'))

if peso:
    qua = input('Digite qualidade da fruta [boa/ruim]: ').lower()

    if qua == 'boa':
        print(analiza(peso, 1))
    elif qua == 'ruim':
        print(analiza(peso, 0))
    else:
        fruta = analiza(peso, 1)
        print(f'Desculpa, qualidade invalida, mas acredito que seja {fruta}.')
else:
    print('Desculpa, peso invalido.')
