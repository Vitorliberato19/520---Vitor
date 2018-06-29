#!/usr/bin/python3
'''
criar um dicionario de frutas e armazenar nome e valor

'''
from pprint import pprint

frutas = [
    {'nome' : 'mamao','valor':10,'qt':11},
    {'nome' : 'laranja','valor':15,'qt':12},
    {'nome' : 'limao','valor':20,'qt':13},
    {'nome' : 'maca','valor':25,'qt':14},
    {'nome' : 'banana','valor':30,'qt':15},
  
]

frutas2 = []
soma = 0
for fruta in frutas:
    fruta['preco'] = fruta['valor']*1.31 + 2
    fruta['precoFinal'] = fruta['preco']*fruta['qt']
    frutas2.append(fruta)
    soma = soma + fruta['preco']*fruta['qt']



pprint(frutas2)

print(soma)
print('Total: {:.2f}'.format(soma))


# print(frutas)
# pprint(frutas)

