#!/usr/bin/python3
'''

ler e verificar se ele é par ou impar
e adicionar ele em uma lista com o resultadooo

[2, 'par']
[3, 'impar']
'''
# receber o numero do usuário
num  = float(input('colocar número: '))
# Pegar o resto da divisão por 2
resto = num % 2

# Criar uma lista temporária para preenchimento futuro
lista = [0,'x']

if resto == 0:
    lista[0]=num
    lista[1]='par'
    print(lista)
if resto == 1:
    lista[0]=num
    lista[1]='impar'
    print(lista)
if resto != 1 and resto != 0:
    lista[0]=num
    lista[1]='decimal'
    print(lista)

   





