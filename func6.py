#!/usr/bin/python3



letras = ['a','b','c','d','e']
letras1 = []
def listar(conteudo):
    for var in conteudo:
        letras1.append('{}\n'.format(var))
    return letras1

        
alterado = listar(letras)

def arqu(aquivotxt,cont):
    try:
        with open(aquivotxt,'w') as arquivo:
            arquivo.writelines(cont)
            return True
    except Exception as e:
        return 'Erro:{}'.format(e)


arqu('NovoFrutas.txt',alterado)

