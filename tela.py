#!/usr/bin/python3
# a = ""
# b = ""
# c = ""
# d = ""

var = input('digite: ')
class tela():
    def __init__(self,a,b,c,d,x):
        self.a = ""
        self.b = ""
        self.c = ""
        self.d = ""
        self.x = ""
        self.soma = 0

    def a_(self):
        self.soma += 1
        self.a = self.a + "1"
        self.b = self.b + " "
        self.c = self.c + " "
        self.d = self.d + " "
        if self.soma >=10:
            self.a = self.a[0:10]
            self.b = self.b[0:10]
            self.c = self.c[0:10]
            self.d = self.d[0:10]
            self.soma = 10
        return self.a

    def b_(self):
        self.soma += 1
        self.a = self.a + " "
        self.b = self.b + "2"
        self.c = self.c + " "
        self.d = self.d + " "
        if self.soma >=10:
            self.a = self.a[0:10]
            self.b = self.b[0:10]
            self.c = self.c[0:10]
            self.d = self.d[0:10]
            self.soma = 10
        return self.b

    def c_(self):
        self.soma += 1
        self.a = self.a + " "
        self.b = self.b + " "
        self.c = self.c + "3"
        self.d = self.d + " "
        if self.soma >=10:
            self.a = self.a[0:10]
            self.b = self.b[0:10]
            self.c = self.c[0:10]
            self.d = self.d[0:10]
            self.soma = 10
        return self.c

    def d_(self):
        self.soma += 1
        self.a = self.a + " "
        self.b = self.b + " "
        self.c = self.c + " "
        self.d = self.d + "4"
        if self.soma >=10:
            self.a = self.a[0:10]
            self.b = self.b[0:10]
            self.c = self.c[0:10]
            self.d = self.d[0:10]
            self.soma = 10
        return self.d 

tela1 = tela("a2","b2","c2","d2","x2")

a3 = ""
b3 = ""
c3 = ""
d3 = ""
while True:
    comando = input('digite: ')
    if comando == 'sair':
        break

    if comando == 'a':
       a3 = tela1.a_()

    if comando == 'b':
       b3 = tela1.b_()

    if comando == 'c':
       c3 = tela1.c_()

    if comando == 'd':
       d3 = tela1.d_()

    print('''
    {}
    {}
    {}
    {}
    '''.format( a3,b3,c3,d3))


