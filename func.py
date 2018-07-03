#!/usr/bin/python3


def boas_vindas(nome = 'joao',idade = 25):
    print('Oi sou o {} e tenho {} anos'.format(nome,idade))

boas_vindas()
boas_vindas('Daniel',24)
boas_vindas(24,'Daniel')
boas_vindas(idade=24,nome='Daniel')
# boas_vindas('Jose',25)
# boas_vindas('Maria',43)

