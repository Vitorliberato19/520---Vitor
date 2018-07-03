#!/usr/bin/python3

def arqu(aquivotxt):
    try:
        with open(aquivotxt,'r') as arquivo:
            # var = arquivo.readlines()
            var = arquivo.read()
            return var
    except Exception as e:
            return "erro: {}".format(e)



a = arqu('frutas.txt')
b = arqu('frutas2_.txt')
c = arqu('arquivoNomes.txt')

print(a)
print(b)
print(c)
