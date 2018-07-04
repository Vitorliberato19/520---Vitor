#!/usr/bin/python3

#args
def boas_vindas(*nomes):
    for item in nomes:
        print("Olá {}, seja bem vindo!".format(item))
    
    print(nomes)  
    print(type(nomes))
    print(len(nomes))

boas_vindas('daniel','rafael','lucia','pedro')
