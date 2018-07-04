#!/usr/bin/python3
#args

def boas_vindas(**kargs):
    print(kargs)
    print("olá {} {} seja bem vindo".format(kargs['nome'],kargs['sobrenome']))

boas_vindas(nome='daniel', sobrenome='prata')
