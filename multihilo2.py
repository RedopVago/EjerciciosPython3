from threading import Thread

import time

class hola(Thread):

    nombre = ''
    inc = 0
    n = 0

    def __init__(self, number, nombre):
        Thread.__init__(self)
        self.nombre = nombre
        self.inc = number

    def run(self):
        print(f'hola {self.nombre}')

        while True:
            print(f'[{self.inc}] {self.n}')
            self.n += self.inc
            time.sleep(self.inc)



if __name__ == '__main__':
    number = [1, 2, 3]
    nombres = ['ana', 'maria', 'jose']
    fechas = ['2000/02/23', '1952/08/12', '1997/12/07']
    lugares = ['Jalisco', 'Colima', 'Nayarit']

    for no, n in zip(number, nombres):
        h = hola(no, n)
        h.start()