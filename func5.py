#!/usr/bin/python3

def ler(aquivotxt):
    try:
        with open(aquivotxt,'r') as arquivo:
            # var = arquivo.readlines()
            var = arquivo.read()
            return var
    except Exception as e:
            return "erro: {}".format(e)

with open('NovoFrutas.txt','w') as arqNomes:
    arqNomes.write("")
letras = ['a\n','b\n','c\n','d\n','e\n']
# print(letras)
def arqu(aquivotxt,cont):
    try:
        with open(aquivotxt,'w') as arquivo:
            arquivo.writelines(cont)
            return True
    except Exception as e:
        return 'Erro:{}'.format(e)
        

arqu('NovoFrutas.txt',ler('frutas.txt'))

print(arqu('NovoFrutas.txt',ler('frutas.txt')))


