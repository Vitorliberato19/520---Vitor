#!/usr/bin/python3

class Dog():
    def __init__(self, nome, idade ):
        self.nome = nome
        self.idade = idade
        self.energia = 10

    def latir(self):
        print('au au!')

    def dormindo(self):
        self.energia = 10
        print('Dormindo ZzZzZ ...energia = {}'.format(self.energia))

    def andar(self):
        if self.energia > 0:
            self.energia -=  1
            print('andando...  energia = {}'.format(self.energia))
        elif self.energia <= 0:
            # self.energia = self.energia
            print('tenho q dormir energia = {}'.format(self.energia))
            self.dormindo()
       


dog1 = Dog('bilu', 2)
dog2 = Dog('Python', 3)
print(dog1.nome)
print(dog1.idade)
dog1.latir()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
# dog1.dormindo()
dog1.andar()

