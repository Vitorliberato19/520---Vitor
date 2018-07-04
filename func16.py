#!/usr/bin/python3
from random import choice, randint



def sorteio2(arquivo):
    with open('arquivoNomes.txt','r') as arq:
        pessoas = arq.readlines()
        print(choice(pessoas))
    
sorteio2('arquivoNomes.txt')
