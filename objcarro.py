#!/usr/bin/python3


class Carro():
    def __init__(self, marca, modelo ):
        self.marca = marca
        self.modelo = modelo
        self.gasolina = 10
        self.velociadade = 0
        self.combustivel = 'gasolina'

    def parar(self):
        self.velociadade = 0
        print('o carro parou')
        print('gasolina = {}'.format(self.gasolina))
        print('velocidade = {}'.format(self.velociadade))
        print('\n')

    def andar(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print('o carro está andando...')
            print('\n')
        else:
            self.parar()




    def virar(self, esq, dir):
        self.esq = esq
        self.dir = dir
        if self.esq == 1:
            print('o carro virou a esquerda')
            print('\n')
        if self.dir == 1:
            print('o carro virou a direita')
            print('\n')
        
    def abasteceu(self):
        self.gasolina = 10
        print('tanque cheio!!')
        print('\n')


    def acelerar(self):
        if self.gasolina > 0:
            self.velociadade += 1
            self.gasolina -= 1
            print('acelerando...')
            print('velocidade = {}'.format(self.velociadade))
            print('gasolina = {}'.format(self.gasolina))
            print('\n')
        else:
            self.parar()

    def freiando(self):
        if self.velociadade > 0:
            self.velociadade -= 1
            print('freiando...')
            print('velocidade = {}'.format(self.velociadade))
            print('gasolina = {}'.format(self.gasolina))
            print('\n')
        else:
            self.velociadade = 0
            print('carro parado')

class Carrro_elet(Carro)
    def __init__(self)
        self.combustivel = 'energia'

car_1 = Carro('jetta', 'sedan')

# car_1.andar()
# car_1.parar()
# car_1.virar(1,0)
# car_1.virar(0,1)
# car_1.abasteceu()
# car_1.acelerar()
# car_1.acelerar()
# car_1.freiando()
# car_1.acelerar()
# car_1.acelerar()
# car_1.virar(1,0)
# car_1.acelerar()
# car_1.virar(0,1)
# car_1.acelerar()
# car_1.acelerar()
# car_1.acelerar()
# car_1.acelerar()
# car_1.acelerar()
# car_1.acelerar()
# car_1.abasteceu()




while True:
    comando = input('a = acelerar - f = freiar - ab = abastecer - esq = vire a esquerda - sair ')
    if comando == 'sair':
        break

    if comando == 'a':
        car_1.acelerar()

    if comando == 'f':
        car_1.freiando()
    
    if comando == 'ab':
        car_1.abasteceu()
    
    if comando == 'esq':
        car_1.virar(1,0)

    if comando == 'dir':
        car_1.virar(0,1)

