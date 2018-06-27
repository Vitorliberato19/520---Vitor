#!/usr/bin/python3

# cont = 0
# while cont >= 10:
#     print('executo')
#     cont += 1

# soma = 0
# while True:
#     num = int(input("digite um numero ou 0 para sair"))
#     if num == 0:
#         break
#     soma += num

# print('total: {}'.format(soma))

'''
lista de nome vazia
ir adicionando nomes ate a pessoa digitar sair

'''


listaNomes = []
while True:
    nome = input('digite o nome para incluir na lista ou sair para finalziar a lista: ')
    if nome.strip().lower() == 'sair':
        break
    listaNomes.append(nome)

print(listaNomes)

nome2 = 'daniel'
print('sim' if nome2 == 'daniel' else 'não')


