#!/usr/bin/python3
from datetime import datetime
users = ['daniel', 'pedro', 'maria', 'joao']
try:
    while True:
        num = input('User: 0-daniel 1-pedro 2-maria 3-joao sair: ')
        if num == 'sair':
            break
        num = int(num)
        print("O usuario {} está logado!".format(users[int(num)]))
except ValueError as e:
    print("não é inteiro: {}".format(e))
    d = datetime.now()
    with open('loginPython.log', 'a') as arquivo:
        result= "{}, {}".format(e, d.strftime("%Y-%m-%d %H:%M"))
        arquivo.write(result)
   
except IndexError as e:
    print("Não existe essa usuario {}".format(e))
    d = datetime.now()
    with open('loginPython.log', 'a') as arquivo:
        result= "{}, {}".format(e, d.strftime("%Y-%m-%d %H:%M"))
        arquivo.write(result)
        
except KeyboardInterrupt as e:
    print("   ...erro ctrl + c.... ")
    d = datetime.now()
    with open('loginPython.log', 'a') as arquivo:
        result= "{}, {}".format(e, d.strftime("%Y-%m-%d %H:%M"))
        arquivo.write(result)
   


