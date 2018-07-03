#!/usr/bin/python3

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
        

arqu('NovoFrutas.txt',letras)

print(arqu('NovoFrutas.txt',letras))


